from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class StandListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/stand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class StandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/stand_detail.html"
    model = CookieStand
    context_object_name = "cookie_stand"


class StandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/stand_update.html"
    model = CookieStand
    fields = "__all__"
    context_object_name = "cookie_stand"

    def get_success_url(self):
        return reverse_lazy('cookie_stand_detail', args=[str(self.id)])


class StandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/stand_create.html"
    model = CookieStand
    fields = "__all__"


class StandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/stand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("stand_list")
    context_object_name = "cookie_stand"
