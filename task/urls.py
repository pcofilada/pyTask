from django.conf.urls import patterns, url
from task import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^$', login_required(views.IndexView.as_view())),
	)