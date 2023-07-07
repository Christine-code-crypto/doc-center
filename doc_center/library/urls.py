from django.urls import path, re_path

from . import views

app_name = "library"

urlpatterns =[
    path("", views.index, name="index"),
    # create a document
    path("new-document", views.newDocument, name="new-document"),
    # issue a document
    re_path(r'^issue-document/(?P<pk>\d+)', views.issueDocument, name="issue-document"),
    # mark document as returned
    re_path(r'^return-book/(?P<pk>\d+)', views.returnDocument, name="return-book"),
    # document by id
    re_path(r'^document/(?P<pk>\d+)', views.singleDocument, name="document"),
     # documents by category
    path("search", views.documentsByCategory, name="search-documents"),
    # update document
    re_path(r'^update/(?P<pk>\d+)', views.updateDocument, name="update-document"),
    # delete document
    re_path(r'^delete/(?P<pk>\d+)', views.deleteDocument, name="delete-document")
]