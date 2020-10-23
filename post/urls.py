from django.urls import path
from . import views


urlpatterns = [
    path('',views.indexListView.as_view(),name='index'),
]
