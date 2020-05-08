from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings
from .views import (
    postListView,
    postCreateView,
)

app_name='insta'
urlpatterns=[
    path('',postListView.as_view(), name='post_list'),
    path('new/',postCreateView.as_view(), name='post_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)