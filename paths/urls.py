from django.conf.urls import url
from . import views

app_name = 'paths'

urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),
    url(r'^getTrajectories$', views.getTrajectories, name='getTrajectories'),
    url(r'^nextSteps$', views.nextSteps, name='nextSteps'),
    url(r'^sortBySimilarity$', views.sortBySimilarity, name='sortBySimilarity'),
    url(r'^autocomplete_job/$', views.autocomplete_job, name='autocomplete_job'),

]
