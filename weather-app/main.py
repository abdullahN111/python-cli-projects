from tkinter import *
from tkinter import ttk
import requests

def get_data():
    
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e0937f1c27bc7e87a11b580ee9ae3b2f").json()
    weather_output.config(text=data["weather"][0]["main"])
    desc_output.config(text=data["weather"][0]["description"])
    temp_output.config(text=str(data["main"]["temp"]))
    temp_output.config(text=data["main"]["pressure"])

wind = Tk()
wind.title("Weather App")
wind.config(bg="blue")
wind.geometry("500x500")


list_name = [  "Islamabad", "Karachi", "Lahore", "Faisalabad", "Rawalpindi", 
    "Peshawar", "Quetta", "Multan", "Sialkot", "Gujranwala", 
    "Sargodha", "Bahawalpur", "Sukkur", "Hyderabad", "Mardan", 
    "Abbottabad", "Muzaffarabad", "Gilgit", "Mirpur", "Sheikhupura", 
    "Larkana", "Rahim Yar Khan", "Jhang", "Okara", "Kasur", 
    "Gujrat", "Mingora", "Dera Ghazi Khan", "Nawabshah", "Mansehra", 
    "Chiniot", "Turbat", "Kotli", "Bannu", "Kohat", 
    "Dera Ismail Khan", "Vehari", "Khuzdar", "Jhelum", "Attock", 
    "Swabi", "Hafizabad", "Lodhran", "Mandi Bahauddin", "Sahiwal", 
    "Shikarpur", "Thatta", "Jacobabad", "Kamber", "Ghotki"]

city_name = StringVar()


name_label = Label(wind, text="Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=50, y=50, height=50, width=400)

com_box = ttk.Combobox(wind, text="Weather App", values=list_name, font=("Times New Roman", 15, "bold"), textvariable=city_name)

com_box.place(x=50, y=120, height=50, width=400)




weather_label = Label(wind, text="Weather Climate:", font=("Times New Roman", 11, "bold"))
weather_label.place(x=50, y=270, height=30, width=160)
weather_output = Label(wind, font=("Times New Roman", 11, "bold"))
weather_output.place(x=230, y=270, height=30, width=150)

desc_label = Label(wind, text="Description:", font=("Times New Roman", 11, "bold"))
desc_label.place(x=50, y=310, height=30, width=160)
desc_output = Label(wind, font=("Times New Roman", 11, "bold"))
desc_output.place(x=230, y=310, height=30, width=150)

temp_label = Label(wind, text="Temperature:", font=("Times New Roman", 11, "bold"))
temp_label.place(x=50, y=350, height=30, width=160)
temp_output = Label(wind, font=("Times New Roman", 11, "bold"))
temp_output.place(x=230, y=350, height=30, width=150)

pressure_label = Label(wind, text="Pressure:", font=("Times New Roman", 11, "bold"))
pressure_label.place(x=50, y=390, height=30, width=160)
pressure_output = Label(wind, font=("Times New Roman", 11, "bold"))
pressure_output.place(x=230, y=390, height=30, width=150)


btn = Button(wind, text="Check Weather", font=("Times New Roman", 11, "bold"), command=get_data)
btn.place(x=200, y=190, height=40, width=120)


wind.mainloop()
