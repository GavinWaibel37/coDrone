from codrone_edu.drone import *

drone = Drone()
drone.pair()

battery = drone.get_battery()      # ask the drone how much charge is left
print("Battery:", battery, "%")    # show it in the Console

drone.set_drone_LED(0, 255, 0, 100)    # red, green, blue, brightness


# Takeoff
drone.takeoff()
drone.drone_buzzer(440, 500)    # 440 Hz for 500 milliseconds

#Hover
drone.hover(6)

#Landing
drone.drone_buzzer(400, 300)
drone.land()

#Close program
drone.close()