import streamlit as st
import password_generator, account, home, unit_converter, file_converter, quiz

def app():
    st.title("⚙ iSolutions - All-in-One Tools")
    
    st.markdown(
        """
        <style>
            .home-container {
                text-align: center;
                padding: 20px;
                background-color: #1e1e1e;
                color: white;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(255, 255, 255, 0.1);
                margin: 20px;
            }
            .home-text {
                font-size: 18px;
                margin-top: 10px;
            }
        </style>
        <div class="home-container">
            <h2>Welcome to iSolutions 🚀</h2>
            <p class="home-text">Your one-stop destination for essential tools!<br>
            Convert files, generate secure passwords, test your knowledge with word games, and much more.</p>
            <p class="home-text">Choose a tool from the sidebar and get started!</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("🔧 Available Tools:")
    tools = ["🏠 Home", "📂 File Converter", "📏 Unit Converter", "🔑 Password Generator", "❓ Guess A Word", "👤 Account"]
    for tool in tools:
        st.markdown(f"- {tool}")
