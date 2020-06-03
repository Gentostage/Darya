from django.urls import path
from .views import WorksListView, WorksDetailView, UpdateWorkImage, DestroyImage, CreateImage
from rest_framework.authtoken import views


app_name = "pict"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('works/', WorksListView.as_view()),
    path('works/<int:pk>', WorksDetailView.as_view()),
    path('works/image/<int:pk>', UpdateWorkImage.as_view()),
    path('picture/<int:pk>', DestroyImage.as_view()),
    path('picture/', CreateImage.as_view()),
    # path('auth/', views.obtain_auth_token),
]