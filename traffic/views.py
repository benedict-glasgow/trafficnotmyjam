from django.shortcuts import render, redirect
from django.http import HttpResponse
from traffic.models import Posts, Comments
from traffic.forms import SearchForm, PostsForm

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

    slugs = Posts.objects.values('categorySlug').distinct()
    categories = []

    if slugs.exists():
        for slug in slugs:
            ## Get a name of the category for each slug:
            categories += Posts.objects.filter(categorySlug=slug['categorySlug']).values('category').distinct()

        print(categories, list(slugs))
        contextDict['categories'] = zip(categories, slugs)
        
    else:
        contextDict['categories'] = None


    return render(request, 'traffic/categoriesTesting.html', context=contextDict)


def category(request, categorySlug):
    contextDict = {}

    posts = Posts.objects.filter(categorySlug=categorySlug)

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

    posts = Posts.objects.filter(title=searchQuery)

    if posts.exists():
        contextDict['posts'] = posts
    else:
        contextDict['posts'] = None

<<<<<<< HEAD
    return render(request, 'traffic/searchResultTesting.html', contextDict)

def addPosts(request):
    form = PostsForm()
    
    if request.method =='POST':
        form = PostsForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect(' ')
        else:
            print(form.errors)
            
    return render(request, '/post/writePosts.html', {'form': form})

        
=======
    return render(request, 'traffic/results.html', contextDict)
>>>>>>> cae0ed468f39d674b3505803b68cf83329a0f8c8
    

















