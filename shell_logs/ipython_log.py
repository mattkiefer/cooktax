# IPython log file

from compare.models import *
Property.__dict__
Property.__doc__
Property.objects.filter(pl_address__startswith="1336 GREENWILLOW")
Property.objects.filter(pl_address__startswith=" 1336 GREENWILLOW")
gw = Property.objects.filter(pl_address__startswith=" 1336 GREENWILLOW")
for p in gw:
    p.id
    
for p in gw:
    p.pin
    
gw
for p in gw:
    p
    
len(list(gw))
for p in list(gw):
    p
    
list(gw)
list(gw)[0]
for p in gw:
    print p.pin, p.ml_address, p.cur_mktval
    
for p in gw:
    print p.pin, p.pl_address, p.cur_mktval
    
pin = 4351240120000
home = Property.objects.filter(pin=4351240120000)
home
home.__dict__
home = Property.objects.get(pin=4351240120000)
home.__dict__
n = home.nbhd
bc = home.bldg_cls
comps = Property.objects.filter(bldg_cls=bc,nbhd=n)
len(list(comps))
t = home.town
comps = Property.objects.filter(bldg_cls=bc,nbhd=n,town=t)
len(list(comps))
for x in comps:
    x.pl_address, x.cur_mktval
    
for x in comps:
    print x.pl_address, x.cur_mktval
    
for x in comps:
    print x.pl_address, x.cur_mktval/x.bldg_sqft
    
for x in comps:
    print x.pin, x.pl_address, x.cur_mktval/x.bldg_sqft
    
home
home.pin
get_ipython().magic(u'logstart')
exit()
