from django.db import models
from dynamic_models.models import AbstractModelSchema, AbstractFieldSchema
from django import forms
# Create your models here.
class FieldSchema(AbstractFieldSchema):
    pass

class ModelSchema(AbstractModelSchema):
    pass

class UploadFile(models.Model):
	file = models.FileField(upload_to='credit_risk/dataset')
	columns = models.CharField(max_length=1000000)
	nominal_features = models.CharField(max_length=1000000)
# Create your models here.
class Feature(models.Model):
	VALUE_CHOICES = [
		('Bi', 'Binary'),
		('No', 'Nominal'),
		('In', 'Interval'),
		('Ra', 'Ratio'),

	]
	DATA_CHOICES = [
		('Nu', 'Numeric'),
		('Ch', 'Character'),
		('Da', 'Date'),
	]
	CATEGORY_CHOICES = [
		('In', 'Individual'),
		('Co', 'Company'),
		('Cy', 'Country'),
	]
	name = models.CharField(max_length=100)
	value = models.CharField(max_length=10, choices=VALUE_CHOICES)
	data_type = models.CharField(max_length=10, choices=DATA_CHOICES)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.name

class Configuration(models.Model):
	# FEATURE_CHOICES = [
	# 	('In', 'Individual'),
	# 	('Co', 'Company'),
	# 	('Cy', 'Country'),
	# ]
	CATEGORY_CHOICES = [
		('In', 'Individual'),
		('Co', 'Company'),
		('Cy', 'Country'),
	]
	PRODUCT_CHOICES = [
		('Ag', 'Agricultural'),
		('Ho', 'Home'),
		('Pe', 'Personal'),
		('Ve', 'Vehicle'),
	]
	feature = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
	product = models.CharField(max_length=10, choices=PRODUCT_CHOICES)
	weightage = models.FloatField()

	def __str__(self):
		return self.feature

class Criteria(models.Model):
	feature = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=10)
	product = models.CharField(max_length=10)
	data_source = models.CharField(max_length=10)
	api = models.CharField(max_length=10000)
	key = models.CharField(max_length=100)

class CriteriaHelper(models.Model):
	criteria = models.ForeignKey(Criteria, 
		on_delete=models.CASCADE,)
	entry = models.CharField(max_length=1000000)
	score = models.IntegerField()