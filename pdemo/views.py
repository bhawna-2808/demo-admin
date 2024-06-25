from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from login.models import CustomUser
# Create your views here.


def index(request):
    try:
        if request.user.is_authenticated:
            return redirect("dashboard")
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            # Fetch user by email
            try:
                user = CustomUser.objects.get(email=email)
                email = user.email
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid email or password!")
                return redirect("index")

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome to the Dashboard!")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid email or password!")
                return redirect("index")
        return render(request, "pages/samples/login.html")
    except Exception as ex:
        print("Error in: login_page method", ex)
        messages.error(request, "An error occurred. Please try again.")
    return render(request, 'pages/samples/login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect("index")


def button(request):
    return render(request, 'pages/ui-features/buttons.html')

def dropdowns(request):
    return render(request, 'pages/ui-features/dropdowns.html')

def typography(request):
    return render(request, 'pages/ui-features/typography.html')


def fontawsome(request):
    return render(request, 'pages/icons/font-awesome.html')

def forms(request):
    return render(request, 'pages/forms/basic_elements.html')

def chart(request):
    return render(request, 'pages/charts/chartjs.html')


def table(request):
    return render(request, 'pages/tables/basic-table.html')


def blank_page(request):
    return render(request, 'pages/samples/blank-page.html')


# def login(request):
#     return render(request, 'pages/samples/login.html')


def register(request):
    return render(request, 'pages/samples/register.html')


def error_404(request):
    return render(request, 'pages/samples/error-404.html')


def error_500(request):
    return render(request, 'pages/samples/error-500.html')
#