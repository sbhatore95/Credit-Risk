from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Feature
from .models import Configuration
from .forms import FeatureForm
from .forms import ConfigurationForm

from django.urls import reverse
from urllib.parse import urlencode
from .forms import UploadFileForm, CriteriaForm
import sys
from .counter import *
# Create your views here.

def index(request):
	add = request.GET.get('add')
	form = FeatureForm()
	if(add == 'ok1'):
		context = {'form':form, 'add':add}
	else:
		context = {'form':form}
	return render(request, 'loan_admin/index.html', context)

def configuration(request):
	add = request.GET.get('add1')
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
		query_string =  urlencode({'add': 'ok1'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)

@require_POST
def addConfiguration(request):
	form = ConfigurationForm(request.POST)
	url = reverse('loan_admin:configuration') 
	if form.is_valid():
		feature = form.save()
		base_url = reverse('loan_admin:configuration')
		query_string =  urlencode({'add1': 'ok2'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)

def criteria(request):
	add = request.GET.get('add2')
	form = CriteriaForm()
	counter = Counter()
	if(add == 'ok3'):
		context = {'form':form, 'counter':counter, 'add':add}
	else:
		context = {'form':form, 'counter':counter}
	return render(request, 'loan_admin/criteria.html', context)

@require_POST
def addCriteria(request):
	form = CriteriaForm(request.POST)
	url = reverse('loan_admin:criteria') 
	if form.is_valid():
		feature = form.save()
		base_url = reverse('loan_admin:criteria')
		query_string =  urlencode({'add2': 'ok3'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)

def uploadCSV(request):
	add = request.GET.get('add3')
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
		form.process_data(request.POST, request.FILES['file'])
		base_url = reverse('loan_admin:uploadCSV')
		query_string =  urlencode({'add3': 'ok4'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)