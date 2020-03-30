from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db import models
from django.views.generic import FormView
from django.urls import reverse
from urllib.parse import urlencode
from .forms import MyForm, FeatureForm
from .project import *
import sys
from .models import SavedState
import pickle
import codecs
from six.moves import cPickle
# Create your views here.
columns = ['loan_status','funded_amnt','term','int_rate','installment','sub_grade','emp_length',
'home_ownership','annual_inc','verification_status','pymnt_plan','purpose',
'dti','delinq_2yrs','inq_last_6mths','open_acc','pub_rec','revol_bal','revol_util','total_acc',
'initial_list_status','collections_12_mths_ex_med','acc_now_delinq','tot_coll_amt','acc_open_past_24mths',
'avg_cur_bal','bc_open_to_buy','chargeoff_within_12_mths','delinq_amnt','mo_sin_old_il_acct',
'mo_sin_old_rev_tl_op','mo_sin_rcnt_rev_tl_op','mo_sin_rcnt_tl','mort_acc','mths_since_recent_bc',
'mths_since_recent_inq','num_accts_ever_120_pd',
'num_actv_bc_tl','num_bc_tl','num_il_tl','num_tl_90g_dpd_24m','num_tl_op_past_12m','pct_tl_nvr_dlq',
'percent_bc_gt_75','pub_rec_bankruptcies','tax_liens','total_il_high_credit_limit']
nominal = ['term','sub_grade','emp_length','home_ownership','verification_status',
'pymnt_plan','purpose','initial_list_status']
arr = ['30000','_36_months','22.35','1151.16','D5','5_years','MORTGAGE','100000',
'Source_Verified','n','debt_consolidation','30.46','0','0','11','1','15603','37','19','w','0','0',
'0','4','42939','15181','0','0','83','73','23','2','1','23','8','0','3','5','10','0','2','89.5',
'33.3','1','0','101984']

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
		f = open('id_dataset.csv', 'r')
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
		f = open('id_dataset.csv', 'r')
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
		res = load_and_predict("statistical", sp)
	else:
		if(SavedState.objects.all().first().ml == "false"):
			learn_and_save("ml", columns, nominal, "dataset.csv")
			m = SavedState.objects.all().first()
			m.ml = "true"
			m.save()
		f = open('id_dataset.csv', 'r')
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
		res = load_and_predict("ml", sp)
	out = res.split(',')
	context = {'approve': out[0], 'not_approve': out[1]}
	return render(request, 'loan_officer/result.html', context)

def uploadCSV(request):
	add = request.GET.get('add')
	form = FeatureForm()
	context = {'form':form, 'add':add}
	return render(request, 'loan_officer/uploadCSV.html', context)

@require_POST
def addApplicant(request):
	form = FeatureForm(request.POST, request.FILES)
	url = reverse('loan_officer:uploadCSV')
	if form.is_valid():
		form.process_data(request.FILES['file'])
		base_url = reverse('loan_officer:uploadCSV')
		query_string =  urlencode({'add': 'ok'})
		url = '{}?{}'.format(base_url, query_string)
	return redirect(url)