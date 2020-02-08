from django.db import models

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
	name = models.CharField(max_length=200, primary_key=True)
	value = models.CharField(max_length=10, choices=VALUE_CHOICES)
	data_type = models.CharField(max_length=10, choices=DATA_CHOICES)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.name