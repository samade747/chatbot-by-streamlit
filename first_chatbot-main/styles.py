import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container */
        .stApp {
            background: #ffffff;
        }
        
        .main {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 2rem;
        }
        
        /* Chat messages */
        .stChatMessage {
            padding: 1.5rem;
            border-radius: 20px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            animation: fadeIn 0.5s ease-out;
            background: white;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* User message */
        .stChatMessage[data-testid="chat-message-user"] {
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white !important;
            border-bottom-right-radius: 5px;
            box-shadow: 0 5px 15px rgba(99, 102, 241, 0.2);
        }
        
        /* Assistant message */
        .stChatMessage[data-testid="chat-message-assistant"] {
            background: white;
            border: 1px solid rgba(99, 102, 241, 0.1);
            border-bottom-left-radius: 5px;
        }
        
        .stChatMessage[data-testid="chat-message-assistant"] p {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        /* Chat container wrapper */
        .stChatFloatingInputContainer {
            bottom: 0;
            background: linear-gradient(to top, rgba(248, 249, 250, 1) 0%, rgba(248, 249, 250, 0.9) 50%, transparent 100%);
            padding: 2rem 0;
            margin: -6rem 0 0 0;
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(99, 102, 241, 0.1);
        }

        /* Input container positioning */
        .stChatInputContainer {
            padding: 0.5rem;
            max-width: 800px;
            margin: 0 auto;
            background: transparent;
        }

        /* Input box styling */
        .stChatInput {
            border-radius: 25px !important;
            border: 2px solid rgba(99, 102, 241, 0.2) !important;
            padding: 1.2rem 2rem !important;
            font-size: 1rem !important;
            background: white !important;
            color: #1f2937 !important;
            width: 100% !important;
            max-width: 800px !important;
            margin: 0 auto !important;
            display: block !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            position: relative;
        }

        /* Input hover and focus states */
        .stChatInput:hover {
            border-color: rgba(99, 102, 241, 0.4) !important;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.1);
        }

        .stChatInput:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 25px rgba(99, 102, 241, 0.2);
            transform: translateY(-2px);
        }

        /* Message container spacing */
        .stChatMessageContainer {
            padding-bottom: 120px;  /* Space for input */
        }

        /* Title */
        .stTitle {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(45deg, #6366f1, #8b5cf6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-align: center;
            font-weight: 700;
            font-size: 2.5rem !important;
            text-shadow: 0 0 30px rgba(99, 102, 241, 0.3);
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 20px rgba(99, 102, 241, 0.2); }
            to { text-shadow: 0 0 30px rgba(99, 102, 241, 0.4); }
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: white;
            border-right: 1px solid rgba(99, 102, 241, 0.1);
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: white !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2);
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
        }
        
        /* Caption text */
        .stCaption {
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            background: #f8f9fa;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(to bottom, #6366f1, #8b5cf6);
            border-radius: 4px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .main {
                padding: 1rem;
            }
            
            .stTitle {
                font-size: 2rem !important;
            }
            
            .stChatFloatingInputContainer {
                padding: 1rem 0;
            }
            
            .stChatInputContainer {
                padding: 0.5rem;
                margin: 0 1rem;
            }
            
            .stChatInput {
                padding: 1rem 1.5rem !important;
                font-size: 0.9rem !important;
            }
        }
        </style>
    """, unsafe_allow_html=True) 