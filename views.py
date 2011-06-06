# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse

import datetime

def home(request):	
	return TemplateResponse(request, 'home.html', {'entries': ''})