from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from arenda import views

urlpatterns = [
                  url(r'^$', views.PlaceList.as_view(), name='index'),
                  url(r'^(?P<pk>[0-9]+)/$', views.PlaceDetail.as_view(), name='detail'),
    
                  url(r'^filter/(?P<kind_id>[0-9]+)', views.PlaceList.as_view(), name='filter'),
                  url(r'^page/(?P<page>[0-9]+)', views.PlaceList.as_view(), name='page'),
    
                  url(r'^about/$', views.About.as_view(), name='about'),
                  url(r'^contact/$', views.Contact.as_view(), name='contact'),
    
                  url(r'^admin/', admin.site.urls),
                  url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
