from django.test import TestCase
from django.shortcuts import reverse

from blog.models import *


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Yegane')
        cls.post1 = Post.objects.create(
            title='post_title1',
            author=cls.user,
            text='This is the description in this code i want to test if it works',
            status=Post.STATUS_CHOICES[0][0]  # published
        )
        cls.post2 = Post.objects.create(
            author=cls.user,  # nist cls  چونکه فقط تو خود همین متد استفاده میشه نه بقیه تست ها لازم به
            title='post_title2',
            text='This is the description 2',
            status=Post.STATUS_CHOICES[1][0]  # draft
        )

    # def setUp(self) -> None:

    def test_post_url(self):
        res = self.client.get('/blog/')
        self.assertEqual(res.status_code, 200)

    def test_post_url_by_name(self):
        res = self.client.get(reverse('posts_list'))

    def test_post_list_content(self):
        res = self.client.get(reverse('posts_list'))
        self.assertContains(res, self.post1.title)
        self.assertContains(res, 'post_title1')

    def test_post_detail_url_by_name(self):
        res = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(res.status_code, 200)

    def test_post_detail_url(self):
        res = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(res.status_code, 200)

    def test_post_detail_content(self):
        res = self.client.get(reverse('post_detail', args=[self.post1.id]))
        # self.assertContains(res,'post_title1')
        self.assertContains(res, self.post1.title)

    def test_post_not_exist(self):
        res = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(res.status_code, 404)

    def test_draft_post_not_display_in_postlist(self):
        res = self.client.get(reverse('posts_list'))
        self.assertContains(res, self.post1.title)
        self.assertNotContains(res, self.post2.title)

    def test_post_model_str(self):
        post = self.post1
        expected_output = f' {post.title} : {post.text[:30]}...'
        self.assertEqual(str(post), expected_output)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post_title1')
        self.assertEqual(self.post1.text, 'This is the description in this code i want to test if it works')
        self.assertEqual(self.post1.author.username, 'Yegane')
        self.assertEqual(self.post1.status, 'pub')

    def test_create_post(self):
        res = self.client.post(reverse('post_create'), {
            'title': 'test title create',
            'text': 'test text create',
            'author': self.user.id,
            'status': 'pub'
        })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'test title create')
        self.assertEqual(Post.objects.last().text, 'test text create')

    def test_update_post(self):
        res = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'post 2 title sample updated',
            'text': 'post 2 text sample updated',
            'author': self.post2.author.id,
            'status': 'pub'
        })
        self.assertEqual(res.status_code, 302)
        # self.assertEqual(Post.objects.filter(pk=2).values_list('title', flat=True).first(),'post 2 title sample updated')
        self.assertEqual(Post.objects.last().title, 'post 2 title sample updated')
        self.assertEqual(Post.objects.last().text, 'post 2 text sample updated')

    def test_delete_post(self):
        res = self.client.post(reverse('post_delete', args=[self.post2.pk]))
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(res.status_code, 302)
        self.assertNotContains(response,self.post2.title)

    def test_post_delete_not_exist(self):
        res = self.client.get(reverse('post_delete',args=[1000]))
        self.assertEqual(res.status_code,404)

