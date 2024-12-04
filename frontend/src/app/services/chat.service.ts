import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  private socket$: WebSocketSubject<any> | null = null;
  private messageSubject = new BehaviorSubject<string[]>([]);

  constructor() {}

  connect() {
    if (!this.socket$) {
      this.socket$ = new WebSocketSubject('ws://localhost:8000/ws/chat/');

      this.socket$.subscribe(
        message => {
          this.messageSubject.next([...this.messageSubject.getValue(), message]);
        },
        err => console.error('Error WebSocket:', err)
      );
    }
  }

  sendMessage(message: string) {
    if (this.socket$) {
      this.socket$.next({ message });
    }
  }

  getMessages() {
    return this.messageSubject.asObservable();
  }
}
