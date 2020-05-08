from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import post
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
