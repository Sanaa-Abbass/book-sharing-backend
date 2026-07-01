from django.urls import path
from .views import BookListCreateView

from .views import BookViewSet

router = DefaultRouter()

router.register(
    "",
    BookViewSet,
    basename="books"
)

urlpatterns = [

    path(
        "",
        include(router.urls)
    ),
]
