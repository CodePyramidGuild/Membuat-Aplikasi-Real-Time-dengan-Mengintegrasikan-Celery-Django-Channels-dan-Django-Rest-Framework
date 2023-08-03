from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from realtime_app import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/realtime/', consumers.RealTimeConsumer.as_asgi()), 
    ]),
})