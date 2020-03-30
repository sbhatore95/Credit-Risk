from django.db import models
from dynamic_models.models import AbstractModelSchema, AbstractFieldSchema
from django import forms
# Create your models here.
class FieldSchema(AbstractFieldSchema):
    pass

class ModelSchema(AbstractModelSchema):
    pass

class CSV(models.Model):
	csv = models.FileField(upload_to='profile/%Y/%m/%d')
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
	name = models.CharField(max_length=10)
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
	x = Feature.objects.values('name')
	# x = [{'name': 'abc'}]
	FEATURE_CHOICES = []
	a = '1'
	for i in x:
		b = (a, i['name'])
		FEATURE_CHOICES.append(b)
		a = a + '1'
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
	feature = models.CharField(max_length=10, null=True, choices=FEATURE_CHOICES)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
	product = models.CharField(max_length=10, choices=PRODUCT_CHOICES)
	weightage = models.FloatField()

	def __str__(self):
		return self.feature