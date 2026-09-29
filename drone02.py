from codrone_edu.drone import *

drone = Drone()
drone.connect()

#Lift off
drone.takeoff()
drone.hover(1)

'''
#Out and back
drone.move_forward(50, "cm", 1)     # 50 cm forward at 1 m/s
drone.hover(1)
drone.move_backward(50, "cm", 1)    # and back

#Turning
drone.turn_degree(90)      # turn LEFT 90 degrees
drone.turn_degree(-90)     # turn RIGHT 90 degrees

#Square 
drone.takeoff()
drone.hover(1)

drone.move_forward(50, "cm", 1)
drone.turn_degree(90)

drone.move_forward(50, "cm", 1)
drone.turn_degree(180)

drone.move_forward(50, "cm", 1)
drone.turn_degree(270)

drone.move_forward(50, "cm", 1)

#Square with loop
for i in range(4):                  # do this four times
    drone.move_forward(20, "cm", 1)
    drone.turn_left()               # turn 90 from where it is facing now
'''
#Course code 
drone.move_forward(65, "in", 0.5)
drone.turn_right()

drone.move_forward(24, "in", 0.5)
drone.turn_left()

drone.move_forward(60, "in", 0.5)
drone.turn_right()

drone.move_forward(52, "in", 0.5)
drone.hover(1)

#Landing
drone.land()

drone.disconnect()