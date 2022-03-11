from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
	def get(self, request, **kwargs):
		return render(request, 'pages/index.html')


def about(request):
	return render(request, 'pages/about.html')