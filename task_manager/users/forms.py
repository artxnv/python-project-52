from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].requred = True

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2'
                  ]


class UserUpdateForm(UserCreateForm):

    def clean_username(self):
        return self.cleaned_data.get("username")
