from django.urls import path
from . import views

urlpatterns = [
    path("",views.overview,name="overview"),
    path("create_mock/",views.create_mock,name="createmock"),
    path("create_mock/<id>/<company>/",views.add_questions,name="add_question"),
    path("create_mock/delete/<id>/<company>/<series>/",views.delete_series,name="delete_series"),
]