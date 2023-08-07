import requests
import json
import time
import geocoder
import turtle
import datetime

def main():
    starttime = time.time()
    myLocation = geocoder.ip('me')
    print(f"Current Location: {myLocation.city}")
    print(f"Latitude + Longitude: {myLocation.latlng}")
    
    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)

    
    # load the world map image and update pin location for users IP address
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    screen.register_shape("little_pin.gif")
    pin = turtle.Turtle()
    pin.shape("little_pin.gif")
    pin.setheading(45)
    pin.penup()
    pin.goto(float(myLocation.latlng[1]), float(myLocation.latlng[0]))
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()


    while True:
        # Remove the Time taken by code to execute
        response = requests.get("http://api.open-notify.org/iss-now.json")
        #print(response.json())
        
        if(response.status_code != 200):
            print("Error Code: " + response.status_code)
            break
        
        #update long and lat of ISS
        issLatLon = response.json()['iss_position']
        issLon = issLatLon['longitude']
        issLat = issLatLon['latitude']
        
        print(f"\nISS Location: [{issLat},{issLon}]")
        print(datetime.datetime.fromtimestamp(response.json()['timestamp']))
        
        issLon = float(issLon)
        issLat = float(issLat)
        
        #update loaction on map
        iss.goto(issLon,issLat)
        
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))
        
if __name__ == '__main__':
    main()