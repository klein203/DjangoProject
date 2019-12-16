from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(name='name', verbose_name=r'分类', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'博客分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(name='name', verbose_name=r'标签', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = r'博客标签'
        verbose_name_plural = verbose_name


class Entry(models.Model):
    title = models.CharField(name='title', verbose_name=r'文章标题', max_length=128)
    author = models.ForeignKey(User, related_name='author', verbose_name=r'作者', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog_img', verbose_name=r'博客配图', null=True, blank=True)
    body = models.TextField(name='body', verbose_name=r'正文')
    abstract = models.TextField(name='abstract', verbose_name=r'摘要', max_length=256, null=True, blank=True)
    visiting = models.PositiveIntegerField(name='visiting', verbose_name=r'访问量', default=0)
    category = models.ManyToManyField(Category, related_name='category', verbose_name=r'博客分类')
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name=r'标签')
    create_time = models.DateTimeField(name='create_time', verbose_name=r'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(name='update_time', verbose_name=r'修改时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = r'博客正文'
        verbose_name_plural = verbose_name