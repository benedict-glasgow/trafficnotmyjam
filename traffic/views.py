from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password, ValidationError
from traffic.models import Posts, Comments
from traffic.forms import SearchForm, PostsForm, CommentsForm, UserForm, UserProfileForm, ChangePasswordForm
from traffic.multichoice import POST_CATEGORIES
import json
from traffic.bingCoordinates import getCoordinates
from django.views.generic import View
from django.core import serializers
from math import ceil
#from django import template
#register = template.Library()

def indexMain(request):
    ## If the front page is requested, it is the same as the first page
    return index(request, '1')

def index(request, page):
    contextDict = {}

    ## If the page number is invalid, raise a 404 error
    try:
        page = int(page)
    except:
        raise Http404('Invalid page number')
    
    n = 5*page
    postsList = Posts.objects.order_by("-date")[(n-5):n]
    
    if not postsList.exists():
        raise Http404('Invalid page number')

    numberOfPages = ceil(Posts.objects.count() / 5)

    contextDict["posts"] = postsList
    contextDict['numberOfPages'] = range(1, numberOfPages + 1)
    contextDict['pageNumber'] = page
    return render(request, 'traffic/index.html', context=contextDict)

def post(request, postSlug):
   
    post = get_object_or_404(Posts, slug=postSlug)
    user = request.user
    comments = Comments.objects.filter(post=post)
     
    if comments.exists():
        comments = comments
    else:
        comments = None
            
      
    currentComment = None
        
    if request.method == 'POST':
        commentForm = CommentsForm(data=request.POST)
        if commentForm.is_valid():
            currentComment = commentForm.save(commit=False)
            currentComment.post = post
            currentComment.user = user
            currentComment.save()
    else:
            
        commentForm = CommentsForm()
            
    
    return render(request, 'traffic/post.html',  {'post': post,
                   'comments': comments,
                   'currentComment': currentComment,
                   'commentForm': commentForm}) 


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
        categories += [ {'slug':category[0], 'name':category[1],
        'count': Posts.objects.filter(category=category[0]).count() } ]
    
    contextDict['categories'] = categories

    return render(request, 'traffic/categories.html', context=contextDict)


def category(request, categorySlug):
    contextDict = { 'posts':None, }

    posts = Posts.objects.filter(category=categorySlug)

    if posts.exists():
        contextDict['posts'] = posts

    contextDict['categoryName'] = dict(POST_CATEGORIES)[categorySlug]

    return render(request, 'traffic/category.html', context=contextDict)


def search(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            return redirect(form.cleaned_data['search'] + '/')

        else:
            print(form.errors)

    return render(request, 'traffic/search.html', {'form':form} )


def searchResult(request, searchQuery):
    contextDict = {}

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            return redirect(form.cleaned_data['search'] + '/')

        else:
            print(form.errors)

    contextDict['form'] = SearchForm(initial={'search':searchQuery})
    contextDict['query'] = searchQuery

    posts = Posts.objects.filter(title__icontains=searchQuery)
    comments = Comments.objects.filter(content__icontains=searchQuery)

    if posts.exists():
        contextDict['posts'] = posts

    if comments.exists():
        contextDict['comments'] = comments

    return render(request, 'traffic/results.html', contextDict) 


@login_required
def addPost(request):
    form = PostsForm()
    
    if request.method =='POST':
        form = PostsForm(request.POST,request.FILES)
        
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

def addComments(request):
    form = CommentsForm()
    
    if request.method =='POST':
        form = CommentsForm(request.POST)
        
        if form.is_valid():
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

            user = userForm.save(commit=False)
            
            try:
                ## Check if the password follows the validation rules
                validate_password(user.password)
                user.set_password(user.password)
                user.save()

                ## The UserProfile models are set up for future expansion

                profile = userProfileForm.save(commit=False)
                profile.user = user
                profile.save()

                registered = True

            except ValidationError as exc:
                ## If the password does not follow the validation rules add the error message
                ## to the form and try again
                userForm.add_error("password", exc)

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
    contextDict = {}

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('traffic:index'))

            else:
                contextDict['loginFail'] = True
                contextDict['loginMessage'] = "Account disabled"
                return render(request, 'traffic/login.html', contextDict)

        
        else:
            contextDict['loginFail'] = True
            contextDict['loginMessage'] = "Invalid log in details provided."
            return render(request, 'traffic/login.html', contextDict)

    else:
        contextDict['loginFail'] = False
        return render(request, 'traffic/login.html', contextDict)


