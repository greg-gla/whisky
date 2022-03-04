from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
class IndexView(View):
	def get(self, request, **kwargs):
		return render(request, 'pages/index.html')		