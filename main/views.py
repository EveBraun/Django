from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
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
    return redirect(post_list)

# главная cтраница приложения main
def index(request):
    return HttpResponsePermanentRedirect("/blog/posts")


def about(request):
    context={'menu': menu}
    return render(request, 'main/about.html', context=context)

def contacts(request):
    context={'menu': menu}
    return render(request, 'main/contacts.html', context=context)



# отображение списка постов
def post_list(request):
    # получаем все объекты таблицы(модели) Post
    posts = Post.objects.all()
    # заносим их  вобъкт-контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)

@login_required
def post_add(request):
    title = "Создать пост"
    if request.method == "GET":
        form = PostForm()
        context = {'title': title, "menu": menu, "form": form}
        return render(request, 'main/post_add.html', context)
    
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = Post()
            post.author = request.user
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.image = post_form.cleaned_data['image']
            post.publish()
            
            return post_list(request)
        

# 23/01/24
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    title = 'Info about post'
    context = {'post': post, 'title': title}
    return render(request, template_name="main/post_detail.html", context=context)
