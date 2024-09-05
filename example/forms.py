from django import forms

from . import models


class ParentCreationForm(forms.ModelForm):
    class Meta:
        model = models.Parent
        fields = ("name",)


class ChildCreationForm(forms.ModelForm):
    class Meta:
        model = models.Child
        fields = ("name", "parent")
