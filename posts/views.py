from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Post

#Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



# def index(request):
#     posts = Posts.objects.all()
#     return render(request, 'index.html', {'posts': posts})

# def post(request, pk):
#     posts = Posts.objects.get(id=pk)
#     return render(request, 'posts.html', {'posts': posts})
