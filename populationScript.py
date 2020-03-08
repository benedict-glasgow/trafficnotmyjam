import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tnmjproject.settings')

import django
django.setup()
from traffic.models import Posts

def populate():

    pythonPosts = [
        { 'title': "Dont be fucking rude",
          'description': "I'm gonna hurt you, I swear to God",
          'photo': 'blank',
          'location': "G12",
          'category': "Bad Parking"
          },
        { 'title': "Are you kidding me?",
          'description': "no",
          'photo': 'blank',
          'location': "G13",
          'category': "Bad Parking"
          },
        { 'title': "SERIOUSLY",
          'description': "I am furious!! Imagine the audacity at the actual \
center of Glasgow!!",
          'photo': 'blank',
          'location': "G1",
          'category': "Bad Parking"
          },
        ]

    for post in pythonPosts:
        addPosts(post['title'], post['description'], post['photo'],
                 post['location'], post['category'])
    for p in Posts.objects.all():
            print(f'- {p}')


def addPosts(title, description, photo, location, category):
    post = Posts.objects.get_or_create(title=title,description = description,photo = photo,location = location,category = category)[0]
    #post.description = description
    #post.photo = photo
    #post.location = location
    #post.category = category
    post.save()
    return post

if __name__ =='__main__':
    print('Starting traffic population script')
    populate()


