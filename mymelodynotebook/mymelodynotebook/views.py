from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
	t = get_template('index.html')
	html = t.render(RequestContext(request,{}))
	#html = t.render(RequestContext(request,{'message':'Welcome to MyMelodyNotebook'}))
	return HttpResponse(html)

def password_change_done(request):
	t = get_template('registration/password_change_done.html')
	html = t.render(RequestContext(request,{}))
	return HttpResponse(html)

def password_reset_done(request):
	t = get_template('registration/password_reset_done.html')
	html = t.render(RequestContext(request,{}))
	return HttpResponse(html)

def password_reset_complete(request):
	t = get_template('registration/password_reset_complete.html')
	html = t.render(RequestContext(request,{}))
	return HttpResponse(html)
