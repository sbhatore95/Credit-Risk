from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Feature
from .models import Configuration
from .forms import FeatureForm
from .forms import ConfigurationForm

from django.urls import reverse
from urllib.parse import urlencode
from .forms import UploadFileForm
import sys
# Create your views here.
class Variable:
	is_changed = "false"

def index(request):
	add = request.GET.get('add')
	form = FeatureForm()
	context = {'form':form, 'add':add}
	return render(request, 'loan_admin/index.html', context)

def configuration(request):
	add = request.GET.get('weigh')
	form = ConfigurationForm()
	context = {'form':form, 'add':add}
	return render(request, 'loan_admin/configuration.html', context)

@require_POST
def addFeature(request):
	form = FeatureForm(request.POST)
	url = reverse('loan_admin:index') 
	if form.is_valid():
		feature = form.save()
		base_url = reverse('loan_admin:index')
		query_string =  urlencode({'add': 'ok'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)

@require_POST
def addConfiguration(request):
	form = ConfigurationForm(request.POST)
	url = reverse('loan_admin:configuration') 
	if form.is_valid():
		feature = form.save()
		base_url = reverse('loan_admin:configuration')
		query_string =  urlencode({'add': 'ok'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)

def uploadCSV(request):
	add = request.GET.get('add')
	form = UploadFileForm()
	context = {'form':form, 'add':add}
	return render(request, 'loan_admin/uploadCSV.html', context)

@require_POST
def addApplicant(request):
	form = UploadFileForm(request.POST, request.FILES)
	url = reverse('loan_admin:uploadCSV')
	print(form.errors)
	print(form.is_valid(), file=sys.stderr)
	if form.is_valid():
		Variable.is_changed = "true"
		form.process_data(request.FILES['file'])
		base_url = reverse('loan_admin:uploadCSV')
		query_string =  urlencode({'add': 'ok'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)
