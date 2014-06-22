import csv, json, pprint, datetime, pdb
from django.core import management

def output_log(record_counter):
    log_file_name = './logs/ingestion.log'
    if record_counter == 0:
        open(log_file_name,'w').write('')
    log = open(log_file_name,'a')
    log.write(str(record_counter) + '\n')
    log.close()

print 'reading in data file...'
#  import csv data as file
datafile = open('FOI22606.CSV','r')

# open file with headers, clean and append to list
headers = open('field_headers.txt','r').read().lower().replace('\n','').split(',')

print 'converting file to dictreader'
# make a csv dict
datacsv = csv.DictReader(datafile,headers)

# declare a string to hold json fixture, start by opening an array
jsonstring = '['
# and a buffer file to stage json strings for loading

# objects to hold information about related models
class RelatedModel:
    def __init__(self,name,header,field):
        self.model_name = name
        self.csv_header = header
        self.field = field
    id = 0
    value = None
    value_list = {}

# map the model names to csv header for import helper objects
model_names = [{'name':'town', 'header':'town', 'field':'town_desc' },
               {'name':'bldgclass', 'header':'clsdescr',  'field':'bldg_cls_desc' },
               {'name':'restype',  'header':'res_type', 'field':'res_type_desc' },
               {'name':'bldguse', 'header':'bldg_use', 'field':'bldg_use_desc' },
               {'name':'extconst', 'header':'ext_const', 'field':'ext_const_desc' },
               {'name':'bsmt', 'header':'bsmt', 'field':'bsmt_desc' },
               {'name':'attic', 'header':'attic', 'field':'attic_desc' },
               {'name':'garage', 'header':'gar_des', 'field':'gar_desc' },
              ]          

import_objects = []

for model_name in model_names:
    import_objects.append(RelatedModel(model_name['name'],model_name['header'],model_name['field']))

# look up current related model id by csv header, value
def get_rel_model_id(name, value, import_objects=import_objects):
    #if name == 'clsdescr': pdb.set_trace()
    return [x.value_list[line[name]] for x in import_objects if x.csv_header == name and x.value == value][0]


# so we can track when to write to file
record_counter = 1

print 'commencing data load...'

for line in datacsv:
    # related models first so pk/fk gets incremented
    for import_object in import_objects:
        import_object.value = line[import_object.csv_header]
        if import_object.value not in import_object.value_list:
            import_object.id += 1 # increment the fk
            import_object.value_list[import_object.value] = import_object.id # add value to unique list 
            fixture = ''
            fixture += '{"pk":'  + str(import_object.id) + ','
            fixture += '"model": "compare.' + import_object.model_name + '",'
            fixture += '"fields":'
            # dump the dict here as json key:value pairs
            # special case for bldgclass
            if import_object.model_name == 'bldgclass':
                fixture += json.dumps({import_object.field:import_object.value, 'old_cls':line['cls']},encoding='latin1')
            else:
                fixture += json.dumps({import_object.field:import_object.value},encoding='latin1') # note encoding
            fixture += "},\n"
        # add this related model fixture to the main fixture
        jsonstring += fixture
        fixture = ''   

    # build a new dict specific to the Property model
    prop = {'pin':line['pin'],
            'ml_address':line['ml_address'],
            'pl_address':line['pl_address'],
            'town':get_rel_model_id('town',line['town']),
            'bldg_cls':get_rel_model_id('clsdescr',line['clsdescr']),
            'triennial':line['triennial'],
            'land_sqft':line['land_sqft'],
            'bldg_sqft':line['bldg_sqft'],
            'nbhd':line['nbhd'],
            'tax_code':line['tax_code'],
            'cur_land':line['cur_land'],
            'cur_bld':line['cur_bld'],
            'cur_total':line['cur_total'],
            'cur_mktval':line['cur_mktval'],
            'pri_land':line['pri_land'],
            'pri_bldg':line['pri_bldg'],
            'pri_total':line['pri_total'],
            'pri_mktval':line['pri_mktval'],
            'res_type':get_rel_model_id('res_type',line['res_type']),
            'bldg_use':get_rel_model_id('bldg_use',line['bldg_use']),
            'no_of_apts':line['no_of_apts'],
            'ext_const':get_rel_model_id('ext_const',line['ext_const']),
            'full_bath':line['full_bath'],
            'half_bath':line['half_bath'],
            'bsmt':get_rel_model_id('bsmt',line['bsmt']),
            'attic':get_rel_model_id('attic',line['attic']),
            'fire_pl':line['fire_pl'],
            'gar':get_rel_model_id('gar_des',line['gar_des']),
            'age':line['age'],
            'pass_no':line['pass_no'],
            'year':line['year'],
           }  

    # first add metadata
    jsonstring += '{"pk":'  + str(prop['pin']) + ','
    jsonstring += '"model": "compare.property",'
    jsonstring += '"fields":'
    # dump the csv row here as json key:value pairs
    jsonstring += json.dumps(prop)
    jsonstring += "},\n"
    # clear out string buffer every 100K lines
    if record_counter % 10000 == 0:
        # put this in a function
        # declare a file object to save the json string
        buffering_start = datetime.datetime.now() 
        print str(record_counter)
        print 'buffering'
        jsonstring = jsonstring[:-2] # gets rid of trailing comma
        jsonstring += ']'
        jsonfile = open('fixture.json','w')
        jsonfile.write(jsonstring)
	jsonfile.close() 
        
        # put this in a function
        buffering_end = datetime.datetime.now()
        buffering_time = buffering_end - buffering_start
        print 'buffering time: ' + str(buffering_time.seconds)
        print 'loading'
        loading_start = datetime.datetime.now()
        management.call_command('loaddata','fixture.json')
        loading_end = datetime.datetime.now()
        loading_time = loading_end - loading_start
        print 'loading time: ' + str(loading_time.seconds)
        jsonfile = open('fixture.json','w')
        jsonstring = '['
    output_log(record_counter)
    record_counter += 1
jsonstring = jsonstring[:-2]
jsonstring += ']'

# the remaining buffer that wasn't written in the loop
jsonfile.write(jsonstring) 
jsonfile.close()
management.call_command('loaddata','fixture.json')

datafile.close()
headerfile.close()
