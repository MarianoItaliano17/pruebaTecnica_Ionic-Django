import { Component, OnInit } from '@angular/core';
import { ChatService } from '../services/chat.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.page.html',
  styleUrls: ['./chat.page.scss'],
})
export class ChatPage implements OnInit {
  messages: string[] = [];
  message: string = '';

  constructor(private chatService: ChatService) {}

  ngOnInit() {
      // Conectar al WebSocket cuando se inicializa el componente
      this.chatService.connect();

      // Suscribirse a los mensajes recibidos
      this.chatService.getMessages().subscribe((messages) => {
        this.messages = messages;  // Actualizar la lista de mensajes
      });
  }

  ngOnDestroy() {
    // Asegurarse de que la conexión WebSocket se cierre cuando se destruye el componente
    // Si es necesario, puedes cerrar la conexión desde el servicio.
    this.chatService.ngOnDestroy();
  }

  sendMessage() {
    if (this.message.trim()) {
      // Enviar el mensaje a través del servicio WebSocket
      this.chatService.sendMessage(this.message);
      this.message = '';  // Limpiar el campo de texto después de enviar el mensaje
    }
  }
}
