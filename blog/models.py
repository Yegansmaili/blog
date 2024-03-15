from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    class Meta:
        verbose_name_plural = 'Posts'

    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='pub')

    def __str__(self):
        return f' {self.title} : {self.text[:30]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

class Comment(BaseModel):
    class Meta:
        verbose_name_plural = 'Comments'
    name = models.CharField(max_length=30 , default='Unknown')
    email = models.EmailField()
    content = models.TextField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return f'{self.name} : {self.content[:10]}... : {self.post.text[:50]}...'




