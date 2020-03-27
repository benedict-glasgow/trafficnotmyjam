from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from traffic.models import Posts, Comments
from traffic.forms import SearchForm, PostsForm, CommentsForm, UserForm, UserProfileForm, ChangePasswordForm
from traffic.multichoice import POST_CATEGORIES
import json
from traffic.bingCoordinates import getCoordinates
#from django import template
#register = template.Library()

def index(request):
    
    postsList = Posts.objects.order_by("-date")[:10]
    
    contextDict = {}
    contextDict["posts"] = postsList
    return render(request, 'traffic/index.html', context=contextDict)



#@register.inclusion_tag('writeComment.html')
def post(request, postSlug):
    #contextDict = {}
    
    #try:
        #post = Posts.objects.get(slug=postSlug)
    print("test")
    post = get_object_or_404(Posts, slug=postSlug)
    user = request.user
    comments = Comments.objects.filter(post=post)
        #contextDict['post'] = post
        #contextDict['commentform'] = CommentsForm()
    if comments.exists():
           # contextDict['comments'] = comments
        comments = comments
    else:
            #contextDict['comments'] = None
        comments = None
            
      
        
        #contextDict['currentComment'] = None
    currentComment = None
        
    if request.method == 'POST':
            #contextDict['commentform']  = CommentsForm(data=request.POST)
        commentForm = CommentsForm(data=request.POST)
        if commentForm.is_valid():
            currentComment = commentForm.save(commit=False)
            currentComment.post = post
            currentComment.user = user
            currentComment.save()
    else:
            #contextDict['commentform'] = CommentsForm()
        commentForm = CommentsForm()
            
    #except Posts.DoesNotExist:
        #contextDict['post'] = None
       # post = None
        #contextDict['comments'] = None
        #comments = None
    #except: Comments.DoesNotExist
    
    
    return render(request, 'traffic/post.html',  {'post': post,
                   'comments': comments,
                   'currentComment': currentComment,
                   'commentForm': commentForm}) #postTesting.html removed / context=contextDict


def information(request):
    contextDict = {}
    return render(request, 'traffic/info.html', context=contextDict)


def about(request):
    return redirect('/about/information/')


def rules(request):
    contextDict = {}
    return render(request, 'traffic/rule.html', context=contextDict)


def FAQ(request):
    contextDict = {}
    return render(request, 'traffic/faq.html', context=contextDict)


def categories(request):
    contextDict = {}

    categories = []

    for category in POST_CATEGORIES:
        categories += [ {'slug':category[0], 'name':category[1] } ]
    
    contextDict['categories'] = categories

    return render(request, 'traffic/categoriesTesting.html', context=contextDict)


def category(request, categorySlug):
    contextDict = {}

    posts = Posts.objects.filter(category=categorySlug)

    if posts.exists():
        contextDict['posts'] = posts
    else:
        contextDict['posts'] = None

    return render(request, 'traffic/categoryTesting.html', context=contextDict)


def search(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            return redirect(form.cleaned_data['search'] + '/')

        else:
            print(form.errors)

    print(form)
    return render(request, 'traffic/search.html', {'form':form} )


def searchResult(request, searchQuery):
    contextDict = {}

    contextDict['query'] = searchQuery

    posts = Posts.objects.filter(title__icontains=searchQuery)
    comments = Comments.objects.filter(content__icontains=searchQuery)

    if posts.exists():
        contextDict['posts'] = posts
    else:
        contextDict['posts'] = None

    if comments.exists():
        contextDict['comments'] = comments
    else:
        contextDict['comments'] = None

    #return render(request, 'traffic/searchResultTesting.html', contextDict) Not sure which html page to lead to?
    return render(request, 'traffic/results.html', contextDict) 


@login_required
def addPost(request):
    form = PostsForm()
    
    if request.method =='POST':
        form = PostsForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            location = getCoordinates(post.location)
            post.location = location

            post.save()
            return redirect('/')
        else:
            print(form.errors)
            
    return render(request, 'traffic/writePosts.html', {'form': form})

def addComments(request):#,pk
    #post= get_object_or_404(Posts, pk=pk)
    form = CommentsForm()
    
    if request.method =='POST':
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            #form.post = post
            #post= get_object_or_404(Posts, pk=pk)
            #form.post = post
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
            
    return render(request, 'traffic/post.html', {'form': form})

def register(request):
    contextDict = {}

    registered = False

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        userProfileForm = UserProfileForm(request.POST)

        if userForm.is_valid() and userProfileForm.is_valid():

            user = userForm.save()
            user.set_password(user.password)
            user.save()

            ## The UserProfile models are set up for future expansion

            profile = userProfileForm.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(userForm.errors, userProfileForm.errors)

    else:
        userForm = UserForm()
        userProfileForm = UserProfileForm()

    contextDict['userForm'] = userForm
    contextDict['userProfileForm'] = userProfileForm
    contextDict['registered'] = registered

    return render(request, 'traffic/register.html', context=contextDict)


def userLogin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('traffic:index'))

            else:
                HttpResponse("This account is disabled!")

        
        else:
            print(f'Invalid login details {username} {password} ')
            return HttpResponse("Invalid log in details!")

    else:
        return render(request, 'traffic/login.html')


@login_required
def userLogout(request):
    logout(request)
    return redirect(reverse('traffic:index'))
   

@login_required
def account(request):
    user = request.user

    contextDict = { 'posts': None, 'comments': None}

    posts = Posts.objects.order_by('-date').filter(user=user)
    if posts.exists():
        contextDict['posts'] = posts

    comments = Comments.objects.order_by('-date').filter(user=user)
    if comments.exists():
        contextDict['comments'] = comments

    contextDict['updateDetailsForm'] = ChangePasswordForm()

    return render(request, 'traffic/account.html', context=contextDict)



@login_required
def changePassword(request):
    if request.method == 'POST':

        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        repeatNewPassword = request.POST.get('repeatNewPassword')

        correctPassword = check_password(oldPassword, request.user.password)

        if correctPassword:
            if newPassword == repeatNewPassword:
                request.user.set_password(newPassword)
                request.user.save()
                return redirect(reverse('traffic:account'))

            else:
                return HttpResponse('Invalid details')
            
        else:
            return HttpResponse('Invalid details')

    else:
        redirect(reverse('traffic:account'))

















