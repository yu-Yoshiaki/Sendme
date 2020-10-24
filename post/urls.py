from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    #path('',views.indexListView.as_view(),name='index'),
    path('',views.index.as_view(),name='index'),
]
