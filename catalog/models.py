from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import date


# Create your models here.
class Genre(models.Model):
    name = models.CharField('分类', max_length=200,
                            help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Author(models.Model):
    first_name = models.CharField('名', max_length=100)
    last_name = models.CharField('姓', max_length=100)
    date_of_birth = models.DateField('出生日期', null=True, blank=True)
    date_of_death = models.DateField('死亡日期', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Language(models.Model):
    name = models.CharField('语言', max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    class Meta:
        verbose_name = '语言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('书名', max_length=200)
    author = models.ForeignKey(Author, verbose_name='作者',
                               on_delete=models.SET_NULL, null=True)
    summary = models.TextField('摘要', max_length=1000,
                               help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, verbose_name='分类',
                                   help_text='Select a genre for this book')
    language = models.ForeignKey(Language, verbose_name='语言', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = '所有分类'


class BookInstance(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, verbose_name='书籍', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField('出版商名称', max_length=200)
    due_back = models.DateField('归还日期', null=True, blank=True)
    borrower = models.ForeignKey(User, verbose_name='出借人', on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField('状态', max_length=1, choices=LOAN_STATUS, blank=True, default='m',
                              help_text='Book availability',)

    class Meta:
        ordering = ['due_back']
        verbose_name = '藏书'
        verbose_name_plural = verbose_name
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return "%s (%s)" % (self.id, self.book.title)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
