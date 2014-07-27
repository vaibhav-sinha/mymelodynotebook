from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from models import Song,Ref

def index(request):
	t = get_template('index.html')
	html = t.render(RequestContext(request,{}))
	return HttpResponse(html)

@login_required
def home(request):
	t = get_template('home.html')
	songlist = []
	result = Song.objects.all()
	for song in (result):
		songlist.append({'name':song.name,'id':song.id})
	html = t.render(RequestContext(request,{'songlist':songlist}))
	return HttpResponse(html)

@login_required
def add(request):
	t = get_template('add.html')
	html = t.render(RequestContext(request,{'songlist':songlist}))
	return HttpResponse(html)

@login_required
def view(request,songid):
	t = get_template('view.html')
	html = t.render(RequestContext(request,{'songid':songid}))
	return HttpResponse(html)

@login_required
def edit(request,songid):
	t = get_template('edit.html')
	html = t.render(RequestContext(request,{'songid':songid}))
	return HttpResponse(html)

@login_required
def delete(request,songid):
	t = get_template('delete.html')
	html = t.render(RequestContext(request,{'songid':songid}))
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
