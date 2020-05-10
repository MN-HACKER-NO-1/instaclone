from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings
from . import views
from .views import (
    postListView,
    postCreateView,
)

app_name='insta'
from django.conf.urls import url
urlpatterns=[
    path('',postListView.as_view(), name='post_list'),
    path('new/',postCreateView.as_view(), name='post_create'),
    path('login/',views.index),
    path('signup/',views.signup),
    path('ajax-sign-up/', views.ajaxsignup),
    path('ajax-login/', views.ajaxlogin),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)