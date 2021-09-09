from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    model = CustomUser
    template_name = "signup.html"
