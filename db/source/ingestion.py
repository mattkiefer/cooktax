import csv, json, gc

from django.core import management

# import csv data as file
datafile = open('FOI22606.CSV','r')

# open file with headers, append to string 
headerfile = open('field_headers.txt','r')
headers = ''
for line in headerfile:
    headers += line
# lowercase to match django model, get rid of extra line break
headers = headers.lower().replace('\n','')
# make a list for csvdict
headers = headers.split(',')

# make a csv dict
datacsv = csv.DictReader(datafile,headers)

# declare a string to hold json fixture, start by opening an array
jsonstring = '['
# declare a file object to save the json string
jsonfile = open('output_test.json','w')

# metadata for django fixture: primary key and model name
pk = 1
model = "compare.property"

for line in datacsv:
    # first add metadata
    jsonstring += '{"pk":'  + str(pk) + ','
    jsonstring += '"model": "' + model + '",'
    jsonstring += '"fields":'
    # dump the csv row here as json key:value pairs
    jsonstring += json.dumps(line,encoding='latin1') # note encoding
    jsonstring += "},"
    print pk
    pk += 1
    # clear out string buffer every 10K lines
    if pk % 10000 == 0:
        print '!!!!!!!!!!!!!!!loading last 10K records!!!!!!!!!!!!!!!!!!!!'
        jsonstring = jsonstring[:-1]
        jsonstring += ']'
        jsonfile.write(jsonstring)
        jsonfile.close()
        management.call_command('loaddata','output_test.json') 
        del jsonfile
        del jsonstring
        del line
        jsonfile = open('output_test.json','w')
        # jsonfile.write('')
        jsonstring='['
        gc.collect()
# fix this last comma issue
jsonstring = jsonstring[:-1]
jsonstring += ']'

# convert data to json
# json.dump(datacsv,jsonfile)

# the remaining buffer that wasn't written in the loop
jsonfile.write(jsonstring) 
jsonfile.close()
management.call_command('loaddata','output_test.json')

datafile.close()
headerfile.close()
