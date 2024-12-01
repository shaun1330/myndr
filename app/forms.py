from django import forms
from app.models import Tag, Category


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class NewTaskForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Tags'
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select,
        label='Category'
    )


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

