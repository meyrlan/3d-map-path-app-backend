"""
ASGI config for UvU project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

# from websocket_app.routing import websocket_urlpatterns  # noqa: 402 # isort:skip

# application = ProtocolTypeRouter(
#     {
#         "http": django_asgi_app,
#         "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
#     }
# )
