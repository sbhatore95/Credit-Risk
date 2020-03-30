from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'loan_admin'
urlpatterns = [
	path('', views.index, name='index'),
	path('add', views.addFeature, name='add'),
	path('index/?add=ok', views.index, name='index'),
	path('configuration', views.configuration, name='configuration'),
	path('weigh', views.addConfiguration, name='weigh'),
	path('configuration/?add=ok', views.configuration, name='configuration'),
	path('uploadCSV', views.uploadCSV, name='uploadCSV'),
	path('uploadCSV/?add=ok', views.uploadCSV, name='uploadCSV'),
	path('addApplicant', views.addApplicant, name='addApplicant'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)