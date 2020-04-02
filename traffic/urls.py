from django.urls import path
from traffic import views

app_name = 'traffic'

urlpatterns = [
    path('', views.indexMain, name='index'),
    path('p/<slug:page>/', views.index, name='pagesIndex'),
    path('post/<slug:postSlug>/', views.post, name='post'),
    path('about/information/', views.information, name='information'),
    path('about/', views.about, name='about'),
    path('about/faq/', views.FAQ, name='faq'),
    path('about/rules/', views.rules, name='rules'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:categorySlug>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('search/<searchQuery>/', views.searchResult, name='searchResult'),
    path('addpost/',views.addPost, name ='addposts'),
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('account/', views.account, name='account'),
    path('traffic/greenreaction/', views.ReactionsViewGreen.as_view(),name ='green'),
    path('traffic/yellowreaction/', views.ReactionsViewYellow.as_view(),name ='yellow'),
    path('traffic/redreaction/', views.ReactionsViewRed.as_view(),name ='red'),
    path('traffic/stopreaction/', views.ReactionsViewStop.as_view(),name ='stop'),
    path('traffic/map/', views.LoadMapView.as_view(), name='loadMap'),

]
