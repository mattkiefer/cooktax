from django.db import models

#  todo
# normalize tables
# add indices, pks
# add fk relations
# modify types, max_lengths

class Property(models.Model):
    pin=models.CharField(primary_key=True,db_index=True,max_length=14) 
    ml_address=models.CharField(max_length=50)
    pl_address=models.CharField(max_length=50)
    town=models.ForeignKey('Town')
    bldg_cls=models.ForeignKey('BldgClass')
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
    res_type=models.ForeignKey('ResType')
    bldg_use=models.ForeignKey('BldgUse')
    no_of_apts=models.IntegerField()
    ext_const=models.ForeignKey('ExtConst')
    full_bath=models.IntegerField()
    half_bath=models.IntegerField()
    bsmt=models.ForeignKey('Bsmt')
    attic=models.ForeignKey('Attic')
    fire_pl=models.IntegerField()
    gar=models.ForeignKey('Garage')
    age=models.IntegerField()
    pass_no=models.IntegerField() # 1, 2
    year=models.IntegerField() # 2013
    #coolpic = models.Boolean() # 01011000030000 

    #this should come in through ingestion
    @property
    def quo_cmv_bsf(self): # quotient: current market value / bldg sq ft 
        return round(self.cur_mktval / float(self.bldg_sqft),2)

    @property
    def img_url(self):
        url = 'http://www.cookcountyassessor.com/ImageStreamer/StreamImage.aspx?pin=' + str(self.pin14(self.pin))
        return url

    def __unicode__(self):
        return unicode(self.pin)

    def pin14(self,pin):
        if len(str(pin)) == 13:
            pin = '0' + str(pin)
        return pin

class Town (models.Model):
    town = models.IntegerField(primary_key=True,db_index=True)
    town_desc = models.CharField(max_length=20, unique=True)

class BldgClass (models.Model):
    bldg_cls=models.IntegerField(primary_key=True,db_index=True) # primary key
    bldg_cls_desc=models.CharField(max_length=20)#, unique=True) # cls *** check this
    old_cls=models.CharField(max_length=4)

class ResType (models.Model):
    res_type = models.IntegerField(primary_key=True,db_index=True) 
    res_type_desc = models.CharField(max_length=11, unique=True)

class BldgUse (models.Model):
    bldg_use = models.IntegerField(primary_key=True,db_index=True) 
    bldg_use_desc = models.CharField(max_length=13, unique=True)

class ExtConst (models.Model):
    ext_const = models.IntegerField(primary_key=True,db_index=True)
    ext_const_desc = models.CharField(max_length=13, unique=True) 

class Bsmt (models.Model):
    bsmt = models.IntegerField(primary_key=True,db_index=True)
    bsmt_desc =  models.CharField(max_length=26, unique=True) 

class Attic (models.Model):
    attic = models.IntegerField(primary_key=True,db_index=True)
    attic_desc = models.CharField(max_length=21, unique=True )

class Garage (models.Model):
    gar = models.IntegerField(primary_key=True,db_index=True) 
    gar_desc = models.CharField(max_length=20, unique=True)


