from win10toast import ToastNotifier
import json
import time
import requests

def updater():#the whole function
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Confirmed cases: {data["cases"]} \nDeaths : {data["death"]} \nRecovered : {data["recovered"]}'

    #loop to have the updates after specified time intervals
    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 updates", text, duration=20)#the heading for the notification, duration is how long the notification will be displayed for in seconds
        toast.sleep(60)#Interval of notification
        
updater()