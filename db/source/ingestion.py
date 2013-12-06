import csv, json

from django.core import management

# import csv data as file
# datafile = open('test.csv','r')
datafile = open('FOI22606.CSV','r')

# open file with headers, appending to a string and splitting to a list
headerfile = open('field_headers.txt','r')
headers = ''
for line in headerfile:
    headers += line
headers = headers.lower()
# fix this line break issue
headers = headers.replace('\n','')
headers = headers.split(',')

# metadata
pk = 1
model = "compare.property"

# make a csv dict
datacsv = csv.DictReader(datafile,headers)

# declare empty string, file to hold json fixture
jsonstring = '['
jsonfile = open('output_test.json','w')

for line in datacsv:
    jsonstring += '{"pk":' + str(pk) + ','
    jsonstring += '"model": "' + model + '",'
    jsonstring += '"fields":'
    jsonstring += json.dumps(line,encoding='latin1')
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
        jsonfile = open('output_test.json','w')
        jsonfile.write('')
        jsonstring='['
# fix this last comma issue
jsonstring = jsonstring[:-1]
jsonstring += ']'

# convert data to json
# json.dump(datacsv,jsonfile)

# the remaining buffer that wasn't written in the loop
# jsonfile.write(jsonstring) 
management.call_command('loaddata',jsonstring)

print str(pk) + ' records converted from csv to json fixture.'

"""
# declare dict of derived fields and functions
derivations = {}

# loop through data
for line in dfile:
    for field in line: 
        record = {}
        record[headers[counter]] = hfile[counter] 
        # use counter as index for header, data
        # if header in list of derived fields
            # call function to calculate derivation
        # concatenate header/data together, or use a json library*
        # write to json file
         counter += 1
    fixture.append(record)
# print how much data has been converted to fixture, etc.
# prompt to load into django
# call django import utility

for line in fixture:
    print line
"""
datafile.close()
headerfile.close()
jsonfile.close()
