import google.generativeai as genai


API_KEY="AIzaSyDenTN2hQEVhpunx2C32WtUdqze_Yms6N8"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content()