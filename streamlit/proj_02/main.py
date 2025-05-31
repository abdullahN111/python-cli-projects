import streamlit as st
from streamlit_option_menu import option_menu

import password_generator, account, home, unit_converter, file_converter, quiz


st.set_page_config(
    page_title="iSolutions",
    page_icon="⚙"
)

class MultiApp:
    def __init__(self):
        self.apps = []
        
    def add(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
        
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="iSolutions",
                options=["Home", "File Converter", "Unit Converter", "Password Generator", "Guess A Word", "Account"],
                icons=["house-fill", "trophy-fill", "chat-fill", "info-circle-fill", "question-circle-fill", "person-circle"],
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "menu-title": {"color": "white", "font-size": "22px", "font-weight": "bold", "text-align": "center"},
                    "icon": {"color": "white", "font-size": "20px"}, 
                    "nav-link": {"color":"white","font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                            "nav-link-selected": {"background-color": "#02ab21"},
                        }
                    )
            
        if app == "Home":
            home.app()
                
        elif app == "File Converter":
            file_converter.app()
                
        elif app == "Unit Converter":
            unit_converter.app()
                
        elif app == "Password Generator":
            password_generator.app()
                
                
        elif app == "Guess A Word":
            quiz.app()
                
        elif app == "Account":
            account.app()
            
        else:
            st.header("404. Not found!")
                
    run()
                
            