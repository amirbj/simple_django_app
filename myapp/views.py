from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.utils import timezone
from myapp.models import *






from django.contrib.sites.shortcuts import get_current_site

#from registration import signals
from myapp.models import Regform, RegUniqueEmail
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from myapp.forms import ArticleForm, CommentForm
from django.core.urlresolvers import reverse_lazy

class Register(View):
	form_class = Regform
	template_name = 'signup/www/index.html'
	#unique_email = RegUniqueEmail()

	def get(self, request, *args, **kwargs):
		formal = self.form_class
		return render(request, self.template_name, {'form': formal})

	def post(self, request, *args, **kwargs):
		formal = self.form_class(request.POST)
		#aa= RegUniqueEmail(formal)
		if formal.is_valid():
			#if formal.clean():
				#if aa.clean_email():
			formal.save()
			return HttpResponse("<h1>'registered seuccefully'</h1>")

		
		return render(request, self.template_name,{'form': formal})



class HomeView(TemplateView):
    template_name = 'signup/www/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
	
def default(request):
	return render (request, 'signup/www/home.html')


class UploadImg(CreateView):
	template_name = 'signup/www/uploadimg.html'
	form_class = ArticleForm
	success_url = '/thanks/'

	def form_valid(self, form):
		form.instance.createdby = self.request.user
		return super(UploadImg , self).form_valid(form)


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)	
			
		return  super(UploadImg, self).post(form)
		
		




	






def post(self, request, *args, **kwargs):
	form = self.form_class(request.POST, request.FILES)
	if form.is_valid():
		form.save()

		return redirect(self.success_url)

	else:
		return render(request, self.template_name, {'form': form})
			










