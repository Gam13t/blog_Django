from django.shortcuts import render
from .models import Post

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


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
