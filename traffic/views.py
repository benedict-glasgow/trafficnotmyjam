from django.shortcuts import render, redirect
from django.http import HttpResponse
from traffic.models import Posts, Comments

def index(request):
    
    postsList = Posts.objects.order_by("-date")[:10]
    
    contextDict = {}
    contextDict["posts"] = postsList
    return render(request, 'traffic/index.html', context=contextDict)


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


    return render(request, 'traffic/post.html', context=contextDict)


def information(request):
    contextDict = {}
    return render(request, 'traffic/informationTesting.html', context=contextDict)


def about(request):
    return redirect('/about/information/')


def rules(request):
    contextDict = {}
    return render(request, 'traffic/rulesTesting.html', context=contextDict)


def FAQ(request):
    contextDict = {}
    return render(request, 'traffic/FAQTesting.html', context=contextDict)





















