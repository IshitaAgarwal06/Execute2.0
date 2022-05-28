from xml.dom import ValidationErr
from django.db import models

def validate_file_extension(value):
    if not value.name.endswith('.csv' or '.xlsx'):
        raise ValidationErr(u'ONLY CSV OR .xlsx IS ACCEPTED')

class details(models.Model):
	uniqueid=models.CharField(max_length=100,default="0")
	companyname=models.CharField(max_length=100)
	businesstype=models.CharField(max_length=100)
	productname=models.CharField(max_length=100)
	targetaudience=models.CharField(max_length=100)
	theinfo=models.FileField(default="images/default.pdf",validators=[validate_file_extension])
	fileuploaded=models.BooleanField(default=False)
	mail=models.CharField(max_length=1000)
	phno=models.CharField(max_length=100)
	accepted=models.BooleanField(default=False)



