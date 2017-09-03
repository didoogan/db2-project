from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import extras


COUNTRYES = (
    ('Ukraine', 'Ukraine'),
    ('USA', 'USA'),
    ('United Kingdom', 'United Kingdom'),
    ('Australia', 'Australia'),
)

SITIES = (
    ('Kiev', 'Kiev'),
    ('Donetsk', 'Donetsk'),
    ('Dnepr', 'Dnepr'),
    ('Los Angeles', 'Los Angeles'),
    ('New York', 'New York'),
    ('San Francisco', 'San Francisco'),
    ('Sidney', 'Sidney'),
    ('Melbourne', 'Melbourne'),
)


class SignUpForm(UserCreationForm):
    birthday = forms.DateField(
        widget=extras.SelectDateWidget()
    )
    country = forms.ChoiceField(choices=COUNTRYES)
    city = forms.ChoiceField(choices=SITIES)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'birthday',
                  'city', 'country')
