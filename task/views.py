from django.shortcuts import render
from django.views import generic
from task.models import Task

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'task/index.html'
	context_object_name = 'latest_task_list'

	def get_queryset(self):
		return Task.objects.all()