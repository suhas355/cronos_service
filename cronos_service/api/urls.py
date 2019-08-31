from django.conf.urls import url, include

from cronos_service.api.views import HomeView

app_name = 'api'
urlpatterns = [
        url(r'home', HomeView.as_view(), name="home"),
                ]
