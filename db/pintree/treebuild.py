import django
from compare.models import Property
from numpy import median
import os


### START CONFIG ###
l = 1000
### END CONFIG ###

class TreeBuild(object): 

    def __init__(self,l):
        self.base = os.getcwd()
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
	return [x for x in self.pin_adds.iterkeys()]

    def doMath(self):
        """
        given a dict or subset,
        find median, max of index
        and mk dirs for their address values
	"""
        key_list = self.keyList()
        key_median = round(median(key_list),0) # rounding because indices are whole ints
        key_max = max(key_list)
        # import pdb; pdb.set_trace()
        os.mkdir(str(self.pin_adds[key_median][1])) # address is second item in value tuple
        os.mkdir(str(self.pin_adds[key_max][1]))
