from django.urls import include, path

urlpatterns = [
    path("client/", include(("api.v2.client.urls", "client"), namespace="client")),
]
