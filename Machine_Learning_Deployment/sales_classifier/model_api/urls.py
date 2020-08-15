from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('model_api', views.StatusView)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('status/', views.winloss),
    path('', views.myform, name ='myform'),
]