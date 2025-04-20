from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('livre/creer/',livre_create, name = 'creer_livre'),
    path('',liste_livres, name= 'liste_livres'),
    path('signup/', signup, name = 'signup'),
    path('livre/<int:pk>/', livre_detail, name = 'detail_livre'),
    path('livre/<int:pk>/modifier/', livre_update, name = 'modifier_livre'),
    path('livre/<int:pk>/supprimer/', livre_delete, name = 'supprimer_livre'),
    path('summernote/', include('django_summernote.urls')),
    path('logout/', views.custom_logout, name='logout'),
]