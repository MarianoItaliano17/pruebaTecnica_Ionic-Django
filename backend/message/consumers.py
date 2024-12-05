# messages/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Aquí asignamos un nombre de sala único, puedes modificarlo como gustes
        self.room_name = "chat_room"
        self.room_group_name = f'chat_{self.room_name}'

        # Unir a la sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Aceptar la conexión WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Salir de la sala cuando se desconecta
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Recibir mensaje del cliente y enviarlo a todos los conectados
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Enviar el mensaje a todos los usuarios en la sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Enviar mensaje a un cliente específico
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
