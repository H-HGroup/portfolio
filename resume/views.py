from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserLoginForm  


def Home(request):
    return render(request, "home.html")


def AdminChat(request):
    return render(request,'chat.html')


def UserLogout(request):  
    logout(request)  
    return redirect('Home')  


def UserLogin(request):  
    if request.method == 'POST':  
        form = UserLoginForm(request.POST)  
        if form.is_valid():  
            data = form.cleaned_data  
            user = authenticate(request, username=data['username'], password=data['password'])  

            if user is not None:  
                login(request, user)  
                if user.is_superuser:  
                    return redirect('AdminChat')  
                else:  
                    return redirect('Home')   

        return render(request, 'home.html', {'form': form, 'error': 'نام کاربری یا رمز عبور نامعتبر است'})   

    else:  
        form = UserLoginForm()  
        return render(request, 'home.html', {'form': form})


def ContactUs(request):
    return render(request, 'contact.html')
