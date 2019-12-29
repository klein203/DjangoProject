import datetime
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .models import Book, BookInstance, Author
from .forms import RenewBookForm, RenewBookModelForm


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


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    # context_object_name = 'bookinstance_list'
    paginate_by = 5
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        # form = RenewBookForm(request.POST)
        form = RenewBookModelForm(request.POST)

        if form.is_valid():
            # book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.due_back = form.cleaned_data['due_back']
            book_instance.save()

            return HttpResponseRedirect(reverse('catalog:all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        # form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
        form = RenewBookModelForm(initial={'due_back': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '2099/01/01'}
    # template_name = 'author_form.html'
    # success_url = reverse_lazy('catalog:authors')


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    # success_url = reverse_lazy('catalog:author-detail', self.id)


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    # template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('catalog:authors')


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    # template_name = 'book_form.html'
    # success_url = reverse_lazy('catalog:books')


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']
    # success_url = reverse_lazy('catalog:book-detail', self.id)


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    # template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('catalog:books')
