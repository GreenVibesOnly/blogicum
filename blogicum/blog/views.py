from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import CommentForm, PostForm, UserForm
from .models import Category, Comment, Post
from .mixins import CommentMixinView, PostMixinView
from .utils import filter_posts, unfilter_posts


User = get_user_model()


class IndexListView(ListView):
    ''' Главная страница, все опубл. посты '''
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pub_date'
    paginate_by = 10

    def get_queryset(self):
        return filter_posts()


class CategoryListView(IndexListView):
    ''' Страница категории, посты категории '''
    template_name = 'blog/category.html'
    category = None

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs['category'],
            is_published=True
        )
        return super().get_queryset().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProfileListView(IndexListView):
    ''' Страница профиля, посты пользователя '''
    template_name = 'blog/profile.html'
    author = None

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        if self.author == self.request.user:
            return unfilter_posts().filter(author=self.author)
        return super().get_queryset().filter(author=self.author)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.author
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    ''' Редактирование профиля '''
    model = User
    form_class = UserForm
    template_name = 'blog/user.html'
    user_obj = None

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('blog:profile', kwargs={'username': self.request.user})


class PostDetailView(DetailView):
    ''' Страница отдельного поста '''
    model = Post
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'post_id'  # Добавляет pk к url
    post = None

    def get_queryset(self):
        self.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        if self.post.author == self.request.user:
            return unfilter_posts().filter(id=self.kwargs['post_id'])
        return filter_posts().filter(id=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        ''' Дополняет context '''
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = (
            # Дополнительно подгружаем авторов комментариев,
            # чтобы избежать множества запросов к БД.
            self.post.comments.select_related('author')
        )
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    ''' Создание поста '''
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:profile', kwargs={'username': self.request.user})


class PostUpdateView(PostMixinView, UpdateView):
    ''' Редактирование поста '''
    form_class = PostForm


class PostDeleteView(PostMixinView, DeleteView):
    ''' Удаление поста '''

    def get_success_url(self):
        return reverse('blog:profile', kwargs={'username': self.request.user})


class CommentCreateView(LoginRequiredMixin, CreateView):
    ''' Создание комментария '''
    model = Comment
    form_class = CommentForm
    post_obj = None

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(
            Post,
            id=kwargs['post_id'],
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post_obj
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'post_id': self.kwargs['post_id']}
        )


class CommentUpdateView(CommentMixinView, UpdateView):
    ''' Редактирование комментария '''
    form_class = CommentForm


class CommentDeleteView(CommentMixinView, DeleteView):
    ''' Удаление комментария '''
    pass
