from django.urls import path

from . import views

urlpatterns = [
    path('show_headings/', views.show_headings),
    path('show_contents/<int:pk>/', views.show_contents)
]