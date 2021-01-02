from django.urls import path
from . import views
urlpatterns = [
    path('',views.compiler,name="compiler"),
    path('test/',views.test,name="test"),
    path('temp/<id>/',views.temp,name="temp"),
    path('save/<id>/',views.save,name="save"),
    path('savefile/<id>/',views.savefile,name="savefile"),
    path('playground/',views.playground,name="playground"),
    path('playground/delete/<id>/',views.delete,name="delete"),
    path('playground/edit/<id>/',views.edit,name="edit"),
    path('playground/<var>/',views.emptyplay,name="emptyplay"),
    path('playground/frontend/html/',views.html,name="html"),
    path('playground/frontend/editor/',views.editor,name="editor")

]