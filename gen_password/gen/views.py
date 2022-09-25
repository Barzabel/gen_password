from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
	return render(request, 'gen/home.html')

def password(request):
	res = ''
	length = int(request.GET.get('length'))
	if length > 40:
		length = 40
	alf = list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('uppercase'):
		alf.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	if request.GET.get('number'):
		alf.extend("1234567890")

	if request.GET.get('special'):
		alf.extend("$~|>=<+^%#&\\/*@}{][)(\"''.?!:;,-_")

	for x in range(length):
		res += random.choice(alf)

	return render(request, 'gen/password.html', {"password":res})

def description(request):
	return render(request, "gen/description.html")