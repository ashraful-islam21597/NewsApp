from django.urls import path

from users.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('<int:pk>/',ProfileView.as_view(),name='profile'),
    #path('<int:pk>/edit/',profileUpdateView.as_view(),name='profile_edit')
]