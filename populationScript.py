import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tnmjproject.settings')

import django
django.setup()
from traffic.models import Posts, UserProfile, Comments, User


from django.utils import timezone


def populate():
    

    postsData = [
        { 'title': "Dont be rude",
          'description': "This makes me so angry",
          'photo': 'postImages\worstparking.jpg',
          'location': "55.8816012, -4.3175199",
          'date' : timezone.now(),
          'category': 'how-not-to-drive',
          'greenCount': 100,
          'yellowCount': 50,
          'redCount': 25,
          'stopCount': 10
          },
        { 'title': "Are you kidding me?",
          'description': "I cannot believe this",
          'photo': 'postImages\cyclelanes.jpg',
          'location': "55.8947967, -4.3668728",
          'date' : timezone.now(),
          'category': 'bad-parking',
          'greenCount': 27,
          'yellowCount': 45,
          'redCount': 21,
          'stopCount': 11,
          },
        { 'title': "SERIOUSLY",
          'description': "I am furious!! Imagine the audacity at the actual \
          center of Glasgow!!",
          'photo': 'postImages\Pothole.jpg', 
          'location': "55.8589193, -4.2589934",
          'date' : timezone.now(),
          'category': 'general-jams',
          'greenCount': 300,
          'yellowCount': 500,
          'redCount': 700,
          'stopCount': 1000
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
    



    for user in userData:
        u = addUser(user['username'],user['password'])
        addUserProfile(u)


    for post in postsData:
        p = addPosts(post['title'], User.objects.order_by('?').first(), post['description'], post['photo'],
                 post['location'],post['date'], post['category'],post['greenCount'],post['yellowCount'],post['redCount'],post['stopCount']) 

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


    


def addPosts(title, user, description, photo, location,date, category,greenCount,yellowCount,redCount,stopCount): 
    post = Posts.objects.get_or_create(title=title, user=user, description=description, photo=photo, location=location,date=date, category=category,
                                       greenCount=greenCount, yellowCount=yellowCount, redCount=redCount, stopCount=stopCount)[0]
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


if __name__ =='__main__':
    print('Starting traffic population script')
    print(timezone.now())
    populate()


