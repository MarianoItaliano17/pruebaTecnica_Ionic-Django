import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Asignar un nombre de sala único
        self.room_name = "chat_room"
        self.room_group_name = f'chat_{self.room_name}'

        # Unir al grupo de la sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Aceptar la conexión WebSocket
        await self.accept()
        print(f"Conexión establecida con el WebSocket: {self.channel_name}")

    async def disconnect(self, close_code):
        # Salir de la sala cuando el cliente se desconecta
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"Conexión cerrada para el WebSocket: {self.channel_name}")

    async def receive(self, text_data):
        # Recibir el mensaje del cliente
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Guardar el mensaje en la base de datos de manera asincrónica
        await self.save_message(message)

        # Enviar el mensaje a todos los usuarios en la sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def save_message(self, message):
        # Función sincrónica que guarda el mensaje en la base de datos
        try:
            # Importar el modelo aquí para evitar problemas con el orden de importación
            from message.models import Message
            message_instance = await sync_to_async(Message.objects.create)(content=message)
            print(f"Mensaje guardado: {message_instance.content}")
        except Exception as e:
            print(f"Error al guardar el mensaje: {e}")

    async def chat_message(self, event):
        # Enviar el mensaje recibido a un cliente específico
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
        print(f"Mensaje enviado al WebSocket: {message}")
