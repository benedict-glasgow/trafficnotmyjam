from django.urls import path
from traffic import views

app_name = 'traffic'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:postSlug>/', views.post, name='post'),
    path('about/information/', views.information, name='information'),
    path('about/', views.about, name='about'),
    path('about/faq/', views.FAQ, name='faq'),
    path('about/rules/', views.rules, name='rules'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:categorySlug>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('search/<searchQuery>/', views.searchResult, name='searchResult'),
    path('addposts/',views.addPost, name ='addposts'),
    path('addcomments/',views.addComments, name ='addComments'),
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('account/', views.account, name='account'),
    path('account/changepassword/', views.changePassword, name='changePassword'),
    path('traffic/greenreaction/', views.ReactionsViewGreen.as_view(),name ='green'),
    path('traffic/yellowreaction/', views.ReactionsViewYellow.as_view(),name ='yellow'),
    path('traffic/redreaction/', views.ReactionsViewRed.as_view(),name ='red'),
    path('traffic/stopreaction/', views.ReactionsViewStop.as_view(),name ='stop')
    
    #path('<slug:pk>/', indexView.as_view() ,name = 'index'),

]
