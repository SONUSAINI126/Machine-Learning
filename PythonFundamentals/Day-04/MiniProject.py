'''Mini Project - OOPs Chat System'''
from datetime import datetime

# ----------------- Message Class -----------------
class Message:
    def __init__(self, sender, content, recipient=None):
        # If sender is None (system message), use a dummy object with name="System"
        if sender is None:
            class SystemSender:
                name = "System"
            sender = SystemSender()
        self.sender = sender
        self.content = content
        self.recipient = recipient  # None for public messages
        self.timestamp = datetime.now()

    def display(self):
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        if self.recipient:
            print(f"[{time_str}] {self.sender.name} -> {self.recipient.name}: {self.content}")
        else:
            print(f"[{time_str}] {self.sender.name}: {self.content}")


# ----------------- User Class -----------------
class User:
    def __init__(self, name):
        self.name = name
        self.chatrooms = []  # List of ChatRooms the user has joined

    def send_message(self, chatroom, content, recipient=None):
        if recipient and recipient not in chatroom.users:
            print(f"{recipient.name} is not in the chatroom '{chatroom.room_name}'!")
            return
        message = Message(self, content, recipient)
        chatroom.add_message(message)

    def join_chatroom(self, chatroom):
        if self not in chatroom.users:
            chatroom.add_user(self)
            self.chatrooms.append(chatroom)
            chatroom.broadcast(f"{self.name} has joined the chatroom.", sender=None)
            print(f"{self.name} joined the chatroom '{chatroom.room_name}'.")

    def leave_chatroom(self, chatroom):
        if self in chatroom.users:
            chatroom.remove_user(self)
            self.chatrooms.remove(chatroom)
            chatroom.broadcast(f"{self.name} has left the chatroom.", sender=None)
            print(f"{self.name} left the chatroom '{chatroom.room_name}'.")


# ----------------- ChatRoom Class -----------------
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def add_message(self, message):
        self.messages.append(message)

    def broadcast(self, content, sender=None):
        """Send a system or broadcast message to all users"""
        message = Message(sender, content)
        self.messages.append(message)

    def view_chat_history(self):
        print(f"\n--- Chat History in '{self.room_name}' ---")
        if not self.messages:
            print("No messages yet.")
        else:
            for msg in self.messages:
                msg.display()
        print("--- End of Chat History ---\n")


# ----------------- Example Usage -----------------

# Create multiple chatrooms
python_chat = ChatRoom("Python Room")
semester_chat = ChatRoom("Semester Room")

# Create users
user1 = User("Sonu")
user2 = User("Nikhil")
user3 = User("Riya")

# Users join chatrooms
user1.join_chatroom(python_chat)
user2.join_chatroom(python_chat)
user3.join_chatroom(semester_chat)
user1.join_chatroom(semester_chat)

# Users send public messages
user1.send_message(python_chat, "Hello Pythonistas!")
user2.send_message(python_chat, "Hi Sonu!")

# User sends a private message
user1.send_message(semester_chat, "Hey Riya, are you ready for the exam?", recipient=user3)

# View chat history
python_chat.view_chat_history()
semester_chat.view_chat_history()

# User leaves chatroom
user1.leave_chatroom(semester_chat)
