import csv, json, pprint
import pdb
import datetime

from django.core import management
"""
from django.db.models import *
from compare.models import *
"""
# p = Property.objects.all()

print 'reading in data file...'
#  import csv data as file
datafile = open('FOI22606.CSV','r')

# open file with headers, clean and append to list
headers = open('field_headers.txt','r').read().lower().replace('\n','').split(',')

'converting file to dictreader'
# make a csv dict
datacsv = list(csv.DictReader(datafile,headers))

#pdb.set_trace()

# declare a string to hold json fixture, start by opening an array
jsonstring = '['
# and a buffer file to stage json strings for loading

# keys for models
# property_pk = 1 # using pin
town_pk = 1
res_type_pk = 1
bldg_use_pk = 1
ext_const_pk = 1
bsmt_pk = 1
attic_pk = 1
garage_pk = 1

# so we can track when to write to file
record_counter = 1

# lists to store, check for uniqueness when populating related models
town_names = []
bldg_class_descs = []
res_types = []
bldg_uses = []
ext_const_descs = []
bsmt_descs = []
attic_descs = []
garage_descs = []

print 'commencing data load...'

for line in datacsv:
    # related models first so pk/fk gets incremented
    related_models = [
        {
         'model_name': 'town',
         'id': town_pk,
         'value': {'town':line['town']}, # write a header, header[value] dict
         'value_list': town_names
        },
        {
         'model_name': 'bldgclass',
         'id': line['cls'],
         'value': {'clsdescr':line['clsdescr']},
         'value_list': bldg_class_descs
        },
        {
         'model_name': 'restype',
         'id': res_type_pk,
         'value':{'res_type':line['res_type']},
         'value_list': res_types,
        },
        {
         'model_name': 'bldguse',
         'id': bldg_use_pk,
         'value':{'bldg_use':line['bldg_use']},
         'value_list': bldg_uses,
        },
        {
         'model_name': 'extconst',
         'id': ext_const_pk,
         'value': {'ext_const':line['ext_const']},
         'value_list': ext_const_descs
        },
        {
         'model_name': 'bsmt',
         'id': bsmt_pk,
         'value': {'bsmt':line['bsmt']},
         'value_list': bsmt_descs,
        },
        {
         'model_name': 'attic',
         'id': attic_pk,
         'value': {'attic':line['attic']},
         'value_list': attic_descs
        },
        {
        'model_name': 'garage',
        'id': garage_pk,
        'value': {'gar_des':line['gar_des']},
        'value_list': garage_descs
        }
    ]

    for related_model in related_models:
        if related_model['value'] not in related_model['value_list']:
            fixture = ''
            fixture += '{"pk":'  + str(related_model['id']) + ','
            fixture += '"model": "compare.' + related_model['model_name'] + '",'
            fixture += '"fields":'
            # dump the dict here as json key:value pairs
            fixture += json.dumps(related_model['value'],encoding='latin1') # note encoding
            fixture += "},\n"
            # add this related model fixture to the main fixture
            jsonstring += fixture
            # pprint.pprint(fixture)
            fixture = ''   
            # print related_model['model_name'] + ' pk: ' + str(related_model['id'])
            # ugh ... hack!
            if related_model['model_name'] == 'town':
                town_pk += 1
                town_names.append(related_model['value'])
            elif related_model['model_name'] == 'restype':
                res_type_pk = 1
                res_types.append(related_model['value'])
            elif related_model['model_name'] == 'bldguse':
                bldg_use_pk += 1
                bldg_uses.append(related_model['value'])
            elif related_model['model_name'] == 'extconst':
                ext_const_pk += 1
                ext_const_descs.append(related_model['value'])
            elif related_model['model_name'] == 'bsmt':
                bsmt_pk += 1
                bsmt_descs.append(related_model['value'])
            elif related_model['model_name'] == 'attic':
                attic_pk += 1
                attic_descs.append(related_model['value'])
            elif related_model['model_name'] == 'garage':
                garage_pk += 1
                garage_descs.append(related_model['value'])

        #buildFixture(related_model['model_name'],related_model['id'],related_model['value'],related_model['value_list'])

    # build a new dict specific to the Property model
    prop = {'pin':line['pin'],
            'ml_address':line['ml_address'],
            'pl_address':line['pl_address'],
            'town_id':town_pk,
            'cls_id':line['cls'],
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
            'res_id':res_type_pk,
            'bldg_id':bldg_use_pk,
            'no_of_apts':line['no_of_apts'],
            'ext_const_id':ext_const_pk,
            'full_bath':line['full_bath'],
            'half_bath':line['half_bath'],
            'bsmt_id':bsmt_pk,
            'attic_id':attic_pk,
            'fire_pl':line['fire_pl'],
            'gar_id':garage_pk,
            'age':line['age'],
            'pass_no':line['pass_no'],
            'year':line['year'],
           }  

    # first add metadata
    jsonstring += '{"pk":'  + str(prop['pin']) + ','
    jsonstring += '"model": "compare.property",'
    jsonstring += '"fields":'
    # dump the csv row here as json key:value pairs
    jsonstring += json.dumps(prop,encoding='latin1') # note encoding
    # pprint.pprint(json.dumps(prop))
    jsonstring += "},\n"
    #print 'property pk:' + str(property['pin'])
    # clear out string buffer every 100K lines
    if record_counter % 10000 == 0:
        # declare a file object to save the json string
        buffering_start = datetime.datetime.now() 
        print str(record_counter)
        print 'buffering'
        #print '!!!!!!!!!!!!!!!loading last 100K records!!!!!!!!!!!!!!!!!!!!'
        jsonstring = jsonstring[:-2] # gets rid of trailing comma
        jsonstring += ']' # debug?
        jsonfile.write(jsonstring)
	jsonfile.close() # debug
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
    #print str(record_counter) + ' records'
    record_counter += 1
# fix this last comma issue
jsonstring = jsonstring[:-2]
jsonstring += ']'

# the remaining buffer that wasn't written in the loop
jsonfile.write(jsonstring) 
jsonfile.close()
management.call_command('loaddata','fixture.json')

datafile.close()
headerfile.close()
