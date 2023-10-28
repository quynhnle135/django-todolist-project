from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.UserLogInView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("", views.TaskList.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskDetail.as_view(), name="task-detail"),
    path("create/", views.TaskCreate.as_view(), name="task-create"),
    path("<int:pk>/update", views.TaskUpdate.as_view(), name="task-update"),
    path("<int:pk>/delete", views.TaskDelete.as_view(), name="task-delete"),
]