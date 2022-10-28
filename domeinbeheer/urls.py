# domeinbeheer/urls.py

# django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('users.urls', namespace="users")),
  path('', include('domeinen.urls', namespace="domeinen")),
  # debug urls
  #path("__debug__", include('debug_toolbar.urls')),
]
