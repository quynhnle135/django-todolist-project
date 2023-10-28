from django.urls import path
from django.views.generic import RedirectView

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='home'),  # Redirect from the root URL
    path("login/", views.UserLogInView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("tasks/", views.TaskList.as_view(), name="task-list"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="task-detail"),
    path("tasks/create/", views.TaskCreate.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", views.TaskUpdate.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", views.TaskDelete.as_view(), name="task-delete"),
]