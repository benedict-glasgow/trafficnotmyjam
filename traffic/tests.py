from django.test import TestCase
from traffic.models import Posts
from traffic.forms import PostsForm,CommentsForm,UserForm,ChangePasswordForm
from django.contrib.auth.models import User


class ModelsTests(TestCase):
    def test_ensure_reactions_are_positive(self):
        """ Checks that the number of each reaction is greater than or equal to 0. """ 
        user = User.objects.get_or_create(username='test', password = 'test')[0]
        user.save()
        post = Posts(title='test', user=user,description = 'test',location= 'G1',category = 'general-jams',
                     greenCount=-1,yellowCount=-1,redCount=-1,stopCount=-1 ) 
        post.save()
        self.assertEqual((post.greenCount >= 0 and post.yellowCount >= 0 and post.redCount >=0 and post.stopCount >=0), True)
        
        
    def test_slug_line_creation(self): 
        """ When a post is created an approprate slug should be created. """ 
        user = User.objects.get_or_create(username='test', password = 'test')[0]
        user.save()
        post = Posts(title='Testing Post Slug',user=user,description = 'test',location= 'G1',category = 'general-jams',
                     greenCount=0,yellowCount=0,redCount=0,stopCount=0 ) 
        post.save()
        self.assertEqual(post.slug, 'testing-post-slug1')

class FormTests(TestCase):
    def test_posts_form(self):
        """ Tests PostsForm is valid. """ 
        form = PostsForm(data ={'title':'Testing Posts Form','description':'test','location':'G1','category':'general-jams'})
        self.assertTrue(form.is_valid())
        
    def test_posts_form_invalid(self):
        """ Tests PostsForm is invalid. """ 
        form = PostsForm(data ={'title':'','description':'','location':'','category':''})
        self.assertFalse(form.is_valid())
        
    def test_comment_form(self):
        """ Tests CommentsForm is valid. """ 
        form = CommentsForm(data = {'content':'test content'})
        self.assertTrue(form.is_valid())
        
    def test_comment_form_invalid(self):
        """ Tests CommentsForm is invalid. """ 
        form = CommentsForm(data = {'content':''})
        self.assertFalse(form.is_valid())
        
    def test_user_form(self):
        """ Tests UserForm is valid. """ 
        form = UserForm(data = {'username': 'test','password':'test1'})
        self.assertTrue(form.is_valid())
        
    def test_user_form_invalid(self):
        """ Tests UserForm is invalid. """ 
        form = UserForm(data = {'username': '','password':''})
        self.assertFalse(form.is_valid())
        
    def test_change_password_form(self):
        """ Tests ChangePasswordForm is valid. """ 
        form = ChangePasswordForm(data = {'oldPassword' : 'test', 'newPassword' : 'test2', 'repeatNewPassword': 'test2'})
        self.assertTrue(form.is_valid())
        
    def test_change_password_form_invalid(self):
        """ Tests ChangePasswordForm is invalid. """ 
        form = ChangePasswordForm(data = {'oldPassword' : '', 'newPassword' : '', 'repeatNewPassword': ''})
        self.assertFalse(form.is_valid())

class UserLoginTest(TestCase):
    def test_user_login(self):
        """ Checks a user can login with a valid username and password. """ 
        user = User.objects.get_or_create(username='test')[0]
        user.set_password('test')
        user.save()
        checkLogin = self.client.login(username='test', password='test')
        self.assertTrue(checkLogin)
        
    def test_user_invalid_login(self):
        """ Checks a user can login with a invalid username and password. """ 
        checkLogin = self.client.login(username='test', password='test')
        self.assertFalse(checkLogin)
        
        
        