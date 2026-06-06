# ================================================================
#  🤖  ZARA  -  Your AI Buddy
#  GoYang Workshop  |  Session 1: Streamlit + Groq Basics
# ================================================================
#
#  What we learn in Session 1:
#  ✅ Connecting to a real AI using Groq API
#  ✅ Building a chat UI with Streamlit
#  ✅ Sending messages and getting replies
#
#  NOTE: No memory yet! Bot forgets after every message.
#        Memory comes in Session 4! 🧠
#
#  SETUP:  pip install streamlit groq python-dotenv
#  RUN:    streamlit run session1.py
# ================================================================

# ── STEP 1: IMPORTS ───────────────────────────────────────────────
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# ── STEP 2: YOUR SETTINGS ─────────────────────────────────────────
API_KEY  = os.environ.get("GROQ_API_KEY")   # Loaded from .env file
BOT_NAME = "Zara"                            # Your bot's name
MODEL    = "llama-3.3-70b-versatile"         # The AI brain we're using

# ── STEP 3: PAGE SETUP ────────────────────────────────────────────
st.set_page_config(
    page_title = f"{BOT_NAME} — AI Chatbot",
    page_icon  = "🤖",
    layout     = "centered",
)

# ── STEP 4: SIDEBAR ───────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")
    st.markdown(f"**Bot:** {BOT_NAME}")
    st.markdown(f"**Model:** {MODEL}")
    st.markdown("---")
    st.markdown("**Codeyoung Workshop** • Session 1")
    st.markdown("Powered by [Groq](https://groq.com) + LLaMA 3 🦙")

# ── STEP 5: CHAT DISPLAY ──────────────────────────────────────────
st.title(f"🤖 {BOT_NAME}")
st.caption("Powered by Groq + LLaMA 3 • GoYang Workshop 🚀")

# Show welcome message
st.info(f"👋 Hi! I'm **{BOT_NAME}**, your AI buddy. Ask me anything!")

# ── STEP 6: INPUT + AI RESPONSE ───────────────────────────────────
# ⚠️ No memory yet — bot only sees your current message!

user_input = st.chat_input(f"Message {BOT_NAME}...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            try:
                # Connect to Groq
                client = Groq(api_key=API_KEY)

                # Send ONLY the current message — no history!
                response = client.chat.completions.create(
                    model      = MODEL,
                    messages   = [{"role": "user", "content": user_input}],
                    max_tokens = 400,
                )

                # Show the reply
                reply = response.choices[0].message.content
                st.markdown(reply)

            except Exception as error:
                st.error(f"❌ Error: {error}")
