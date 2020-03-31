from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db import models
from django.views.generic import FormView
from django.urls import reverse
from urllib.parse import urlencode
from .forms import MyForm, FileUploadForm
from .project import *
import sys
from .models import SavedState
import pickle
import codecs
from six.moves import cPickle
from loan_admin.models import UploadFile

def index(request):
	form = MyForm()
	context = {'form':form}
	return render(request, 'loan_officer/index.html', context)
	# x = predict_score(columns, 'loan_status', nominal, "dataset.csv")
	# print(x.Preprocess())

def result(request):
	loan_id = request.GET.get('loan_id')
	rule = request.GET.get('rule_based')
	stat = request.GET.get('statistical_based')
	ml = request.GET.get('ML_based')
	res = ""
	columns = UploadFile.objects.all().first().columns.split(',')
	del columns[0]
	nominal = UploadFile.objects.all().first().nominal_features.split(',')
	if(SavedState.objects.all().first() == None):
		m = SavedState(stat="false", ml="false")
		m.save()
	if(rule and stat and ml):
		pass
	elif(rule and stat):
		pass
	elif(rule and ml):
		pass
	elif(stat and ml):
		if(SavedState.objects.all().first().statandml == "false"):
			learn_and_save("statandml", columns, nominal, "dataset.csv")
			m = SavedState.objects.all().first()
			m.statandml = "true"
			m.save()
		f = open('media/credit_risk/dataset/test_id_dataset.csv', 'r')
		line = f.readline()
		sp = line.split(',')
		count = 0
		while(line != ""):
			if(sp[0] == loan_id):
				break
			sp = line.split(',')
			line = f.readline()
		# if(sp[0] != int(loan_id)):
		del sp[0]
		del sp[0]
		res = load_and_predict("statandml", sp)
	elif(rule):
		pass
	elif(stat):
		if(SavedState.objects.all().first().stat == "false"):
			learn_and_save("statistical", columns, nominal, "dataset.csv")
			m = SavedState.objects.all().first()
			m.stat = "true"
			m.save()
		f = open('media/credit_risk/dataset/test_id_dataset.csv', 'r')
		line = f.readline()
		fw = open('result.csv', 'w')
		while(line != ""):
			sp = line.split(',')
			del sp[0]
			del sp[0]
			fw.write(load_and_predict("statistical", sp) + '\n')
			line = f.readline()
		fw.close()
		# sp = line.split(',')
		# count = 0
		# while(line != ""):
		# 	if(sp[0] == loan_id):
		# 		break
		# 	sp = line.split(',')
		# 	line = f.readline()
		# # if(sp[0] != int(loan_id)):
		# del sp[0]
		# del sp[0]
		# res = load_and_predict("statistical", sp)
	else:
		if(SavedState.objects.all().first().ml == "false"):
			learn_and_save("ml", columns, nominal, "dataset.csv")
			m = SavedState.objects.all().first()
			m.ml = "true"
			m.save()
		f = open('media/credit_risk/dataset/test_id_dataset.csv', 'r')
		line = f.readline()
		sp = line.split(',')
		count = 0
		while(line != ""):
			if(sp[0] == loan_id):
				break
			sp = line.split(',')
			line = f.readline()
		# if(sp[0] != int(loan_id)):
		f.close()
		del sp[0]
		del sp[0]
		res = load_and_predict("ml", sp)
	# out = res.split(',')
	# context = {'approve': out[0], 'not_approve': out[1]}
	# return render(request, 'loan_officer/result.html', context)
	return render(request, 'loan_officer/result.html')

def uploadCSV(request):
	add = request.GET.get('add')
	form = FileUploadForm()
	context = {'form':form, 'add':add}
	return render(request, 'loan_officer/uploadCSV.html', context)

@require_POST
def addApplicant(request):
	form = FileUploadForm(request.POST, request.FILES)
	url = reverse('loan_officer:uploadCSV')
	if form.is_valid():
		# form.process_data(request.POST, request.FILES['file'])
		form.save()
		base_url = reverse('loan_officer:uploadCSV')
		query_string =  urlencode({'add': 'ok'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)