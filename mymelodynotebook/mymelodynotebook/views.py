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
	if(request.method == "POST"):
		name = request.POST.get("name","")
		movie = request.POST.get("movie", "")
		artist = request.POST.get("artist", "")
		scale = request.POST.get("scale", "")
		notes = request.FILES['notes']
		#notes = request.POST.get('notes')
		tempo = request.POST.get("tempo", "0")
		form_count = request.POST.get("count", 0)
		song = Song(name=name,movie=movie,artist=artist,scale=scale,tempo=tempo,notation="",notes=notes,user=request.user)
		song.save()
		if(form_count > 0):
			for i in range(1,int(form_count)+1):
				ref = Ref(name=request.POST.get("ref_name"+str(i)),link=request.POST.get("ref_url"+str(i)),comment=request.POST.get("ref_comment"+str(i)),category=request.POST.get("ref_category"+str(i)),song=song)
				ref.save()
		t = get_template('add_done.html')
		html = t.render(RequestContext(request,{}))
		return HttpResponse(html)
	else:
		t = get_template('add.html')
		html = t.render(RequestContext(request,{}))
		return HttpResponse(html)

@login_required
def view(request,songid):
	t = get_template('view.html')
	result = Song.objects.filter(id=songid)
	if(result):
		if(result[0].user.id == request.user.id):
			html = t.render(RequestContext(request,{'allowed':1}))
			return HttpResponse(html)
	html = t.render(Context({'allowed':0}))
	return HttpResponse(html)

@login_required
def edit(request,songid):
	t = get_template('edit.html')
	result = Song.objects.filter(id=songid)
	if(result):
		if(result[0].user.id == request.user.id):
			html = t.render(RequestContext(request,{'allowed':1}))
			return HttpResponse(html)
	html = t.render(Context({'allowed':0}))
	return HttpResponse(html)

@login_required
def delete(request,songid):
	t = get_template('delete.html')
	result = Song.objects.filter(id=songid)
	if(result):
		if(result[0].user.id == request.user.id):
			html = t.render(RequestContext(request,{'allowed':1}))
			return HttpResponse(html)
	html = t.render(Context({'allowed':0}))
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
