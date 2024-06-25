from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'dashboard.html')

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


def login(request):
    return render(request, 'pages/samples/login.html')


def register(request):
    return render(request, 'pages/samples/register.html')


def error_404(request):
    return render(request, 'pages/samples/error-404.html')


def error_500(request):
    return render(request, 'pages/samples/error-500.html')
#