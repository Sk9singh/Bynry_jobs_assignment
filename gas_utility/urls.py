from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service_requests.views import ServiceRequestViewSet

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

