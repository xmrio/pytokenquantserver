from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
            URLRouter(
                    chat.routing.websocket_urlpatterns
                )
        ),
    })