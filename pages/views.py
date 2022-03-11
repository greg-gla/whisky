from django.shortcuts import render
from django.views.generic import View, ListView
from django.shortcuts import get_object_or_404
from pages.models import Whisky, Rating, Distillery

# Create your views here.
class IndexView(View):
	def get(self, request, **kwargs):
		context = {}
		context['distilleries'] = Distillery.objects.all()

		return render(request, 'pages/index.html', context)		

class ReviewView(View):
	def get(self, request, **kwargs):
		context = {}
		instance = get_object_or_404(Whisky, pk=kwargs.get('pk'))

		context['whisky'] = instance
		context['ratings'] = Rating.objects.filter(whisky_id=instance.pk)

		return render(request, 'pages/review.html', context)

class WhiskyList(ListView):
	template_name = 'templates/whisky_list.html'
	paginate_by = 10

	def get_queryset(self, *args, **kwargs):
		instance = 	get_object_or_404(Distillery, pk=self.kwargs.get('pk'))

		return Whisky.objects.filter(distillery=instance.pk)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		instance = get_object_or_404(Distillery, pk=self.kwargs.get('pk'))

		context['distillery'] = instance

		return context		
