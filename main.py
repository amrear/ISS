import urllib.request
import json
import turtle

sc = turtle.Screen()
sc.setup(1280, 640)
sc.setworldcoordinates(-180, -90, 180, 90)
sc.bgpic("map.gif")
sc.register_shape("iss.gif")

def show_iss(lat, lon):
	iss = turtle.Turtle()
	iss.shape("iss.gif")
	iss.setheading(90)
	iss.penup()
	iss.goto(lon, lat)

print("Connecting to the server...\n")

astros = json.loads(urllib.request.urlopen("http://api.open-notify.org/astros.json").read())
iss = json.loads(urllib.request.urlopen("http://api.open-notify.org/iss-now.json").read())

if not astros["message"] == "success" or not iss["message"] == "success":
	raise Exception("Something went wrong!")

astros_names = [astro["name"] for astro in astros["people"]]

print(f"Currently there are {astros['number']} people in ISS:")
for astro_name in astros_names:
	print(f"\t {astro_name}")

lat = iss['iss_position']['latitude']
lon = iss['iss_position']['longitude']

print(f"\nlatitude: {lat}, longitue: {lon}\n")

show_iss(float(lat), float(lon))
input("Press Enter to exit")