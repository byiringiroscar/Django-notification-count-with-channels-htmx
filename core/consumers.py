import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.GROUP_NAME = "new-notifications"
        async_to_sync(self.channel_layer.group_add)(self.GROUP_NAME, self.channel_name)
        self.accept()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.GROUP_NAME, self.channel_name)

    def notification_message_func(self, event):
        html = get_template('partials/notification_counter.html').render(
            context = {'num': event['message']}
            )
        self.send(text_data=html)

