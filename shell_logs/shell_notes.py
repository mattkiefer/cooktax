# make this a simple view
# time this every time you optimize

import time

start = time.time()

from compare.models import Property

gwcs = Property.objects.filter(town__icontains="northfield",cls='295',nbhd='131',ext_const__icontains="masonry")

for gwc in gwcs:
    print gwc.pl_address, gwc.cur_mktval, int(gwc.cur_mktval)/int(gwc.bldg_sqft)


end = time.time()

print 'time elapsed: ' + str(end - start)
