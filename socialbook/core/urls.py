from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/add/', views.addPost, name='addPost'),
    path('', views.postt, name='postt'),
    path('post/view/<int:pk>', views.postDetail, name='postDetail'),
    path('post/delete/<int:pk>', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>', views.editPost, name='editPost'),
    path('sign-up/', views.signUp, name='signUp'),
    path('log-in/', views.logIn, name='logIn'),
    path("logout/", views.logoutUser, name= "logoutUser"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)