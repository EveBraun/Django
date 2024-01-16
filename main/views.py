from django.shortcuts import render
from .models import Post

# Create your views here.

menu = [{'title': 'Posts', 'url_name': 'main:post_list'}, 
        # {'title': 'Add posts', 'url_name': 'main:post_add'},
        # {'title': 'About site', 'url_name': 'main:about'},
        # {'title': 'Contacts', 'url_name': 'main:contacts'},
        ]

def index_root(request):
    return render(request, 'main/index.html')

def index(request):
    return render(request, 'main/index.html')

# ДЗ!!!
def about_site(request):
    pass

# отображение списка постов
def post_list(request):
    # получаем все объекты таблицы(модели) Post
    posts = Post.objects.all()
    # заносим их  вобъкт-контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)