from django.urls import path
from traffic import views

app_name = 'traffic'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:postSlug>/', views.post, name='post'),
   ## path('post/<slug:postSlug>/addcomment/', views.post, name='addComments'),
    path('about/information/', views.information, name='information'),
    path('about/', views.about),
    path('about/faq/', views.FAQ, name='FAQ'),
    path('about/rules/', views.rules, name='rules'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:categorySlug>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('search/<searchQuery>/', views.searchResult, name='searchResult'),
    path('addposts/',views.addPosts, name ='addposts'),
    path('addcomments/',views.addComments, name ='addComments'),
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),

]
