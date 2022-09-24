from django.contrib.auth.views import LoginView
from django.urls import include, path, reverse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


class APILoginView(LoginView):
    template_name = "admin/login.html"
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse("api:swagger")


class MobileSpectacularAPIView(SpectacularAPIView):
    urlconf = "api.urls"


urlpatterns = [
    path("v2/", include(("api.v2.urls", "v2"), namespace="v2")),
    # Swagger.
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger",
    ),
]
