from django.db import models

class Property(models.Model):
    pin = models.CharField(max_length=20)
    ml_address=models.CharField(max_length=20)
    pl_address=models.CharField(max_length=20)
    town=models.CharField(max_length=20)
    cls=models.CharField(max_length=20)
    clsdescr=models.CharField(max_length=20)
    triennial=models.CharField(max_length=20)
    land_sqft=models.CharField(max_length=20)
    bldg_sqft=models.CharField(max_length=20)
    nbhd=models.CharField(max_length=20)
    tax_code=models.CharField(max_length=20)
    cur_land=models.CharField(max_length=20)
    cur_bld=models.CharField(max_length=20)
    cur_total=models.CharField(max_length=20)
    cur_mktval=models.CharField(max_length=20)
    pri_land=models.CharField(max_length=20)
    pri_bldg=models.CharField(max_length=20)
    pri_total=models.CharField(max_length=20)
    pri_mktval=models.CharField(max_length=20)
    res_type=models.CharField(max_length=20)
    bldg_use=models.CharField(max_length=20)
    no_of_apts=models.CharField(max_length=20)
    ext_const=models.CharField(max_length=20)
    full_bath=models.CharField(max_length=20)
    half_bath=models.CharField(max_length=20)
    bsmt=models.CharField(max_length=20)
    attic=models.CharField(max_length=20)
    fire_pl=models.CharField(max_length=20)
    gar_des=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    pass_no=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.pin

