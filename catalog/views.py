from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, BookInstance, Author


# Create your views here.
# function based
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


# class-based
class BookListView(generic.ListView):
    model = Book
    # template_name = 'catalog/book_list.html'
    # context_object_name = 'book_list'
    paginate_by = 5

    # queryset = Book.objects.filter(title__icontains='Family')[:5]
    # def get_queryset(self):
        # return Book.objects.filter(title__icontains='Family')[:5]
        # return Book.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book
    # template_name = 'catalog/book_detail.html'
    # context_object_name = 'book'


class AuthorListView(generic.ListView):
    model = Author
    # template_name = 'catalog/author_list.html'
    # context_object_name = 'author_list'
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    model = Author
    # template_name = 'catalog/author_detail.html'
    # context_object_name = 'author'


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    # context_object_name = 'bookinstance_list'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
