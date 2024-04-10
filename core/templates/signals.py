from core.models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Notification)
def notification_handler(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notification',
            {
                'type': 'notification_message',
                'message': instance.count_not
            }
        )