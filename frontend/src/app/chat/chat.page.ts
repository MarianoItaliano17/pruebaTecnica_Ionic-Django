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
    this.chatService.connect();
    this.chatService.getMessages().subscribe(messages => {
      this.messages = messages;
    });
  }

  sendMessage() {
    if (this.message.trim()) {
      this.chatService.sendMessage(this.message);
      this.message = '';
    }
  }
}
