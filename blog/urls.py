from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index), FBV 방식을 사용할때 씀
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.single_post_page),

]