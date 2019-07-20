from django.urls import path
from .views import WorksView, SingleWorksView


app_name = "pict"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('works/', WorksView.as_view()),
    path('works/<int:pk>', SingleWorksView.as_view()),
]