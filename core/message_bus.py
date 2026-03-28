from dataclasses import dataclass, field

@dataclass
class Message:
    sender:    str
    recipient: str
    content:   str
    task_id:   str
    metadata:  dict = field(default_factory=dict)

class MessageBus:
    def __init__(self):
        self._messages = []

    def send(self, message: Message):
        self._messages.append(message)

    def get_messages_for(self, recipient: str) -> list:
        return [m for m in self._messages if m.recipient == recipient]

    def get_all_messages(self) -> list:
        return self._messages