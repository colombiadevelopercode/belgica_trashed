from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages, name='pages'),
    path('send/', views.send, name='send'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('upload_contact/', views.upload_contact, name='upload_contact'),

    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]