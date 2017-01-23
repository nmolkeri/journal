from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic import direct_to_template
from django.conf.urls import url

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'movies.views.index'),
    url(r'^$', 'members.views.LoginRequest'),
    (r'^addmovie/$', 'movies.views.MovieCreate'),
    (r'^addmusic/$', 'music.views.AlbumCreate'),
    (r'^addmusician/$', 'music.views.MusicianCreate'), 
   (r'^addplace/$', 'places.views.PlaceCreate'),
    (r'^addbook/$', 'books.views.BookCreate'),
    (r'^addcategory/$', 'movies.views.CategoryCreate'),
    (r'^editmovies/$', 'movies.views.post_update'),
    (r'^profile/$', 'members.views.Profile'),
    (r'^music/', 'music.views.AlbumAll'),
    (r'^movies/', 'movies.views.MoviesAll'),
    (r'^places/', 'places.views.PlaceAll'),
    (r'^books/', 'books.views.BookAll'),
    (r'^movies/(?P<moviename>.*)/$', 'movies.views.SpecificMovie'),
    (r'^register/$', 'members.views.MembersReg'),
    (r'^login/$', 'members.views.LoginRequest'),
    (r'^logout/$', 'members.views.LogoutRequest'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name':'password_reset_confirm.html'}),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name':'password_reset_complete.html'}),
url(r'^resetpassword/passwordsent/$',
               'django.contrib.auth.views.password_reset_done',
                {'template_name':'password_reset_done.html'},
                name='password_reset_done'),

   (r'^resetpassword/$','django.contrib.auth.views.password_reset',{'template_name':'password_reset_form.html'}),
)
