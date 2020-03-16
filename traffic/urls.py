from django.urls import path
from traffic import views

app_name = 'traffic'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:postSlug>/', views.post, name='post'),
    path('about/information/', views.information, name='information'),
    path('about/', views.about),
    path('about/FAQ', views.FAQ, name='FAQ'),
    path('about/rules', views.rules, name='rules'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:categorySlug>/', views.category, name='category'),
]
