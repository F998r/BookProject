from django.urls import path
from apps.bookmodule import views   # Ensure this line is present and correct

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns here
]
