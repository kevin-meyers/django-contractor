from django.urls import path
from kit.views import KitListView, KitDetailView


app_name='kit'
urlpatterns = [
    path('', KitListView.as_view(), name='list'),
    path('<str:slug>/', KitDetailView.as_view(), name='detail'),
]
