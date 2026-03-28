from agents.base_agent import BaseAgent
from core.message_bus import Message

class ReviewerAgent(BaseAgent):
    def __init__(self, bus, memory):
        super().__init__(
            name="Reviewer",
            role="Quality Assurance Reviewer",
            goal="Review and improve the final content",
            bus=bus,
            memory=memory
        )

    def run(self, task: str = None) -> str:
        topic   = self.memory.read("topic")
        article = self.memory.read("article")
        print(f"[Reviewer] Reviewing article on: {topic}")
        result = self._call_llm(
            system_prompt="You are a senior editor. Review content for accuracy, clarity and quality. Provide an improved final version.",
            user_prompt=f"""Review and improve this article about '{topic}':

{article}

Please:
1. Fix any gaps or inaccuracies
2. Improve clarity and flow
3. Provide a FINAL POLISHED VERSION
4. End with a REVIEW SUMMARY of improvements made"""
        )
        self.memory.write("final_output", result)
        self.bus.send(Message(
            sender="Reviewer",
            recipient="System",
            content=result,
            task_id="task_004"
        ))
        print("[Reviewer] Done")
        return result