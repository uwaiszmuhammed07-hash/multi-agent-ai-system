from agents.base_agent import BaseAgent
from core.message_bus import Message

class WriterAgent(BaseAgent):
    def __init__(self, bus, memory):
        super().__init__(
            name="Writer",
            role="Professional Content Writer",
            goal="Transform research into compelling content",
            bus=bus,
            memory=memory
        )

    def run(self, task: str = None) -> str:
        topic    = self.memory.read("topic")
        research = self.memory.read("research")
        plan     = self.memory.read("plan")
        print(f"[Writer] Writing article on: {topic}")
        result = self._call_llm(
            system_prompt="You are a professional content writer. Create engaging, clear, well-structured articles.",
            user_prompt=f"""Write a comprehensive article about: '{topic}'

Use this research:
{research}

Follow this plan:
{plan}

Structure with:
- Engaging introduction
- Well-organized sections with headers
- Key insights
- Strong conclusion"""
        )
        self.memory.write("article", result)
        self.bus.send(Message(
            sender="Writer",
            recipient="Reviewer",
            content=result,
            task_id="task_003"
        ))
        print("[Writer] Done")
        return result