from . import models
from django.http import Http404
from django.shortcuts import render_to_response

def blogs(request):
	entries = models.Entry.objects.all()
	return render_to_response('pages/home.html', {'object_list': entries})