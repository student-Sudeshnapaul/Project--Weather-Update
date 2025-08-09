from tkinter import *
import requests
from PIL import Image, ImageTk
from tkinter import messagebox
import json

root= Tk()

root.title("Weather Update")

root.geometry("800x600")

#Use a background image for user interface
img= Image.open(r"C:\Users\Sudeshna\Desktop\Weather_update\Weather_img.jpeg") #Open the bg image
img= img.resize((800, 600)) #Size of the image
tk_img= ImageTk.PhotoImage(img) #Converting the image as Tk image
bg_label= Label(root, image=tk_img) #Creating a lebel for the image
bg_label.place(x=0, y=0, relwidth=1, relheight=1) #Place the image as the whole background of the window

#Create an Entry box to get input(city) from the user
I1= Label(root, text="Enter the City", font= ("Algerian", 25), fg="Black", bg="grey" )
I1.grid(pady=25, padx=273)
txt=Entry(root)
txt.grid(pady=25, padx=273)

#Create Buttons
bt_frame= Frame(root)
bt_frame.grid(padx= 5)
def show_data():
    global L1 
    city=txt.get()#Get the city name
    API_KEY = 'dde92c2489c2a82f1fe15839b527dd1f' #API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)#Send requests for the Data
    data=response.json()
    if not city.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a valid city name (only alphabets).")
        return
    else: 
           if response.status_code==200:
                 city="City:"+ data["name"]
                 temperature="Temperature: "+ str(data["main"]["temp"])+ "°C"
                 feels_like="Feels Like: "+ str(data["main"]["feels_like"])+ "°C"
                 humidity="Humidity: "+ str(data["main"]["humidity"])+ "%"
                 wind="Speed of Wind: "+ str(data["wind"]["speed"])
                 weather_des="Weather: "+ str(data["weather"][0]["description"])
                 total=city+ "\n\n"+ temperature+ "\n\n"+ feels_like+ "\n\n"+ humidity+ "\n\n"+ wind+ "\n\n"+ weather_des
                 L1= Label(root, text=total, font= ("Times New Roman Font",13), fg="black", bg="pink")
                 L1.grid(pady=25)
           else:
                   messagebox.showinfo(title= "Error", message= data["message"])
def reset_pg() :
    txt.delete(0,END)
    global L1 
    if 'L1' in globals():
        L1.destroy()
def destroy() :
      root.destroy
bt_1= Button(bt_frame, text= "View",width=10, fg="white", bg="green", command=show_data)
bt_1.grid(padx= 5)
bt_2= Button(bt_frame, text= "Reset", width=10, fg="white", bg="blue", command= reset_pg)
bt_2.grid(pady= 5)
bt_3= Button(bt_frame, text= "Exit", width=10, fg="black", bg="yellow", command= destroy)
bt_3.grid(pady= 5)

root.mainloop()
