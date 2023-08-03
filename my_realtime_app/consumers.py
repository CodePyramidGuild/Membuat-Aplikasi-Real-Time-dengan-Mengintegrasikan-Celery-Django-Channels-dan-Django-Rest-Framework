import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RealTimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data) 
        message = f"Data diterima: {data}"
        await self.send_message(message)

    async def send_message(self, message):
        await self.send(text_data=json.dumps({'message': message}))
