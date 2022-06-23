from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # lastname = request.POST.get("last_name")
        # firstname = request.POST.get("first_name")
        password = request.POST.get("password")
        username=request.POST.get("username")
        email = request.POST.get("email")
        user = User.objects.create_user(password = password, email = email, username=username)

        login(request, user)
        # return redirect('index')
        return redirect('index')       

    return render(request, "accounts/signup.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect('index')
            
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')