from django.http import HttpResponse, HttpResponseRedirect
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
	songs = Song.objects.filter(user=request.user)
	for song in (songs):
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
				ref = Ref(name=request.POST.get("ref_name"+str(i)),link=(request.POST.get("ref_url"+str(i))).replace("watch?v=","embed/"),comment=request.POST.get("ref_comment"+str(i)),category=request.POST.get("ref_category"+str(i)),song=song)
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
	songs = Song.objects.filter(id=songid)
	if(songs):
		if(songs[0].user.id == request.user.id):
			refs = Ref.objects.filter(song=songs[0])
			html = t.render(RequestContext(request,{'unallowed':'','song':songs[0],'refs':refs}))
		else:
			html = t.render(Context({'unallowed':'You dont own this song. How did you get here?'}))
	else:
		html = t.render(Context({'unallowed':'No such song. How did you get here?'}))
	return HttpResponse(html)

@login_required
def edit(request,songid):
	if(request.method == "POST"):
		t = get_template('edit_done.html')
		songs = Song.objects.filter(id=songid)
		if(songs):
			if(songs[0].user.id == request.user.id):
				#Business logic here
				songs[0].name = request.POST.get("name","")
				songs[0].movie = request.POST.get("movie", "")
				songs[0].artist = request.POST.get("artist", "")
				songs[0].scale = request.POST.get("scale", "")
				songs[0].notes = request.FILES['notes']
				songs[0].tempo = request.POST.get("tempo", "0")
				songs[0].save()
				form_count = int(request.POST.get("count", 0))
				refs = Ref.objects.filter(song=songs[0])
				if(form_count > len(refs)):
					update = len(refs)
					add = form_count - len(refs)
					delete = 0
				if(form_count < len(refs)):
					update = len(refs)
					add = 0
					delete = len(refs) - form_count
				if(form_count == len(refs)):
					update = len(refs)
					add = 0
					delete = 0
				for i in range(1,update+1):
					refs[i-1].name = request.POST.get("ref_name"+str(i))
					refs[i-1].link = (request.POST.get("ref_url"+str(i))).replace("watch?v=","embed/")
					refs[i-1].comment = request.POST.get("ref_comment"+str(i),"")
					refs[i-1].category = request.POST.get("ref_category"+str(i),0)
					refs[i-1].save()
				for i in range(update+1,update+add+1):
					ref = Ref(name=request.POST.get("ref_name"+str(i)),link=(request.POST.get("ref_url"+str(i))).replace("watch?v=","embed/"),comment=request.POST.get("ref_comment"+str(i)),category=request.POST.get("ref_category"+str(i)),song=songs[0])
					ref.save()
				for i in range(update+1,update+delete+1):
					refs[i].delete()
				#Business logic ends
				html = t.render(RequestContext(request,{'unallowed':'Song edited successfully!'}))
			else:
				html = t.render(RequestContext(request,{'unallowed':'You dont own this song. How did you get here?'}))
		else:
			html = t.render(RequestContext(request,{'unallowed':'No such song. How did you get here?'}))
		return HttpResponse(html)
	else:
		t = get_template('edit.html')
		songs = Song.objects.filter(id=songid)
		if(songs):
			refs = Ref.objects.filter(song=songs[0])
			if(songs[0].user.id == request.user.id):
				html = t.render(RequestContext(request,{'unallowed':'','song':songs[0],'refs':refs}))
			else:
				html = t.render(RequestContext(request,{'unallowed':'You dont own this song. How did you get here?'}))
		else:
			html = t.render(RequestContext(request,{'unallowed':'No such song. How did you get here?'}))
		return HttpResponse(html)

@login_required
def delete(request,songid):
	if(request.method == "POST"):
		confirm = int(request.POST.get("confirm", 0))
		if(not confirm):
			return HttpResponseRedirect("/home/")
		t = get_template('delete_done.html')
		songs = Song.objects.filter(id=songid)
		if(songs):
			if(songs[0].user.id == request.user.id):
				#Business logic here
				refs = Ref.objects.filter(song=songs[0])
				for i in range(0,len(refs)):
					refs[i].delete()
				songs[0].delete()
				#Business logic ends
				html = t.render(RequestContext(request,{'unallowed':'Song deleted successfully.'}))
			else:
				html = t.render(RequestContext(request,{'unallowed':'You dont own this song. How did you get here?'}))
		else:
			html = t.render(RequestContext(request,{'unallowed':'No such song. How did you get here?'}))
		return HttpResponse(html)
	else:
		t = get_template('delete.html')
		songs = Song.objects.filter(id=songid)
		if(songs):
			if(songs[0].user.id == request.user.id):
				html = t.render(RequestContext(request,{'unallowed':'','song':songs[0]}))
			else:
				html = t.render(RequestContext(request,{'unallowed':'You dont own this song. How did you get here?'}))
		else:
			html = t.render(RequestContext(request,{'unallowed':'No such song. How did you get here?'}))
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
