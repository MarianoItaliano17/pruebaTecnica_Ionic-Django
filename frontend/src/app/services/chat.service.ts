import { Injectable, OnDestroy } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChatService implements OnDestroy {
  private socket$: WebSocketSubject<any> | null = null;
  private messageSubject = new BehaviorSubject<string[]>([]);

  constructor() {}

  // Método para establecer la conexión WebSocket
  connect() {
    if (!this.socket$) {
      this.socket$ = new WebSocketSubject('ws://localhost:8000/ws/chat/');

      // Suscribirse al WebSocket
      this.socket$.subscribe(
        (message: any) => {
          // Asegúrate de que el mensaje recibido tenga la propiedad 'message'
          if (message && message.message) {
            this.messageSubject.next([...this.messageSubject.getValue(), message.message]);
          }
        },
        (err) => {
          console.error('Error WebSocket:', err);
          // Intentar reconectar después de 5 segundos en caso de error
          setTimeout(() => this.connect(), 5000);
        },
        () => {
          console.log('WebSocket closed');
          // Intentar reconectar después de 5 segundos si la conexión se cierra
          setTimeout(() => this.connect(), 5000);
        }
      );
    }
  }

  // Método para enviar un mensaje al servidor WebSocket
  sendMessage(message: string) {
    if (this.socket$) {
      this.socket$.next({ message });  // Enviar el mensaje al servidor WebSocket
    }
  }

  // Método para obtener los mensajes recibidos como observable
  getMessages(): Observable<string[]> {
    return this.messageSubject.asObservable();  // Retorna el observable de mensajes
  }

  // Método que se llama cuando el servicio se destruye
  ngOnDestroy() {
    if (this.socket$) {
      this.socket$.complete();  // Cerrar la conexión WebSocket al destruir el servicio
    }
  }
}
