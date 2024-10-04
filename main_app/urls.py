from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("dawgs/", views.dawg_index, name="dawg-index"),
    path("dawgs/<int:dawg_id>/", views.dawg_detail, name="dawg-detail"),
    path("dawgs/create/", views.DawgCreate.as_view(), name="dawg-create"),
    path("dawgs/<int:pk>/update/", views.DawgUpdate.as_view(), name="dawg-update"),
    path("dawgs/<int:pk>/delete/", views.DawgDelete.as_view(), name="dawg-delete"),
    path("dawgs/<int:dawg_id>/add-feeding/", views.add_feeding, name="add-feeding"),
    path("toys/create/", views.ToyCreate.as_view(), name="toy-create"),
    path("toys/<int:pk>/", views.ToyDetail.as_view(), name="toy-detail"),
    path("toys/", views.ToyList.as_view(), name="toy-index"),
    path("toys/<int:pk>/update/", views.ToyUpdate.as_view(), name="toy-update"),
    path("toys/<int:pk>/delete/", views.ToyDelete.as_view(), name="toy-delete"),
    path('dawgs/<int:dawg_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    path('dawgs/<int:dawg_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),
]
