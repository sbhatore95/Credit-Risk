from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Feature
from .forms import FeatureForm

from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def index(request):
	add = request.GET.get('add')
	form = FeatureForm()
	context = {'form':form, 'add':add}
	return render(request, 'loan_admin/index.html', context)

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