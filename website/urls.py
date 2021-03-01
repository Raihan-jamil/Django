from django.contrib import admin
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path(r'^music/', include('music.urls')),
]
