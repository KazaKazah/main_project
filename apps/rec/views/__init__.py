from apps.rec.views.list_view.r_home_view import RHomeView
# ----------------------------------------------------------
from apps.rec.views.detail_view.r_c_d_detail_view import RCDDetailView
from apps.rec.views.detail_view.r_c_detail_view import RCDetailView
from apps.rec.views.detail_view.r_detail_view import RDetailView
# ---------------------------------------------------------
from apps.rec.views.create_view.r_create_view import RCreateView
from apps.rec.views.create_view.r_c_create_view import RCCreateView
from apps.rec.views.create_view.r_c_d_create_view import RCDCreateView
# -----------------------------------------------------------------------
from apps.rec.views.update_view.r_update import RUpdateView

__all__ = [
    'RHomeView',
    # --------------------
    'RDetailView',
    'RCDetailView',
    'RCDDetailView',
    # ---------------------
    'RCreateView',
    'RCCreateView',
    'RCDCreateView',
    # ------------------------
    'RUpdateView',
]