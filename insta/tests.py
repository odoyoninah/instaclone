from django.test import TestCase
from .models import *


class ImageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.image = Image.objects.create(user=self.user, image='test.jpg')
        self.comment = Comment.objects.create(user=self.user, image=self.image, comment='test')

    def test_instance(self):
        self.assertTrue(isinstance(self.testuser, Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.image = Image.objects.create(user=self.user, image='test.jpg')
        self.comment = Comment.objects.create(user=self.user, image=self.image, comment='test')

    def test_instance(self):
        self.assertTrue(isinstance(self.testuser, Comment))

class LikeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.image = Image.objects.create(user=self.user, image='test.jpg')
        self.like = Like.objects.create(user=self.user, image=self.image)

    def test_instance(self):
        self.assertTrue(isinstance(self.testuser, Like))

class FollowTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.follower = User.objects.create_user(username='follower', password='12345')
        self.follow = Follow.objects.create(user=self.user, follower=self.follower)

    def test_instance(self):
        self.assertTrue(isinstance(self.testuser, Follow))

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_instance(self):
        self.assertTrue(isinstance(self.testuser, User))




