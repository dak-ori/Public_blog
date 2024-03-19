from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('', views.index), - 목록페이지
    # path('<int:pk>/', views.single_post_page), - 상세페이지

]