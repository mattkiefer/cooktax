"""
TODO
write looping logic
start with the first branch and descend continuously
standard looping will make its way down and then work its way back up
"""

import django
from compare.models import Property
from numpy import median
import os


### START CONFIG ###
base_dir = os.path.dirname(os.path.abspath(__file__)) # same dir as this file by default
l = 1000
max_json_length = 100
### END CONFIG ###


class TreeBuild(object): 

    def __init__(self,l):
        self.base_dir = base_dir
	self.parent_dir = self.base_dir
	self.this_dir = base_dir
        self.pin_adds = self.buildQuery(l)
        self.doMath()


    def buildQuery(self,l):
	limit = l and "limit {!s}".format(l) or ""

	query = """
	    select pin, pl_address
	    from compare_property
            where length(pl_address) > 10
	    order by pl_address
	    {!s}
	    """.format(limit)
  
        return self.pin_add_ord(query)


    def pin_add_ord(self,query):
        """
        for a given query,
	returns dict of {index: (pin, address)}
        """
        results = Property.objects.raw(query)
	rdict = {}
        index = 1
        for result in results:
            rdict[index] = (result.pin,result.pl_address)
            index += 1
        return rdict    

    
    def keyList(self):
        """
	returns list of
	dictionary indices
        because math
        """ 
	return [x for x in self.pin_adds.iterkeys()]


    def doMath(self):
        """
        given a dict or subset,
        find median, max of index
        and mk dirs for their address values
	"""
        # get list of current dict indices
        self.key_list = self.keyList()
        # do the math
        self.key_min = min(key_list)
        self.key_median = int(median(key_list)) # note that this rounds down
        self.key_max = max(key_list)
	# med, max addresses as naming conventions
        self.med_address = self.pin_adds[key_median][1]
	self.max_address = self.pin_adds[key_max][1]
	# index lists of top and bottom halves
        self.hi = [ x for x in range(self.key_median, self.key_max) if x != self.key_median ] # don't list median twice
        self.lo = [ x for x in range(self.key_min, self.key_median)]    


    def branchOrLeaf(self,max_json_length):
	"""
	if current list of keys is longer than max,
	make split directories
	"""
        if len(self.key_list) > max_json_length:
	    dirs = self.makeDirs()
            self.updateDirs()
	else:
	    self.writeFiles()


    def makeDirs(self):
	"""
	docstring
	"""
        # make nodes from address (second item in tuple)
        os.mkdir(med_address)
        os.mkdir(max_address)
        return dict('med':med_address,'max':max_address)
	
    def updateDirs(self,new_dir):
	"""
	change dirs
	update this dir, parent dir
	"""
	self.parent_dir = self.this_dir
        self.this_dir = self.parent_dir + '/' + new_dir
        # needs work ...


    def writeFiles(self):
	"""
	docstring
	"""
	file_name = self.lo + '.json'
	outfile = open(self.file_name,'w')
	# need pin: address pairs here
	# TODO: write a separate json transform method
        outfile.write(self.pin_adds[x] for x in range(self.key_min,self.key_max))


    def drillDown(self):
	"""
	loop called by init?
	will doMath on current selection
	branchOrLeaf down to the bottom
	needs to know: cwd, current query slice
	"""
	pass


# to write the final json file
# given a range of numbers
# write the dict in this way
# dict((x,y) for x,y in d.iteritems() if x <= med)
