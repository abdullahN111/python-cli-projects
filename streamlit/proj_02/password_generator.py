import streamlit as st
import random
import string


def app():
    def generate_password(length, use_digits, use_special_char):
        characters = string.ascii_letters
        
        if use_digits:
            characters += string.digits
        
        if use_special_char:
            characters += string.punctuation
        
        return "".join(random.choice(characters) for _ in range(length))


    # st.set_page_config(page_title="iSolutions | Password Generator", page_icon="⚙")

    st.title("Password Generator")

    length = st.slider("Select Password Length", min_value=8, max_value=20, value=8)

    use_digits = st.checkbox("Include Digits")
    use_special_char = st.checkbox("Include Special characters")

    if st.button("Generate Password"):
        password = generate_password(length, use_digits, use_special_char)
        st.write(f"Generated Password: `{password}`")