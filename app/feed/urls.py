from django.urls import path, include
from rest_framework_nested import routers

from . import views


router = routers.SimpleRouter()
router.register(r"posts", views.PostViewSet)

comment_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
comment_router.register(
    r"comments", views.CommentViewSet, basename="post-comment"
)


urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(comment_router.urls)),
]
