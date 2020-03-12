from django.shortcuts import render
from django.http import HttpResponse
from traffic.models import Posts, Comments

def index(request):
    
    postsList = Posts.objects.order_by("-date")[:10]
    
    contextDict = {}
    contextDict["posts"] = postsList
    return render(request, 'traffic/index.html', context=contextDict)


def post(request, postSlug):
    contextDict = {}
    print(postSlug)


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
