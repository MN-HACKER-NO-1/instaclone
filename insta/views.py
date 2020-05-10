from django.shortcuts import render ,redirect
from .models import User
from django.utils import timezone
from .forms import *
from .forms import PostForm
from .models import post
from django.contrib.auth import authenticate, login, logout as dlogout
from django.views.generic import (
     ListView,
     CreateView,
     DetailView,
)
# Create your views here.
class postListView(ListView):
    template_name = 'insta/post_list.html'
    queryset = post.objects.all()
    context_object_name = 'posts'

class postCreateView(CreateView):
    template_name='insta/post_create.html'
    form_class=PostForm
    queryset = post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author=self.request.user
        return super().form_valid(form)
def ajaxsignup(request):
	ajax = AjaxSignUp(request.POST)
	context = {'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)
def ajaxlogin(request):
	ajax = AjaxLogin(request.POST)
	logged_in_user, output = ajax.validate()
	if logged_in_user != None:
		login(request, logged_in_user)
	context = {'ajax_output': output}
	return render(request, 'ajax.html', context)
def signup(request):
    context={}
    return render(request,'insta/sign-up.html',context)
def index(request):
    context={}
    return render(request,'insta/index.html',context)
