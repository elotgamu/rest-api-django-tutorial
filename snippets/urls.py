from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^snippets/$', views.GenericSnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.GenericSnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

# handle suffix in urls
urlpatterns = format_suffix_patterns(urlpatterns)
