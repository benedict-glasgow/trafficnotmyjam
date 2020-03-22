from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from traffic.models import Posts, Comments
from traffic.forms import SearchForm, PostsForm, CommentsForm, UserForm, UserProfileForm
from traffic.multichoice import POST_CATEGORIES
#from django import template
#register = template.Library()

def index(request):
    
    postsList = Posts.objects.order_by("-date")[:10]
    
    contextDict = {}
    contextDict["posts"] = postsList
    return render(request, 'traffic/index.html', context=contextDict)



#@register.inclusion_tag('writeComment.html')
def post(request, postSlug):
    contextDict = {}
    
    try:
        post = Posts.objects.get(slug=postSlug)
        comments = Comments.objects.filter(post=post)
        contextDict['post'] = post
        if comments.exists():
            contextDict['comments'] = comments
        else:
            contextDict['comments'] = None
            
    except Posts.DoesNotExist:
        contextDict['post'] = None
        contextDict['comments'] = None
    except: Comments.DoesNotExist
    
    
    return render(request, 'traffic/postTesting.html', context=contextDict)


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

    return render(request, 'traffic/searchResultTesting.html', contextDict)
    # return render(request, 'traffic/results.html', contextDict) Not sure which html page to lead to?

def addPosts(request):
    form = PostsForm()
    
    if request.method =='POST':
        form = PostsForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
            
    return render(request, 'traffic/writePosts.html', {'form': form})

def addComments(request,pk):
    post= get_object_or_404(Posts, pk=pk)
    form = CommentsForm()
    
    if request.method =='POST':
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            form.post = post
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
            
    return render(request, 'traffic/writeComment.html', {'form': form})


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

    return render(request, 'traffic/registrationTesting.html', context=contextDict)


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
        return render(request, 'traffic/loginTesting.html')


@login_required
def userLogout(request):
    logout(request)
    return redirect(reverse('traffic:index'))
   

    

















