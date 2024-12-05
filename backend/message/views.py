from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from django.utils import timezone
from rest_framework import status
from .serializer import MessageSerializer

@api_view(['GET'])
def get_message(request):
    messages = Message.objects.all()  # Obtener todos los mensajes
    serializer = MessageSerializer(messages, many=True)  # Serializar los mensajes
    return Response(serializer.data)  # Retornar los mensajes en formato JSON

@api_view(['POST'])
def create_message(request):
    if request.method == 'POST':
        message_content = request.data.get('message')

        # Crear un nuevo mensaje en la base de datos
        if message_content:
            message = Message.objects.create(
                content=message_content,
                timestamp=timezone.now()
            )
            return Response({"message": "Message created successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Message content is required"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
        serializer = MessageSerializer(message, data=request.data, partial=True)  # partial=False significa reemplazo total
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Message updated successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
        message.delete()
        return Response({"message": "Message deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND)