from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


Role_CHOICES = (
    ("Super_Admin", "Super Admin"),
    ("Company_Lead", "Company Lead"),
    ("Org_Lead", "Orgnisation Lead"),
    ("Dept_Lead", "Department Lead"),
    ("Client_Admin", "Client Admin"),
    ("Proj_Lead", "Project Lead"),
    ("Team_Member", "Team Member"),
    ("Hr", "Hr"),
    ("User", "User"),

)

def get_profile_image_path(self,filename):
    return f'profile_images/{self.id}/{"profile_image.jpg"}'
def get_default_profile_image():
    return 'user.png'

class voc_nps(models.Model):
    brand=models.CharField(max_length=250)
    product=models.CharField(max_length=250)
    upload = models.ImageField(upload_to ='brandlogos/',null=True,blank=True)
    is_accept=models.BooleanField(default=False)
    link=models.CharField(max_length=600,null=True,blank=True)
    username=models.CharField(max_length=250,null=True,blank=True)
    userqrcode = models.ImageField(upload_to ='userqrcodes/',null=True,blank=True)
    qrcodename = models.ImageField(upload_to ='qrcodes/',null=True,blank=True)
    class Meta:
        db_table="voc_nps"
class Rating(models.Model):
    orientation = models.CharField(max_length=50,null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    scolor = models.CharField(max_length=100,null=True,blank=True)
    rcolor = models.CharField(max_length=100,null=True,blank=True)
    fcolor = models.CharField(max_length=100,null=True,blank=True)
    bcolor = models.CharField(max_length=100,null=True,blank=True)
    time = models.CharField(max_length=100,null=True,blank=True)
    format = models.CharField(max_length=50,null=True,blank=True)
    template_name = models.CharField(max_length=50,null=True,blank=True,unique=True)
    text=models.CharField(max_length=250,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        db_table="Rating"
    def __str__(self):
        return self.template_name
class Scale(models.Model):
    maintext=models.TextField(null=True,blank=True)
    class Meta:
        db_table="Scale"
class Rating_Report(models.Model):
    brand=models.CharField(max_length=250,null=True,blank=True)
    product=models.CharField(max_length=250,null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    class Meta:
        db_table="Rating_Report"

class Account(AbstractUser):
    role = models.CharField(
        max_length = 20,
        choices = Role_CHOICES,default="User"
        )
    profile_image=models.ImageField(max_length=255,upload_to=get_profile_image_path,null=True,blank=True,default=get_default_profile_image)
    teamcode=models.CharField(max_length=20,null=True)
    phonecode=models.CharField(max_length=20,null=True)
    phone=models.CharField(max_length=20,null=True)