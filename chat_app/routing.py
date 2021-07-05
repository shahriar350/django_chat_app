from django.urls import path, re_path
from . import consumers

ws_patterns = [
    re_path(r'ws/user/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
