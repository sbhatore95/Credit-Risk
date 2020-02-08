from django.urls import path
from . import views

app_name = 'loan_admin'
urlpatterns = [
	path('', views.index, name='index'),
	path('add', views.addFeature, name='add'),
	path('index/?add=ok', views.index, name='index'),
]