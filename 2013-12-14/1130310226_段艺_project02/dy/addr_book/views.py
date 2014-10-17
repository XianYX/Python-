from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from models import People
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


def index(req):
	return render_to_response("index.html",{})

@login_required
def add(req):
	empty = []
	username = req.session.get('username','')
	if req.POST:
		post = req.POST
		for i in post.keys():
			if post[i] == '':
				empty.append(i + ' shouldn\'t be empty!')
		if len(empty) == 0:			
			new_people = People(
				student_num = post["student_num"],
				name = post["name"],
				phone = post["phone"],
				email = post["email"],
				QQ = post["QQ"],
				address = post["address"],
				birthday = post["birthday"],
				master = username,
				)
			if post["sex"] == "M":
				new_people.sex = True
			else:
				new_people.sex = False
			new_people.save()
	return render_to_response("add.html",{'empty':empty},context_instance = RequestContext(req))

@login_required
def show(req):
	username = req.session.get('username','')
	if req.POST:
		k = req.POST["k"]
		show = True
		result = People.objects.filter(master__exact=username).filter(name__contains=k)
		if len(result) == 0:
			show = False
		c = Context({'result':result,'show':show,'username':username})
		return render_to_response("search.html", c ,context_instance = RequestContext(req))
	else:
		people_lst = People.objects.filter(master__exact=username)
		c = Context({"people_lst":people_lst,'username':username})
		return render_to_response("show.html",c,context_instance = RequestContext(req))

@login_required
def delete(req):
	username = req.session.get('username','')
	Id = req.GET["id"]
	people = People.objects.filter(id__exact = Id)[0]
	if people.master != username:
		return HttpResponseRedirect('/show/')
	People.objects.get(id = Id).delete()
	people_lst = People.objects.filter(master__exact=username)
	c = Context({"people_lst":people_lst,'username':username})	
	return render_to_response("show.html",c)

@login_required
def change(req):
	username = req.session.get('username','')
	Id = req.GET["id"]
	people = People.objects.filter(id__exact = Id)[0]
	if people.master != username:
		return HttpResponseRedirect('/show/')
	empty = []
	if req.POST:
		post = req.POST
		for i in post.keys():
			if post[i] == '':
				empty.append(i + ' shouldn\'t be empty!')
		if len(empty) == 0:	
			if post["sex"] == "M":
				Sex = True
			else:
				Sex = False		
			People.objects.filter(id = Id).update(
				student_num = post["student_num"],
				name = post["name"],
				sex = Sex,
				phone = post["phone"],
				email = post["email"],
				QQ = post["QQ"],
				address = post["address"],
				birthday = post["birthday"],
				)
			people_lst = People.objects.filter(master__exact=username)
			c = Context({"people_lst":people_lst,'username':username})	
			return render_to_response("show.html",c)			
	c = Context({'empty':empty,'people':people})
	return render_to_response("change.html", c ,context_instance = RequestContext(req))

def register(req):
	if req.method == 'POST':
		form = UserCreationForm(req.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/login/')
	else:
		form = UserCreationForm()
	return render_to_response('register.html',{'form':form},context_instance = RequestContext(req))

def login(req):
	if req.method == 'POST':
		username = req.POST.get('username','')
		password = req.POST.get('password','')
		user = auth.authenticate(username = username, password = password)
		if user is not None and user.is_active:
			auth.login(req,user)
			req.session['username'] = username
			return HttpResponseRedirect('/show/')
	return render_to_response('login.html',{},context_instance = RequestContext(req))

def logout(req):
    auth.logout(req)
    return HttpResponseRedirect("/")

@login_required
def setpasswd(req):
	username = req.session.get('username','')
	user = User.objects.filter(username__exact=username)[0]
	status = ''
	empty = []
	if req.method == 'POST':
		for k in req.POST.keys():
			if req.POST[k] == '':
				empty.append(k + ' shouldn\'t be empty!')
		if len(empty) == 0:
			passwd = req.POST['passwd']
			newpasswd = req.POST['newpasswd']
			repasswd = req.POST['repasswd']
			if user.check_password(passwd) == True:
				if newpasswd == repasswd:
					user.set_password(newpasswd)
					user.save()
					auth.logout(req)
					return HttpResponseRedirect("/setsuccess/")
				else:
					status = 're_error'
			else:
				status = 'passwd_error'
	return render_to_response('setpasswd.html',{'empty':empty,'status':status},context_instance = RequestContext(req)) 

def setsuccess(req):
	return render_to_response('setsuccess.html',{})