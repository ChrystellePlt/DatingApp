from django.conf.urls import url
from dating_app import views


urlpatterns = [
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private)
]