from django.test import TestCase
from blog.models import Post
# Create your tests here.


class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(author='manoel')

    def test_author(self):
        post_author = Post.objects.get(author='manoel')
        self.assertEqual(post_author.author, 'manoel')
