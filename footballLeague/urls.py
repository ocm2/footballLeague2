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

	url(r'^representative/(?P<idaux>\d+)/$', representativeModel),
	url(r'^player/(?P<idaux>\d+)/$', playerModel),
	url(r'^stadium/(?P<idaux>\d+)/$', stadiumModel),
    url(r'^coach/(?P<idaux>\d+)/$', coachModel),
	url(r'^team/(?P<idaux>\d+)/$', teamModel),
	url(r'^league/(?P<idaux>\d+)/$', leagueModel),
	url(r'^referee/(?P<idaux>\d+)/$', refereeModel),	
	url(r'^match/(?P<idaux>\d+)/$', matchModel),


#	url(r'representative/representative_create/$' ,RepresentativeCreate.as_view(), name = 'RepresentativeCreate'),
#	url(r'player/player_create/$'   ,PlayersCreate.as_view(), name = 'PlayersCreate'),
	url(r'stadium/stadium_create/$' ,Create.as_view(model = Stadium, form_class = StadiumForm), name = 'StadiumCreate'),
#	url(r'coach/coach_create/$' ,CoachCreate.as_view(), name = 'CoachCreate'),
#	url(r'team/team_create/$' ,TeamCreate.as_view(), name = 'TeamCreate'),
#	url(r'league/league_create/$' ,LeagueCreate.as_view(), name = 'LeagueCreate'),
#	url(r'referee/referee_create/$' ,RefereeCreate.as_view(), name = 'RefereeCreate'),
#	url(r'match/match_create/$' ,MatchCreate.as_view(), name = 'MatchCreate'),


	url(r'stadium/(?P<pk>\d+)/stadium_edit$' ,Edit.as_view(model = Stadium, form_class = StadiumForm)),

	url(r'stadium/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/stadiumsList/',model = Stadium),  name = 'Delete'),





	#url(r'^user/(\w+)/$', userpage),
	url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'prova.views.home', name='home'),
    # url(r'^prova/', include('prova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
