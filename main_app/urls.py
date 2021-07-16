from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('records/', views.record_index, name="index"),
    path('records/<int:record_id>/', views.record_detail, name="detail"),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/',
         views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/',
         views.RecordDelete.as_view(), name='records_delete'),
    path('records/<int:record_id>/add_artist/',
         views.add_artist, name='add_artist'),
    path('records/<int:record_id>/assoc_artist/<int:artist_id>',
         views.assoc_artist, name="assoc_artist"),
]
