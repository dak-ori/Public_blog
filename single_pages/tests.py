from django.test import TestCase, Client
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from blog.models import Post

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_dakori = User.objects.create_user(username='dakori', password='somepassword')
    
    def test_landing(self):
        post_001 = Post.objects.create(
            title = '첫번째',
            content = 'Hello, World',
            author = self.user_dakori
        )
        
        post_002 = Post.objects.create(
            title = '두번째',
            content = '늦었다',
            author = self.user_dakori
        )
        
        post_003 = Post.objects.create(
            title = '세번째',
            content = '카테고리 없음',  
            author = self.user_dakori
        )
        
        post_004 = Post.objects.create(
            title = '네번째',
            content = '네번째',
            author = self.user_dakori
        )
        
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        body = soup.body
        self.assertNotIn(post_001.title, body.text)
        self.assertIn(post_002, body.text)
        self.assertIn(post_003, body.text)
        self.assertIn(post_004, body.text)
        