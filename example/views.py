from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.forms import modelform_factory

from . import forms, models


class ChildCreationView(CreateView):
    template_name = "example/home.html"
    success_url = reverse_lazy("home")
    form_class = forms.ChildCreationForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


home = ChildCreationView.as_view()


def parent_creation_view(request):
    if request.method == "POST":
        form = forms.ParentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            response = render(
                request,
                "partials/parent/create-success.html",
                {
                    "form": modelform_factory(
                        models.Child,
                        fields=("parent",),
                    )()
                },
            )
            response["HX-Trigger-After-Swap"] = "modal-close"
            return response
    else:
        form = forms.ParentCreationForm()

    response = render(request, "partials/parent/create.html", {"form": form})
    response["HX-Trigger-After-Swap"] = "modal-open"

    return response
