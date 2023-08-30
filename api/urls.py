from rest_framework import routers

from .views import PostListCreateView, CommentListCreateView, LikeListCreateView

router = routers.DefaultRouter()

router.register(r'posts', PostListCreateView)
router.register(r'comments', CommentListCreateView)
router.register(r'likes', LikeListCreateView)





# urlpatterns = router.urls
