from django.urls import re_path,  include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^error$', views.error, name='error'),
    re_path(r'^tickets$', views.TicketListView.as_view(), name='tickets'),
    re_path(r'^ticket/(?P<pk>\d+)$', views.TicketDetailView.as_view(), name='ticket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
