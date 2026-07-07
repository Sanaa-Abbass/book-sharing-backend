from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BorrowRequestViewSet

router = DefaultRouter()

router.register(
    "",
    BorrowRequestViewSet,
    basename="borrow"
)

urlpatterns = [
    path(
        "",
        include(router.urls)
    )
]
