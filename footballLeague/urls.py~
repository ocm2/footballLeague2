from django.conf.urls import patterns, include, url
from prac2.views import *
from prac2.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', mainpage, name='home'),
	url(r'^representativesList/$', representativesList, name='List of Representative'),
	url(r'^playersList/$', playersList, name='List of Players'),
	url(r'^stadiumsList/$', stadiumsList, name='List of Stadiums'),
	url(r'^coachsList/$', coachsList, name='List of Coachs'),
	url(r'^teamsList/$', teamsList, name='List of Teams'),
	url(r'^leaguesList/$', leaguesList, name='List of Leagues'),
	url(r'^refereesList/$', refereesList, name='List of Referees'),
	url(r'^matchesList/$', matchesList, name='List of Matches'),

	url(r'^stadium/(?P<idaux>\d+)/$', stadiumModel),
	url(r'^match/(?P<idaux>\d+)/$', matchModel),
	url(r'^referee/(?P<idaux>\d+)/$', refereeModel),
	url(r'^team/(?P<idaux>\d+)/$', teamModel),
	url(r'^representative/(?P<idaux>\d+)/$', representativeModel),
	url(r'^player/(?P<idaux>\d+)/$', playerModel),
	url(r'^league/(?P<idaux>\d+)/$', leagueModel),	
    url(r'^coach/(?P<idaux>\d+)/$', coachModel),

	url(r'mystadiums/stadium_create/$' ,StadiumCreate.as_view(), name = 'StadiumCreate'),
	url(r'mystadiums/stadium_edit/(?P<pk>[\W\S]+)/$' ,StadiumEdit.as_view()),
#	url(r'mystadiums/stadium_edit/$' ,UpdateView.as_view(), name='stadium_create'),

	#url(r'^user/(\w+)/$', userpage),
	url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'prova.views.home', name='home'),
    # url(r'^prova/', include('prova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
