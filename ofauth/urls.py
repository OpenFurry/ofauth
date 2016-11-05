from django.conf.urls import (
    include,
    url,
)
from django.contrib import admin

urlpatterns = [
    url(r'^auth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
]
