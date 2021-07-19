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
    path('records/<int:record_id>/assoc_artist/',
         views.assoc_artist, name="assoc_artist"),
    # format paths
    path('records/<int:record_id>/add_format/',
         views.add_format, name='add_format'),
    path('records/<int:record_id>/delete_format/<int:format_id>',
         views.delete_format, name='delete_format'),
    #  artist paths
    path('artists/', views.ArtistList.as_view(), name="artist_index"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artists/<int:pk>/update/',
         views.ArtistUpdate.as_view(), name='artist_update'),
    path('artists/<int:pk>/delete/',
         views.ArtistDelete.as_view(), name='artist_delete'),
]
