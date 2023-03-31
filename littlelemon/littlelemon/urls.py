from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant/booking/', include(router.urls)),
    path('restaurant/menu/', include('restaurant.urls')),
    path('api-token-auth/', obtain_auth_token),
]
