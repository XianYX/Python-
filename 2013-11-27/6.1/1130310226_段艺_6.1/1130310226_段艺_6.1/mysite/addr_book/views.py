from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from models import People

def add(req):
	empty = []
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
				)
			if post["sex"] == "M":
				new_people.sex = True
			else:
				new_people.sex = False
			new_people.save()
	return render_to_response("add.html",{'empty':empty},context_instance = RequestContext(req))

def show(req):
	people_lst = People.objects.all()
	c = Context({"people_lst":people_lst})
	return render_to_response("show.html",c)