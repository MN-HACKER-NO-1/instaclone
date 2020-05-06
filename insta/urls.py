from django.urls import path, include
from .views import (
postlistview
)

app_name='insta'
urlpatterns=[
    path('',postlistview.as_view(), name='post_list'),
]