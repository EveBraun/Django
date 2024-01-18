from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

menu = [{'title': 'Posts', 'url_name': 'main:post_list'}, 
        {'title': 'Add posts', 'url_name': 'main:post_add'},
        {'title': 'About site', 'url_name': 'main:about'},
        {'title': 'Contacts', 'url_name': 'main:contacts'},
        ]

# главная страница сайта
def index_root(request):
    return render(request, 'main/index_root.html')

# главная cтраница приложения main
def index(request):
    return render(request, 'main/index.html', context={'menu': menu})

# ДЗ!!!
def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')



# отображение списка постов
def post_list(request):
    # получаем все объекты таблицы(модели) Post
    posts = Post.objects.all()
    # заносим их  вобъкт-контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)



def post_add(request):
    title = "Создать пост"
    if request.method == "GET":
        form = PostForm()
        context = {'title': title, "menu": menu, "form": form}
        return render(request, 'main/post_add.html', context)
    
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = Post()
            post.author = post_form.cleaned_data['author']
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.save()
            return post_list(request)