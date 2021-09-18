from base.models import Book
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Book

class HomeView(TemplateView):
    template_name = 'base/home.html'

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Books')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Books')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Books')
        return super(RegisterPage, self).get(*args, **kwargs)


class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['books'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['books'] = context['books'].filter(
                title__icontains=search_input) 

        context['search_input'] = search_input
        return context
 
class BookDetail(LoginRequiredMixin, DetailView):
    model = Book 
    context_object_name = 'book'
    template_name = 'base/book.html'

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'progress', 'notes', 'status']
    success_url = reverse_lazy('Books')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate, self).form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'progress', 'notes' , 'status']
    success_url = reverse_lazy('Books')

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('Books')