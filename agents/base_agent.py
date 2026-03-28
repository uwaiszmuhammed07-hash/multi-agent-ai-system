import os
from groq import Groq
from dotenv import load_dotenv
from core.message_bus import MessageBus, Message
from core.memory import SharedMemory

load_dotenv()

class BaseAgent:
    def __init__(self, name: str, role: str, goal: str,
                 bus: MessageBus, memory: SharedMemory):
        self.name   = name
        self.role   = role
        self.goal   = goal
        self.bus    = bus
        self.memory = memory
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            max_tokens=1024
        )
        return response.choices[0].message.content

    def run(self, task: str) -> str:
        raise NotImplementedError("Each agent must implement run()")