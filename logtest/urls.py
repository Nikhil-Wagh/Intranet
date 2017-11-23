from django.conf.urls import url,include
from django.contrib import admin
from logtest import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls',namespace='accounts')),
    url(r'^feed/', include('feed.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
