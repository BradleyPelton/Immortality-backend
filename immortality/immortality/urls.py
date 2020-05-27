from django.contrib import admin
from django.urls import path
# from django.urls import include

from rest_framework.urlpatterns import format_suffix_patterns

from person.views import PersonList, PersonDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/person/', PersonList.as_view()),
    path('api/person/<int:id>/', PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
