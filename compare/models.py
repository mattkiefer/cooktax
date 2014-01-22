from django.db import models

# todo
# normalize tables
# add indices, pks
# add fk relations
# modify types, max_lengths

class Property(models.Model):
    pin = models.IntegerField(primary_key=True) # index
    ml_address=models.CharField(max_length=50)
    pl_address=models.CharField(max_length=50)
    townid=models.ForeignKey('Town')
    cls=models.ForeignKey('BldgClass')
    triennial=models.CharField(max_length=4) # n/w city s/w
    land_sqft=models.IntegerField() # good story idea here
    bldg_sqft=models.IntegerField()
    nbhd=models.IntegerField()
    tax_code=models.IntegerField()
    cur_land=models.IntegerField()
    cur_bld=models.IntegerField()
    cur_total=models.IntegerField()
    cur_mktval=models.IntegerField()
    pri_land=models.IntegerField()
    pri_bldg=models.IntegerField()
    pri_total=models.IntegerField()
    pri_mktval=models.IntegerField()
    res_code=models.ForeignKey('ResType')
    bldg_code=models.ForeignKey('BldgUse')
    no_of_apts=models.IntegerField()
    ext_const_code=models.ForeignKey('ExtConst')
    full_bath=models.IntegerField()
    half_bath=models.IntegerField()
    bsmt_code=models.ForeignKey('Bsmt')
    attic_code=models.IntegerField('Attic')
    fire_pl=models.IntegerField()
    gar_code=models.IntegerField('Garage')
    age=models.IntegerField()
    pass_no=models.IntegerField() # 1, 2
    year=models.IntegerField() # 2013
    
    def __unicode__(self):
        return self.pin

class Town (models.Model):
    townid = models.IntegerField(primary_key=True)
    townname = models.CharField(max_length=20, unique=True)

class BldgClass (models.Model):
    cls=models.IntegerField(primary_key=True) # primary key
    clsdescr=models.CharField(max_length=20, unique=True) # cls

class ResType (models.Model):
    res_code = models.IntegerField(primary_key=True) 
    res_type = models.CharField(max_length=11, unique=True)

class BldgUse (models.Model):
    bldg_code = models.IntegerField(primary_key=True) 
    bldg_use = models.CharField(max_length=13, unique=True)

class ExtConst (models.Model):
    ext_const_code = models.IntegerField(primary_key=True)
    ext_const_desc = models.CharField(max_length=13, unique=True) 

class Bsmt (models.Model):
    bsmt_code = models.IntegerField(primary_key=True)
    bsmt_desc = models.CharField(max_length=26, unique=True) 

class Attic (models.Model):
    attic_code = models.IntegerField(primary_key=True)
    attic_desc = models.CharField(max_length=21, unique=True )

class Garage (models.Model):
    gar_code = models.IntegerField(primary_key=True) 
    gar_desc = models.CharField(max_length=20, unique=True)


