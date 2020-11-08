from django.urls import path
from . import views
urlpatterns = [
    path("",views.frontpage,name="frontpage"),
    path('create_post/',views.create_post,name="create_post"),
    path('article/<username>/<title>/',views.details,name="details"),
    path('article/like/',views.like,name="like"),
    path('my_article/save/',views.save_fav,name="save_fav"),
    path('article/dislike/',views.dislike,name="dislike"),
    path("bookmarks/",views.bookmark,name="bookmark"),
    path("profile/",views.profile,name="profile"),
    path('aptitude/',views.aptitude,name="aptitude"),
    path("courses/",views.courses,name="courses"),
    path("coding/",views.coding,name="coding"),

    path('aptitude/quants/',views.quants,name="quants"),
    path('aptitude/verbal/',views.verbal,name="verbal"),
    path('aptitude/logical/',views.logical,name="logical"),
    path('aptitude/interpretation/',views.interpretation,name="interpretation"),
    path("aptitude/contribute/",views.contribute,name="aptitude_contribute"),
    path("aptitude/<method>/questions/<topic>/",views.questions,name="questions"),
    
    path("aptitude/question/validate/<ids>/<option>",views.validate,name="validate"),

    path("lisitng/",views.listing,name="listing"),
    path('hashtags/<topic>/',views.hashtags,name="hashtags"),

    path("discussion/",views.discussion,name="discussion"),
    path("discussion/<ques_id>/",views.discussion_anwser,name="discussion_anwser"),

    path('scrapper/',views.scrapper,name="scrapper")
    
]