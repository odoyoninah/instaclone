from django.test import TestCase
from .models import *

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image_test = Image(image='image.jpg',caption='This is a test image')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image_test,Image))

    # Testing Save Method
    def test_save_method(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    # Testing Update Method
    def test_update_method(self):
        self.image_test.update_caption('This is a new caption')
        images = Image.objects.all()
        self.assertTrue(images[0].caption == 'This is a new caption')

class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comment_test = Comment(comment='This is a test comment')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment_test,Comment))

    # Testing Save Method
    def test_save_method(self):
        self.comment_test.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.comment_test.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 0)

    # Testing Update Method
    def test_update_method(self):
        self.comment_test.update_comment('This is a new comment')
        comments = Comment.objects.all()
        self.assertTrue(comments[0].comment == 'This is a new comment')

class LikeTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.like_test = Like(like='This is a test like')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.like_test,Like))

    # Testing Save Method
    def test_save_method(self):
        self.like_test.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.like_test.delete_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) == 0)








    