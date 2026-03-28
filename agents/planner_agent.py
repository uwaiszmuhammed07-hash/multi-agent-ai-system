from agents.base_agent import BaseAgent
from core.message_bus import Message

class PlannerAgent(BaseAgent):
    def __init__(self, bus, memory):
        super().__init__(
            name="Planner",
            role="Strategic Task Planner",
            goal="Break down topics into clear research and writing tasks",
            bus=bus,
            memory=memory
        )

    def run(self, topic: str) -> str:
        print(f"[Planner] Planning tasks for: {topic}")
        result = self._call_llm(
            system_prompt="You are a strategic planner for a multi-agent AI system. Break down topics into clear tasks for a Researcher, Writer, and Reviewer agent.",
            user_prompt=f"""Create a detailed task plan for the topic: '{topic}'

Format your response as:
RESEARCH TASK: [what the researcher should find]
WRITING TASK: [what the writer should produce]
REVIEW TASK: [what the reviewer should check]
OVERALL GOAL: [the final deliverable]"""
        )
        self.memory.write("plan", result)
        self.memory.write("topic", topic)
        self.bus.send(Message(
            sender="Planner",
            recipient="Researcher",
            content=result,
            task_id="task_001"
        ))
        print("[Planner] Done")
        return result