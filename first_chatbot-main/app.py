import streamlit as st
import os
from pathlib import Path
from chat_interface import ChatInterface
from chat_history import ChatHistory
from styles import apply_custom_styles

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ChatHistory()

def main():
    st.set_page_config(
        page_title="Ai chatbot🤖",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    apply_custom_styles()
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        st.title("✨ Settings")
        
        # Theme selector
        theme = st.selectbox(
            "Color Theme",
            ["Purple Glow", "Cyber Blue", "Neon Green"],
            index=0
        )
        
        # Clear chat button with confirmation
        if st.button("🗑️ Clear History"):
            if st.session_state.messages:
                if st.button("⚠️ Confirm Clear?"):
                    st.session_state.messages = []
                    st.session_state.chat_history.clear_history()
                    st.rerun()
        
        st.divider()
        st.caption("✨ Made by samad with 💜")
        st.caption("✨Powered by Google Gemini AI")
    
    # Main content
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("✨ Buddy-Bot(Nora)👩 AI Assistant")
        st.caption("Your friendly AI buddy for coding & fun! 🤖💻")
    
    # Initialize chat interface
    chat_interface = ChatInterface()
    chat_interface.display()

if __name__ == "__main__":
    main() 