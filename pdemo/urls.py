
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", index, name='index' ),
    path("logout/", user_logout, name="logout"),

    path("dashboard", dashboard, name='dashboard'),
    path("button/", button, name='button'),
    path("dropdowns/", dropdowns, name='dropdowns'),
    path("typography/", typography, name='typography'),
    path("fontawsome/", fontawsome, name='font-awsome'),
    path("forms/", forms, name='forms'),
    path("chart/", chart, name='chart'),
    path("table/", table, name='table'),
    path("blank-page/", blank_page, name='blank-page'),
    # path("login/", login, name='login'),
    path("register/", register, name='register'),
    path("error-404/", error_404, name='error-404'),
    path("error-500/", error_500, name='error-500'),
    path("contact", contact, name="contact"),
    path("contact-list/", contact_list, name='contact-list'),
    path('delete_contact/<int:contact_id>/', delete_contact, name='delete_contact'),
    path('edit_contact/<int:contact_id>/', edit_contact, name='edit_contact'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
