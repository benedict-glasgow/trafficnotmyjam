from django.urls import path
from traffic import views

app_name = 'traffic'

urlpatterns = [
    path('',views.index,name='index')
]
