from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

DefaultRouter()
"""
/articles/ - Get/list
/articles/ - Post/create
/articles/<int:pk>/ - GET/Read
/articles/<int:pk>/ - DELETE/Read
/articles/<int:pk>/ - PUT/Read
"""
router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]
