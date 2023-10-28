from django.views import generic
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


class UserLogInView(LoginView):
    template_name = "base/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("task-list")


class UserRegisterView(generic.FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "base/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__startswith=search_input)

        context["search_input"] = search_input
        return context


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "base/task_detail.html"


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "base/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ["title", "description", "completed"]
    template_name = "base/task_update_form.html"
    success_url = reverse_lazy("task-list")

