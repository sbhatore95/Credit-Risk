from django import forms
from .models import Feature
from .models import Configuration
from .models import ModelSchema, FieldSchema
from .models import CSV
import csv
import io
class FeatureForm(forms.ModelForm):
	# name = forms.CharField()
	# value  = forms.CharField(widget=forms.Select(
	# 		attrs={
	# 			'class': 'form-control',
	# 		}
	# 	))
	class Meta:
		model = Feature
		fields = ['name', 'value', 'data_type', 'category']

class ConfigurationForm(forms.ModelForm):
	class Meta:
		model = Configuration
		fields = '__all__'

class UploadFileForm(forms.Form):
	file = forms.FileField()
	def process_data(self, f):
		with open('dataset.csv', 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
		destination.close()

class CSVForm(forms.Form):
	class Meta:
		model = CSV
		fields = '__all__'

	data_file = forms.FileField()

	def process_data(self, f):
		# f = self.cleaned_data['data_file'].file
		# reader = csv.DictReader(f)
		# rest = [row for row in reader]
		with open('dataset.csv', 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
		destination.close()
		# if len(ModelSchema.objects.all()) != 0:
		# 	applicant_model_schema = ModelSchema.objects.first()
		# else:
		# 	applicant_model_schema = ModelSchema.objects.create(name='LoanApplicant')
		# field_schema = FieldSchema.objects.create(name='all_field', data_type='character')
		# color = applicant_model_schema.add_field(
		# 	field_schema,
		# 	null = True,
		# )
		# LoanApplicant = applicant_model_schema.as_model()
		# for j in rest:
		# 	a = LoanApplicant(all_field=j)
		# 	a.save()
