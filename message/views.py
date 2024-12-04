from django.shortcuts import render
from .serializers import MessageSerializer
from rest_framework import generics, permissions
from .models import Message
from django.shortcuts import render
from .serializers import MessageSerializer
from rest_framework import generics, permissions
from .models import Message
from langchain.memory import ConversationBufferMemory
from .utils import add_to_memory, get_response



class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        question = serializer.validated_data['question']
        user = self.request.user
        
        # hanlde model
        memory = ConversationBufferMemory()
        
        old_messages = self.get_queryset()
        old_messages = [[message.question,message.response] for message in old_messages]
        
        for message in old_messages:
            memory = add_to_memory(memory=memory,user_input={"input":message[0]}, response={"response":message[1]})
        

        ai_reply = get_response(question, memory.chat_memory)
        print(ai_reply)
        serializer.save(response=ai_reply)