"""
URL'S main project.
"""
from django.contrib import admin
from django.urls import path, include
from api_challenge import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# ROUTERS API
router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'articles', views.ArticleViewSet)

# URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', include(router.urls)),
    path('api/login/', obtain_auth_token),
    path('api/sign-up/', views.SignUpViewSet.as_view()),
    path('api/articles/', views.ArticlesViewSet.as_view()),
]
