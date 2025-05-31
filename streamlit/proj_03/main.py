import streamlit as st
import random

st.set_page_config(page_title="Debug the Word", layout="wide")
st.markdown("""
    <style>
        .stTextInput {
            width: 300px !important;
        }
        .custom-text{
            width: 500px !important;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stAlert {
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
        }
        .main {
            padding: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Debug the Word")

st.markdown('<div class="custom-text">A fun, brain-teasing word game for techies! Guess programming languages, coding terms and much more before getting out of lives. Stuck? Maybe its a feature, not a bug! 🔥💻 Think fast, code faster, and debug your way to victory! 🚀</div>', unsafe_allow_html=True)



words = [
    "bug", "code", "data", "loop", "file",  
    "debug", "cache", "token", "event", "merge",
    "python", "type", "html", "css", "java",  
    "react", "angular", "django", "flask", "next",  
    "list", "tuple", "object", "boolean", "integer",  
    "variable", "function", "class", "method", "async",  
    "array", "string", "number", "float", "index",  
    "idea", "learn", "grow", "build", "change",  
    "skill", "create", "try", "focus", "think",  
    "logic", "goal", "start", "solve", "adapt",  
    "future", "believe", "improve", "share", "move"
]

if 'random_word' not in st.session_state:
    st.session_state.random_word = random.choice(words)
    st.session_state.display_word = ['_' for _ in st.session_state.random_word]
    st.session_state.user_input = ""
    st.session_state.guessed_letters = set()
    st.session_state.lives = 10

st.subheader("Word: " + ' '.join(st.session_state.display_word))
st.write(f"Lives Remaining: {st.session_state.lives} ❤️")




def process_guess():
    user_guess = st.session_state.get("input_key", "").strip().lower()
    if user_guess and user_guess not in st.session_state.guessed_letters:
        st.session_state.guessed_letters.add(user_guess)
        if user_guess in st.session_state.random_word:
            for idx, letter in enumerate(st.session_state.random_word):
                if letter == user_guess:
                    st.session_state.display_word[idx] = user_guess
        
        else:
            st.session_state.lives -= 1
            
        st.session_state.input_key = ""

guess = st.text_input("Guess a letter:", key="input_key", on_change=process_guess)

if st.session_state.lives == 0:
    st.error(f"You lost! The correct word was: {st.session_state.random_word.upper()}")
    if st.button("Play Again"):
        
        del st.session_state["guessed_letters"]

        del st.session_state["random_word"]
        del st.session_state["display_word"]
        del st.session_state["lives"]
        st.rerun()

if '_' not in st.session_state.display_word:
    st.success("Congratulations! You guessed the word: " + st.session_state.random_word.upper())
    if st.button("Play Again"):
        del st.session_state["guessed_letters"]

        del st.session_state["random_word"]
        del st.session_state["display_word"]
        st.rerun()
elif st.session_state.lives > 0: 
    if st.button("Guess"):
        process_guess()


