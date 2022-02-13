from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing as route

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            route.websocket_urlpatterns
        )
    ),
})