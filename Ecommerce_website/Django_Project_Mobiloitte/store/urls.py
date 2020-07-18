from django.urls import path
from store import views


urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.signup),
    path('login', views.login),
    # path('googlemap', views.googlemap),
    path('nearest_restaurants', views.nearest_restaurants)

]