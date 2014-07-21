from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
	t = get_template('index.html')
	html = t.render(RequestContext(request,{'message':'Welcome to MyMelodyNotebook'}))
	return HttpResponse(html)

def register(request):
	id = request.POST['username']
	passw = request.POST['password']
	mailid = request.POST['mailid']
	user = User.objects.create_user(id, mailid, passw)
	t = get_template('login.html')
	html = t.render(Context({'id':id ,'pass':passw}))
	return HttpResponse(html)

@login_required
def home(request):
	t = get_template('home.html')
	html = t.render(Context({'message':'Home page'}))
	return HttpResponse(html)

def log_out(request):
	logout(request)
	t = get_template('logout.html')
	html = t.render(Context({'message':'logout page'}))
	return HttpResponse(html)
