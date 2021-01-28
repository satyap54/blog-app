from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


from . models import Post

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import datetime

# Create your views here.
class PostListView(ListView):
	model = Post
	template_name = "blog/home.html"
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5
	


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_create.html'

	def test_func(self):
		post = self.get_object()
		return post.author == self.request.user

	def form_valid(self, form):
		form.instance.date_updated = datetime.datetime.now()
		form.instance.author = self.request.user
		form.instance.is_updated_once = True
		return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'

	def test_func(self):
		post = self.get_object()
		return post.author == self.request.user

	def get_success_url(self):
		return reverse('blog:home')