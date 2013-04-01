from django.shortcuts import  get_object_or_404, render, HttpResponseRedirect, redirect
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import time
from django.core.urlresolvers import reverse

	
@login_required
def vista_inicio(request):	
	user = request.user	
	return render(request, 'sitio/inicio.html')
	

def ayuda(request):
	return render(request, 'sitio/documentacion/ayuda.html')