# IPython log file

from compare.models import Property
Property.objects.filter(town__icontains="northfield")
len(_2)
Property.objects.filter(town__icontains="northfield",cls='295')
len(_4)
Property.objects.filter(town__icontains="northfield",cls='295',nbhd='131')
len(_6)
from Set import set
from Sets import set
import sets.Set
from sets import Set
taxcodes = Set([])
for taxcode in Property.objects.filter(town__icontains="northfield",cls='295',nbhd='131'):
    taxcodes.add(taxcode.tax_code)
    
taxcodes
Property.objects.filter(town__icontains="northfield",cls='295',nbhd='131',ext_const__icontains="masonry")
len(_15)
gwcs = Property.objects.filter(town__icontains="northfield",cls='295',nbhd='131',ext_const__icontains="masonry")
for gwc in gwcs:
    print gwc.pl_address, gwc.cur_mktval, int(gwc.cur_mktval)/int(gwc.bldg_sqft)
    
for gwc in gwcs:
    print gwc.pl_address, gwc.cur_mktval, int(gwc.cur_mktval)/gwc.bldg_sqft
    
for gwc in gwcs:
    print gwc.pl_address, gwc.cur_mktval, gwc.cur_mktval/gwc.bldg_sqft
    
for gwc in gwcs:
    print gwc.pl_address, gwc.cur_mktval, gwc.bldg_sqft, int(gwc.cur_mktval)/int(gwc.bldg_sqft)
    
get_ipython().magic(u'pinfo %logstart')
get_ipython().magic(u'logstart')
exit()
