from django.db import models
from dynamic_models.models import AbstractModelSchema, AbstractFieldSchema

# Create your models here.
class FieldSchema(AbstractFieldSchema):
    pass

class ModelSchema(AbstractModelSchema):
    pass

class CSV(models.Model):
	csv = models.FileField(upload_to='profile/%Y/%m/%d')

class SavedState(models.Model):
	stat = models.CharField(max_length=10)
	ml = models.CharField(max_length=10)
	statandml = models.CharField(max_length=10, default="false")

class Feature(models.Model):
	file = models.FileField()
	columns = models.CharField(max_length=1000000)
	nominal_features = models.CharField(max_length=1000000)