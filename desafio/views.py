from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

# Signup
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# Login
class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"

# Logout
class LogoutView(auth_views.LogoutView):
    template_name = "registration/logged_out.html"
