from tkinter import *
import requests
import json

root=Tk()
root.title("My country App")
root.geometry("200x200")
root.configure(background="white")

city_name_label=Label(root, text="",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.5,rely=0.15,anchor=CENTER)

def city():
    api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=3245364764575543")
    
    api_output_json = json.loads(api_request.content)
    
    city_name_label=api_output_json[0]['data']
    
search=Button(root,text="Search",command=city) 
search.place(relx=0.5,rely=0.95,anchor=CENTER)   

root.mainloop()