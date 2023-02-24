from content.views.content.animations.create_view.anima_create_type import AnimeCreateTypeView
from content.views.content.animations.create_view.anima_create_animations import AnimeCreateAnimationsView
from content.views.content.animations.create_view.anima_create_charester import AnimeCreateCharesterView
#-----------------------------
from content.views.content.animations.detail_view.anima_charester_detail_view import AnimaCharesterDetailView
from content.views.content.animations.detail_view.anime_anima_detail_view import AnimeAnimaDetailView
from content.views.content.animations.detail_view.anime_type_detail_view import AnimeTypeDetailView
#-----------------------------
from content.views.content.animations.list_view.animation_home_view import AnimationHomeView

__all__ = [
    'AnimationHomeView',
    # ---------------------------
    'AnimeTypeDetailView',
    'AnimeAnimaDetailView',
    'AnimaCharesterDetailView',
    # ---------------------------
    'AnimeCreateTypeView',
    'AnimeCreateAnimationsView',
    'AnimeCreateCharesterView',
]
