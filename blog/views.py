from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                 )
# Just dummy data for debug... Can be deleted any moment you want to
posts = [
    {
        'author':  'Rostislav',
        'title': 'Test Post',
        'content': 'Test post content',
        'date_posted': 'August 11, 2019'
    },
    {
        'author': 'Ясыр',
        'title': 'Почему я стал геем',
        'content': 'Потому что я стал геем',
        'date_posted': 'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Защита Животных',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Бабки под подъездами, и как их победить',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'тут одни дегенераты на этой спецыальности  су....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Защита Животных',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Защита Животных',
        'content': 'берешь палку и ебешься',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Робот (Долбоеб)',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Робот (Долбоеб)',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': 'тут одни дегенераты на этой спецыальности  су....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Бабки под подъездами, и как их победить',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Телефоны убийцы!!',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Защита Животных',
        'content': 'тут одни дегенераты на этой спецыальности  су....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Телефоны убийцы!!',
        'content': 'Дома комары и мухи гонят их под гриву',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Робот (Долбоеб)',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Бабки под подъездами, и как их победить',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'в постели я самый лучший блаодря ей',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Бабки под подъездами, и как их победить',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': 'Дома комары и мухи гонят их под гриву',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Защита Животных',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Робот (Долбоеб)',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Бабки под подъездами, и как их победить',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': 'в постели я самый лучший блаодря ей',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Робот (Долбоеб)',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Робот (Долбоеб)',
        'content': 'тут одни дегенераты на этой спецыальности  су....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': 'в постели я самый лучший блаодря ей',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Бабки под подъездами, и как их победить',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Телефоны убийцы!!',
        'content': 'Дома комары и мухи гонят их под гриву',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Робот (Долбоеб)',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Дома комары и мухи гонят их под гриву',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Любят по утрам делать зарядку',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Робот (Долбоеб)',
        'content': 'щавель, димитил натрий хлор, аккуратно смешиваем в горячей воде в пропроции....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Телефоны убийцы!!',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': 'в постели я самый лучший блаодря ей',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'щавель, димитил натрий хлор, аккуратно смешиваем в горячей воде в пропроции....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'берешь палку и ебешься',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Робот (Долбоеб)',
        'content': 'щавель, димитил натрий хлор, аккуратно смешиваем в горячей воде в пропроции....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Телефоны убийцы!!',
        'content': 'тут одни дегенераты на этой спецыальности  су....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Робот (Долбоеб)',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Дома комары и мухи гонят их под гриву',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'DOdiCK',
        'title': 'Телефоны убийцы!!',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Защита Животных',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Робот (Долбоеб)',
        'content': 'тут одни дегенераты на этой спецыальности  су....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Защита Животных',
        'content': 'тогда наши курсы програмирования для вас...',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'щавель, димитил натрий хлор, аккуратно смешиваем в горячей воде в пропроции....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Телефоны убийцы!!',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Робот (Долбоеб)',
        'content': 'берешь палку и ебешься',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Rostik',
        'title': 'Защита Животных',
        'content': '12344223',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Телефоны убийцы!!',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Dostoevskiy_syka',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'Дома комары и мухи гонят их под гриву',
        'date_posted':'January 28, 2002'
    },
    {
        'author': 'Frik01',
        'title': 'Бабки под подъездами, и как их победить',
        'content': 'рыбачишь вооот такой хуергой,а потом....',
        'date_posted':'January 28, 2002'
    },
]


def home(request):
    context = {
        'posts': Post.objects.all()
        # Debugger with dummy data
        # 'posts': posts
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
