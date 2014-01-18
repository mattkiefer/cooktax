from django.db import models

# todo
# normalize tables
# add indices, pks
# add fk relations
# modify types, max_lengths

class Property(models.Model):
    pin = models.CharField(max_length=20) # index
    ml_address=models.CharField(max_length=20)
    pl_address=models.CharField(max_length=20)
    town=models.CharField(max_length=20) # index
    cls=models.CharField(max_length=20) # index
    clsdescr=models.CharField(max_length=20) # cls
    triennial=models.CharField(max_length=20) # index
    land_sqft=models.CharField(max_length=20) 
    bldg_sqft=models.CharField(max_length=20)
    nbhd=models.CharField(max_length=20) # index
    tax_code=models.CharField(max_length=20) # index
    cur_land=models.CharField(max_length=20)
    cur_bld=models.CharField(max_length=20)
    cur_total=models.CharField(max_length=20)
    cur_mktval=models.CharField(max_length=20)
    pri_land=models.CharField(max_length=20)
    pri_bldg=models.CharField(max_length=20)
    pri_total=models.CharField(max_length=20)
    pri_mktval=models.CharField(max_length=20)
    res_type=models.CharField(max_length=20) # index
    bldg_use=models.CharField(max_length=20) # index  
    no_of_apts=models.CharField(max_length=20) # int
    ext_const=models.CharField(max_length=20) # index
    full_bath=models.CharField(max_length=20) # int
    half_bath=models.CharField(max_length=20) # int
    bsmt=models.CharField(max_length=20) # index
    attic=models.CharField(max_length=20) # index
    fire_pl=models.CharField(max_length=20) # int
    gar_des=models.CharField(max_length=20) # index
    age=models.CharField(max_length=20) # int
    pass_no=models.CharField(max_length=20) # int
    year=models.CharField(max_length=20) # int
    
    def __unicode__(self):
        return self.pin

