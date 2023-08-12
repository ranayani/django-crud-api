from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    #path("project", views.project, name="project"),
    path("",views.ListTaskAPIView.as_view(),name="task_list"),
    path("create/", views.CreateTaskAPIView.as_view(),name="task_create"),
    path("update/<int:pk>/",views.UpdateTaskAPIView.as_view(),name="update_task"),
    path("delete/<int:pk>/",views.DeleteTaskAPIView.as_view(),name="delete_task"),
]