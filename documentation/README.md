cooktax
=======


todos
=====
x data model built (optimize?)
- data ingestion
    x script
        x read csv, invoking dictreader
	x assign fields to dict
	- include derived fields somewhere
	x iterate through dict
	x write to new file as json
	x run loaddata
	- fix encoding issue

- write some views:
    - enter an address, return a record
    - find comparables
    	- same neighborhood
	- same building type
    - compare value/sf (derived field) and return result list

- form to capture user address
- form data passed to views that select comparables
- template renders selected comparables
- fancy design
- additional features (like what? think of use cases)
	- ajax to autocomplete address
- deployment
