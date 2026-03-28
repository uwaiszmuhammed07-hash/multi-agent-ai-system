from agents.base_agent import BaseAgent
from core.message_bus import Message

class ResearcherAgent(BaseAgent):
    def __init__(self, bus, memory):
        super().__init__(
            name="Researcher",
            role="Information Research Specialist",
            goal="Gather comprehensive information on any topic",
            bus=bus,
            memory=memory
        )

    def run(self, task: str = None) -> str:
        topic = self.memory.read("topic")
        plan  = self.memory.read("plan")
        print(f"[Researcher] Researching: {topic}")
        result = self._call_llm(
            system_prompt="You are an expert researcher. Provide comprehensive, accurate, well-structured research findings.",
            user_prompt=f"""Research the topic: '{topic}'

Based on this plan:
{plan}

Provide detailed findings including:
- Key concepts and definitions
- Current trends
- Main challenges and opportunities
- Future outlook"""
        )
        self.memory.write("research", result)
        self.bus.send(Message(
            sender="Researcher",
            recipient="Writer",
            content=result,
            task_id="task_002"
        ))
        print("[Researcher] Done")
        return result