from django.db import models

class People(models.Model):
	"""docstring for People"""
	student_num = models.CharField(max_length = 15)
	name = models.CharField(max_length = 30)
	sex = models.BooleanField(default = True)
	phone = models.CharField(max_length = 15)
	email = models.EmailField()
	QQ = models.CharField(max_length = 11)
	address = models.CharField(max_length = 50)
	birthday = models.CharField(max_length = 8)
