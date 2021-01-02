from django.urls import path
from . import views
urlpatterns = [
    path("",views.frontpage,name="frontpage"),
    path('create_post/',views.create_post,name="create_post"),
    path('article/<username>/<title>/',views.details,name="details"),
    path('article/like/<title>/',views.like,name="like"),
    path('my_article/save/',views.save_fav,name="save_fav"),
    path('article/dislike/<title>/',views.dislike,name="dislike"),
    path("bookmarks/",views.bookmark,name="bookmark"),
    path("profile/",views.profile,name="profile"),
    path('aptitude/',views.aptitude,name="aptitude"),
    path("courses/",views.courses,name="courses"),
    

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
    path("company/information/<company>/",views.getcompanyinfo,name="getcompanyinfo"),
    path('jobs/',views.scrapper,name="scrapper"),
    path('jobs/listing/',views.show_jobs,name="show_jobs"),
    path('jobs/companies/',views.companies,name="companies"),
    path('jobs/companies/<name>/',views.company_info,name="company_info"),
    path("companies/",views.companywise,name="companywise"),
    path("companies/syllabus/",views.company_syllabus,name="syllabus"),
    path("companies/interview/",views.interview,name="interview"),
    path("companies/<name>/",views.company,name="company"),

    path("companies/<company>/<method>/<cat>/",views.get_company_mcq,name="mcqs"),
    path('companies/fetch/syllabus/<com>/<method>/',views.ajax_syllabus,name="ajax_syllabus"),

    path('mock_test/',views.mock_test,name="mock_test"),
    path('mock_test/test/<seriesid>/',views.taketest,name="taketest"),
    path('mock_test/<mockid>/',views.series,name="series"),
    path('mock_test/test_series/solution/<seriesid>/',views.series_solution,name="series_solution"),
]