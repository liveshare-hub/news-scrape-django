from django.urls import path

from .views import scrape_news, home


urlpatterns = [
    path('', home, name='home'),
    path('scrape/', scrape_news, name='scrape'),
]
