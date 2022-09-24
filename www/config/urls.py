from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.templatetags.static import static as static_url
from django.urls import include, path
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url=static_url("favicon.ico"))

urlpatterns = [
    path("core/", include(("core.urls", "core"), namespace="core")),
    path("api/", include(("api.urls", "api"), namespace="api")),
    # path(
    #     "m/",
    #     include(
    #         ("mobile_redirects.urls", "mobile-redirects"), namespace="mobile-redirects"
    #     ),
    # ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add admin URLs last.
urlpatterns.append(path("", admin.site.urls))
