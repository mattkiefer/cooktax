from django.db import models

#  todo
# normalize tables
# add indices, pks
# add fk relations
# modify types, max_lengths

class Property(models.Model):
    pin = models.IntegerField(primary_key=True,db_index=True) # index
    ml_address=models.CharField(max_length=50)
    pl_address=models.CharField(max_length=50)
    town_id=models.ForeignKey('Town')
    cls_id=models.ForeignKey('BldgClass')
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
    res_id=models.ForeignKey('ResType')
    bldg_id=models.ForeignKey('BldgUse')
    no_of_apts=models.IntegerField()
    ext_const_id=models.ForeignKey('ExtConst')
    full_bath=models.IntegerField()
    half_bath=models.IntegerField()
    bsmt_id=models.ForeignKey('Bsmt')
    attic_id=models.ForeignKey('Attic')
    fire_pl=models.IntegerField()
    gar_id=models.ForeignKey('Garage')
    age=models.IntegerField()
    pass_no=models.IntegerField() # 1, 2
    year=models.IntegerField() # 2013
    
    def __unicode__(self):
        return unicode(self.pin)

class Town (models.Model):
    town_id = models.IntegerField(primary_key=True,db_index=True)
    town = models.CharField(max_length=20, unique=True)

class BldgClass (models.Model):
    cls_id=models.IntegerField(primary_key=True,db_index=True) # primary key
    clsdescr=models.CharField(max_length=20)#, unique=True) # cls *** check this

class ResType (models.Model):
    res_id = models.IntegerField(primary_key=True,db_index=True) 
    res_type = models.CharField(max_length=11, unique=True)

class BldgUse (models.Model):
    bldg_id = models.IntegerField(primary_key=True,db_index=True) 
    bldg_use = models.CharField(max_length=13, unique=True)

class ExtConst (models.Model):
    ext_const_id = models.IntegerField(primary_key=True,db_index=True)
    ext_const = models.CharField(max_length=13, unique=True) 

class Bsmt (models.Model):
    bsmt_id = models.IntegerField(primary_key=True,db_index=True)
    bsmt =  models.CharField(max_length=26, unique=True) 

class Attic (models.Model):
    attic_id = models.IntegerField(primary_key=True,db_index=True)
    attic = models.CharField(max_length=21, unique=True )

class Garage (models.Model):
    gar_id = models.IntegerField(primary_key=True,db_index=True) 
    gar_des = models.CharField(max_length=20, unique=True)


