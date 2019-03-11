from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
import requests
import json

red = [255, 0, 0]
green = [0, 255, 0]

redMatrix = [red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red]
greenMatrix = [green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green]

r = requests.get('https://randomuser.me/api/?results=1').json()

with open('data.json', 'w') as outfile:
    json.dump(r, outfile)

sense = SenseHat();

sense.show_message(r["results"][0]["name"]["first"])

while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":

      if event.direction == "left":
        sense.set_pixels(redMatrix)
      elif event.direction == "right":
        sense.set_pixels(greenMatrix)

      sleep(0.5)
      sense.clear()