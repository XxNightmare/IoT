from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from applications.user import views as user_views, backend as user_backend

urlpatterns = [
    path('', user_views.home, name='home'),
    # -------------------------------------------------------------------------------------
    # VIEWS
    # -------------------------------------------------------------------------------------
    path('principal/', user_views.principal, name='principal'),
    path('logout/', user_views.logout_user, name='logout'),
    # -------------------------------------------------------------------------------------
    # BACKEND
    # -------------------------------------------------------------------------------------
    path('give_response/', user_backend.give_response, name='give_response'),
    path('get_conversacion/', user_backend.get_conversacion, name='get_conversacion'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
