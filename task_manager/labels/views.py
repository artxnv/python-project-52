from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.mixins import MyLoginRequiredMixin
from .models import Label
from .forms import LabelForm


class LabelListView(MyLoginRequiredMixin, ListView):
    template_name = "labels/list.html"
    model = Label
    context_object_name = "labels"
    extra_context = {"header": _("Labels")}


class LabelCreateView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "form.html"
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy("labels")
    success_message = _("Label is successfully created")
    extra_context = {
        "header": _("Create label"),
        "button_text": _("Create"),
    }


class LabelUpdateView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "form.html"
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy("labels")
    success_message = _("Label is successfully changed")
    extra_context = {
        "header": _("Change label"),
        "button_text": _("Change"),
    }


class LabelDeleteView(
    MyLoginRequiredMixin, SuccessMessageMixin, DeleteView
):
    template_name = "delete.html"
    model = Label
    success_url = reverse_lazy("labels")
    success_message = _("Label is successfully deleted")
    protected_message = _("Unable to delete a label because it is in use")
    protected_url = reverse_lazy("labels")
    extra_context = {
        "header": _("Delete label"),
        "button_text": _("Yes, delete"),
    }

    def post(self, request, *args, **kwargs):
        if self.get_object().labels.all().exists():
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
        else:
            messages.success(request, self.success_message)
            return super().delete(request, *args, **kwargs)
