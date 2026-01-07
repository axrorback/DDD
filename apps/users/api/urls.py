from django.urls import path
from apps.users.api.views import RegisterView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
]