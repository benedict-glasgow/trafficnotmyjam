from django.test import TestCase
from traffic.models import Posts,UserProfile
from django.contrib.auth.models import User

class PostsReactionsTests(TestCase):
    def test_ensure_reactions_are_positive(self):
        """ Checks that the number of each reaction is greater than or equal to 0. """ 
        user = User.objects.get_or_create(username='test', password = 'test')[0]
        user.save()
        post = Posts(title='test', user=user,description = 'test',location= 'G1',category = 'general-jams',
                     greenCount=-1,yellowCount=-1,redCount=-1,stopCount=-1 ) 
        post.save()
        self.assertEqual((post.greenCount >= 0 and post.yellowCount >= 0 and post.redCount >=0 and post.stopCount >=0), True)