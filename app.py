import streamlit as st
from agents import Runner
from inv_agents.coordinator import investment_mentor
import asyncio

runner = Runner()

st.set_page_config(page_title="Investment Mentor", layout="centered")
st.title("💼 Investment Mentor for Beginners")

# Store chat history as a list of dicts
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "user", "content": "Hi! I'm new to investing. Can you help me?"}
    ]

user_input = st.text_input("You:", key="user_input")

if st.button("Send") and user_input:
    async def get_response():
        # Add user message as a dict
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        result = await runner.run(investment_mentor, st.session_state.chat_history)
        # Add mentor response as a dict
        st.session_state.chat_history.append({"role": "assistant", "content": result.final_output})
        return result.final_output

    output = asyncio.run(get_response())
    st.write(f"**Mentor:** {output}")

# Display conversation
st.markdown("### 💬 Chat History")
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Mentor:** {msg['content']}")