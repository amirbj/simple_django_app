from django.conf.urls import url
from myapp.views import Register, HomeView
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

#from registration.backends.hmac.views import RegistrationView

from myapp.views import Register, UploadImg


    #url(r'^accounts/', include('registration.backends.hmac.urls')),

urlpatterns = [

	url (r'^register/$', Register.as_view(), name = 'register'),
	url (r'^login/$' , auth_views.login, {'template_name': 'signup/www/login.html'},  name= 'auth_views'),
	url(r'^logout/$', auth_views.logout,{'template_name': 'signup/www/login.html'}, name='auth_logout'),
	url (r'^home/$', HomeView.as_view(),{'template_name': 'signup/www/home.html'}, name = 'home'),
	url (r'^home/articles/$', UploadImg.as_view(), name = 'articles'),
	#url (r'^accounts/register/$', RegistrationView.as_view(form_class=Regform), name='registration_register',),
]

