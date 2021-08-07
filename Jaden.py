import speech_recognition
import pyttsx3
import requests
from datetime import date, datetime
import os
import webbrowser

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""


def weather(city_name):
    api_key = "04417d4ed9c27909c9b1a2304004920a"
    base_ulr = "http://api.openweathermap.org/data/2.5/weather?"
    complete_ulr = base_ulr + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_ulr)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = int(y["temp"] - 273.15)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        robot_brain = "Now it is" + str(weather_description) + ", the temperature is " + str(current_temperature) + " degree Celsius," + \
            " the humidity is " + str(current_humidity) + " %," + \
            " the air pressure is " + str(current_pressure) + " hPa"
    else:
        robot_brain = "I can't find your city"
    return robot_brain


def square(number):
    square_result = number * number
    return square_result


def subtract(number1, number2):
    subtract_result = number1 - number2
    return subtract_result


def add(number1, number2):
    add_result = number1 + number2
    return add_result


def divide(number1, number2):
    add_result = number1 / number2
    return add_result


def multiply(number1, number2):
    add_result = number1 * number2
    return add_result


while True:
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic)
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic, timeout=5, phrase_time_limit=5)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    # brain
    if you == '':
        robot_brain = "I can't hear you, try again"
    elif 'hello' in you or 'hi' in you:
        robot_brain = 'Yo, whats up'
    elif 'name' in you:
        robot_brain = 'My name is Jaden'
    elif 'date' in you:
        today = date.today()
        robot_brain = "Today is " + today.strftime("%B %d, %Y")
    elif 'time' in you:
        now = datetime.now()
        robot_brain = "Now is " + \
            now.strftime("%H hours %M minutes %S seconds")
    elif 'where' in you and 'I' in you:
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        robot_brain = "You are in " + city
    elif 'Google' in you:
        robot_brain = "Opening Google"
        webbrowser.open("http://google.com", new=1)
    elif 'YouTube' in you:
        robot_brain = 'Opening YouTube'
        webbrowser.open("http://youtube.com", new=1)
    elif "weather" in you:
        robot_mouth.say("Type your city here: ")
        robot_mouth.runAndWait()
        you = input("Robot: Type your city here ")
        robot_brain = weather(you)
    elif "Square" in you:
        robot_mouth.say("Type your number here: ")
        robot_mouth.runAndWait()
        you = int(input("Robot: Type your number here: "))
        you_1 = str(you)
        robot_brain = you_1 + " square is " + str(square(you))
    elif "subtract" in you:
        robot_mouth.say("Type your numbers here: ")
        robot_mouth.runAndWait()
        you = a, b = (input("Robot: Type your numbers here: ").split())
        number1 = int(a)
        number2 = int(b)
        robot_brain = 'The result is: ' + str(subtract(number1, number2))
    elif "add" in you:
        robot_mouth.say("Type your numbers here: ")
        robot_mouth.runAndWait()
        you = a, b = (input("Robot: Type your numbers here: ").split())
        number1 = int(a)
        number2 = int(b)
        robot_brain = 'The result is: ' + str(add(number1, number2))
    elif "divide" in you:
        robot_mouth.say("Type your numbers here: ")
        robot_mouth.runAndWait()
        you = a, b = (input("Robot: Type your numbers here: ").split())
        number1 = int(a)
        number2 = int(b)
        robot_brain = 'The result is: ' + str(divide(number1, number2))
    elif "multiply" in you or "multi-ply" in you:
        robot_mouth.say("Type your numbers here: ")
        robot_mouth.runAndWait()
        you = a, b = (input("Robot: Type your numbers here: ").split())
        number1 = int(a)
        number2 = int(b)
        robot_brain = 'The result is: ' + str(multiply(number1, number2))
    elif 'goodbye' in you or 'bye' in you:
        robot_brain = 'See ya'
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = 'Whattttt'
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
