import streamlit as st
from dotenv import load_dotenv
from core.message_bus import MessageBus
from core.memory import SharedMemory
from agents.planner_agent import PlannerAgent
from agents.researcher_agent import ResearcherAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent
import os

load_dotenv()
print("KEY FOUND:", os.getenv("ANTHROPIC_API_KEY"))

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Collaborative Multi-Agent System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Collaborative Multi-Agent System")
st.markdown("Enter a topic. The **Planner → Researcher → Writer → Reviewer** agents will work together.")

# ── Input ─────────────────────────────────────────────────────
topic = st.text_input("Enter your topic", placeholder="e.g. AI in healthcare")

if st.button("🚀 Run Agents", type="primary"):
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        # ── Setup ──────────────────────────────────────────────
        bus    = MessageBus()
        memory = SharedMemory()

        planner    = PlannerAgent(bus, memory)
        researcher = ResearcherAgent(bus, memory)
        writer     = WriterAgent(bus, memory)
        reviewer   = ReviewerAgent(bus, memory)

        # ── Run pipeline with live status ─────────────────────
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("🔄 Agent Activity")

            with st.status("Running agents...", expanded=True) as status:

                st.write("📋 Planner is creating a task plan...")
                plan = planner.run(topic)
                st.write("✅ Planner done")

                st.write("🔍 Researcher is gathering information...")
                research = researcher.run()
                st.write("✅ Researcher done")

                st.write("✍️ Writer is creating the article...")
                article = writer.run()
                st.write("✅ Writer done")

                st.write("🔎 Reviewer is reviewing and polishing...")
                final = reviewer.run()
                st.write("✅ Reviewer done")

                status.update(label="✅ All agents completed!", state="complete")

        with col2:
            st.subheader("📄 Results")

            tab1, tab2, tab3, tab4 = st.tabs([
                "📋 Plan", "🔍 Research", "✍️ Article", "✅ Final Output"
            ])

            with tab1:
                st.markdown(memory.read("plan"))

            with tab2:
                st.markdown(memory.read("research"))

            with tab3:
                st.markdown(memory.read("article"))

            with tab4:
                st.success("Final reviewed and polished output:")
                st.markdown(memory.read("final_output"))

                st.download_button(
                    label="⬇️ Download Final Output",
                    data=memory.read("final_output"),
                    file_name=f"{topic.replace(' ', '_')}_output.txt",
                    mime="text/plain"
                )

        # ── Message log ───────────────────────────────────────
        with st.expander("📨 View Agent Message Log"):
            for msg in bus.get_all_messages():
                st.markdown(f"**{msg.sender}** → **{msg.recipient}** (Task: `{msg.task_id}`)")
                st.caption(msg.content[:200] + "...")
                st.divider()