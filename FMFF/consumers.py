import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_id = data.get('messageId')

        if data.get('type') == 'notification':
            # Handle the notification logic (e.g., send a message to the user)
            await self.send(text_data=json.dumps({
                'type': 'notification',
                'message': 'A new post has been made!',
                'messageId': message_id,
            }))

    async def handle_acknowledgment(self, message_id):
        # Handle acknowledgment logic (e.g., mark the message as received)
        print(f"Message with ID {message_id} acknowledged by client {self.scope['user']}")