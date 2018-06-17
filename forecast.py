#!/usr/bin/python3

from weather import Weather, Unit
from subprocess import call



#current weather for a perticular area
def weather_current():
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('jaipur')
    condition = location.condition
    con = f'It\'s {condition.text} today'
    temp =f'With temp {condition.temp}𐤏C'
    call(['notify-send','-u','normal', con, temp])
    

if __name__=="__main__":
    weather_current(flocation)
