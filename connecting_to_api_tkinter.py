'''
Connection to an API in tkinter
weather app
main.py
'''

from tkinter import *
import requests
import json

root = Tk()
root.title("Air Quality")
root.geometry("750x300")

def zipLookup():
    #zip.get()
    #_ = Label(root, text=zip.get()).grid(row=1, column=0, columnspan=2)

    try:
        api_requests = requests.get(
            f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip.get()}&date=2021-11-11&distance=5&API_KEY=BDF95C60-B49D-4F5A-BF71-0EBA71E01B7F")
        api = json.loads(api_requests.content)

        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
        root.configure(bg=weather_color)
        _ = Label(root, text=city + " Air Quality " + str(quality) + "; " + category, font=("Helvetica", 20),
                      bg=weather_color).grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error"


# https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=93021&date=2021-11-11&distance=5&API_KEY=BDF95C60-B49D-4F5A-BF71-0EBA71E01B7F


zip = Entry(root, text="Search For Zip Code:")
zip.grid(row=0, column=0, padx=170, ipadx=50)
zipButton = Button(root, text="Search", command=zipLookup).grid(row=0, column=1, ipadx=65)

