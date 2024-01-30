from django.shortcuts import render
from .forms import UserRegistrationForm
from main.views import menu

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            context = {'new_user': new_user}
            return render(request, 'users/register_done.html', context=context)
    
    user_form = UserRegistrationForm()
    context={'user_form': user_form, 'menu': menu}
    return render(request, 'users/register.html', context=context)

