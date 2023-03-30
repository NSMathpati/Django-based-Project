from django.urls import path, include
from rest_framework import routers
from .views import BookingViewSet, MenuitemsView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('menu-items/', MenuitemsView.as_view()),
    path('menu-items/<int:pk>/', MenuitemsView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