@login_required
def userLogout(request):
    logout(request)
    return redirect(reverse('traffic:index'))
   

def changePasswordH(request):
    ## Helping function for changing the password
    passForm = ChangePasswordForm(request.POST)

    oldPassword = request.POST.get('oldPassword')
    newPassword = request.POST.get('newPassword')
    repeatNewPassword = request.POST.get('repeatNewPassword')

    correctPassword = check_password(oldPassword, request.user.password)
    
    if correctPassword:
        if newPassword == repeatNewPassword:
            try:
                validate_password(newPassword)
                request.user.set_password(newPassword)
                request.user.save()
                passForm.add_error('repeatNewPassword', "Password changed successfully!")
            except ValidationError as exc:
                passForm.add_error('repeatNewPassword', exc)

        else:
            passForm.add_error('repeatNewPassword', "The two passwords don't match")
        
    else:
        passForm.add_error('oldPassword', "Wrong password")

    return passForm


@login_required
def account(request):
    user = request.user

    contextDict = { 'posts': None, 'comments': None, }

    posts = Posts.objects.order_by('-date').filter(user=user)
    if posts.exists():
        contextDict['posts'] = posts

    comments = Comments.objects.order_by('-date').filter(user=user)
    if comments.exists():
        contextDict['comments'] = comments
    
    ## If the request is for changing the password, call the 
    ## changePasswordH function
    if request.method == 'POST':
        passForm = changePasswordH(request)
    else:
        passForm = ChangePasswordForm()

    contextDict['updateDetailsForm'] = passForm

    return render(request, 'traffic/account.html', context=contextDict)

        
    
class ReactionsViewGreen(View):
    def get(self, request):
        postId = request.GET['postId']
        try:
            post = Posts.objects.get(id=int(postId))
        except Posts.DoesNotExist:
            return HttpResponse(-1)
        except ValueError: 
            return HttpResponse(-1)
        
        post. greenCount =  post. greenCount + 1
        post.save()
        
        return HttpResponse(post.greenCount)
    
class ReactionsViewYellow(View):
    def get(self, request):
        postId = request.GET['postId']
        try:
            post = Posts.objects.get(id=int(postId))
        except Posts.DoesNotExist:
            return HttpResponse(-1)
        except ValueError: 
            return HttpResponse(-1)
        
        post. yellowCount =  post. yellowCount + 1
        post.save()
        
        return HttpResponse(post.yellowCount)
            
class ReactionsViewRed(View):
    def get(self, request):
        postId = request.GET['postId']
        try:
            post = Posts.objects.get(id=int(postId))
        except Posts.DoesNotExist:
            return HttpResponse(-1)
        except ValueError: 
            return HttpResponse(-1)
        
        post. redCount =  post. redCount + 1
        post.save()
        
        return HttpResponse(post.redCount)
    
class ReactionsViewStop(View):
    def get(self, request):
        postId = request.GET['postId']
        try:
            post = Posts.objects.get(id=int(postId))
        except Posts.DoesNotExist:
            return HttpResponse(-1)
        except ValueError: 
            return HttpResponse(-1)
        
        post. stopCount =  post. stopCount + 1
        post.save()
        
        return HttpResponse(post.stopCount)



class LoadMapView(View):

    def get(self, request):
        glasgowCoordinates = [ 55.8554403, -4.3024976 ]
        
        postIDs = request.GET['postIDs'].split()

        posts = []
        
        for postID in postIDs:
            try:
                ## If the location is invalid, don't add it to the list of locations
                numbers = Posts.objects.get(id=int(postID)).location.split(',')
                posts += [ { 'title': Posts.objects.get(id=int(postID)).title, 'location': [ float(numbers[0]), float(numbers[1])] }  ]
            except:
                pass

        
        ## If the centre is not glasgow, use the first location as the centre
        if request.GET['centre'] == 'glasgow':
            centre = glasgowCoordinates
        else:
            try:
                centre = [ float(posts[0]['location'][0]), float(posts[0]['location'][1]) ]
            except:
                centre = glasgowCoordinates

        data = json.dumps({'posts': posts, 'centre': centre} )

        return HttpResponse(data)
        















