from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, CategoryViewSet, CreateUserView, ListUserView, LoginUserView, ProfileViewSet

# Viewsetsで定義したものはroutersで宣言する
router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileViewSet)

# generics系はurlpatternsに入れる
urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls))
]
