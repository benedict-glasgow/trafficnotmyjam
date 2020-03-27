import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tnmjproject.settings')

import django
django.setup()
from traffic.models import Posts, UserProfile, Comments, Reactions, User


from django.utils import timezone


def populate():
    

    postsData = [
        { 'title': "Dont be rude",
          'description': "I'm gonna hurt you, I swear to God",
          'photo': 'blank',
          'location': "55.8816012, -4.3175199",
          'date' : timezone.now(),
          'category': 'how-not-to-drive'
          },
        { 'title': "Are you kidding me?",
          'description': "no",
          'photo': 'blank',
          'location': "55.8947967, -4.3668728",
          'date' : timezone.now(),
          'category': 'bad-parking'
          },
        { 'title': "SERIOUSLY",
          'description': "I am furious!! Imagine the audacity at the actual \
          center of Glasgow!!",
          'photo': 'blank',
          'location': "55.8589193, -4.2589934",
          'date' : timezone.now(),
          'category': 'general-jams'
          },
        ]
    userData = [{'username' : 'Jenny',
                   'password': 'test1test2'
                   },
                  {'username' : 'Mark',
                   'password': 'test2test3'
                   },
                   {'username' : 'Gary',
                   'password': 'test3test4'
                   },
    
            ]
    commentsData = [{'content':"I think this is the rudest thing I have ever seen!"},
                   {'content': "I cannot believe that this has happend, you couldnt make it up"},
                   {'content': "I dont understand how this could even happen"},
                  ]
    
    reactionsData = [{'name' : 'Red',
                      'count':12},
                     {'name' : 'Amber',
                      'count':10},
                     {'name' : 'Green',
                      'count':1},
                     {'name' : 'Stop',
                      'count':100},
                      ]



    for user in userData:
        u = addUser(user['username'],user['password'])
        addUserProfile(u)


    for post in postsData:
        p = addPosts(post['title'], User.objects.order_by('?').first(), post['description'], post['photo'],
                 post['location'],post['date'], post['category']) 

    for reaction in reactionsData:
        addReactions(p, reaction['name'],reaction['count'])

    for comment in commentsData:
        addComment(p, User.objects.order_by('?').first(), comment['content'])
    
    print("Posts :")
    for p in Posts.objects.all():
            print(f'- {p}')
    print("Users :")
    for u in User.objects.all():
        print(f'- {u}')
    print("Comments :")
    for c in Comments.objects.all():
        print(f'- {c}')
    print("Reactions :")
    for r in Reactions.objects.all():
        print(f'- {r}')
    


def addPosts(title, user, description, photo, location,date, category): 
    post = Posts.objects.get_or_create(title=title, user=user, description=description, photo=photo, location=location,date=date, category=category)[0]
    post.save()
    return post

def addUser(username, password):
    user = User.objects.get_or_create(username=username, password = password)[0]
    user.set_password(user.password)
    user.save()
    return user

def addUserProfile(user):
    userProfile = UserProfile.objects.get_or_create(user=user)[0]
    userProfile.save()
    return userProfile

def addComment(post, user, content):
    comment = Comments.objects.get_or_create(post=post, content=content, user=user)[0]
    comment.save()
    return comment

def addReactions(post,name,count):
    reaction = Reactions.objects.get_or_create(post=post,name=name,count=count)[0]
    reaction.save()
    return reaction

if __name__ =='__main__':
    print('Starting traffic population script')
    print(timezone.now())
    populate()


