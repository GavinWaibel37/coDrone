from codrone_edu.drone import *
import time



drone = Drone()
drone.connect()

# Drone Color
drone.set_drone_LED(255, 0, 0, 100)
time.sleep(1)
drone.set_drone_LED(255, 165, 0, 100)
time.sleep(1)
drone.set_drone_LED(255, 255, 0, 100)
time.sleep(1)
drone.set_drone_LED(0, 225, 0, 100)
time.sleep(1)
drone.set_drone_LED(100, 100, 100, 100)
time.sleep(1)
drone.drone_LED_off()

#Controller Color
drone.set_controller_LED(0, 225, 0, 100)
drone.controller_LED_off()

#Sound
drone.drone_buzzer(440, 500)         # 440 Hz for 500 milliseconds
drone.controller_buzzer(880, 200)

#Status Lights
drone.set_drone_LED(0, 0, 255, 100)      # blue: getting ready
drone.drone_buzzer(392, 200)
time.sleep(1)

drone.takeoff()
drone.set_drone_LED(0, 255, 0, 100)      # green: flying
drone.hover(1)

drone.set_drone_LED(255, 255, 0, 100)    # yellow: about to land
drone.land()

drone.drone_buzzer(262, 400)
drone.drone_LED_off()

#Startup sequence
# Step 1: Low wake-up chime (Deep Tone) with Cyan LED
drone.set_drone_LED(0, 255, 255, 100)  # Cyan
drone.drone_buzzer(262, 300)          # Low tone
time.sleep(0.4)

# Step 2: Rising mid-tone transition with Magenta LED
drone.set_drone_LED(255, 0, 255, 100)  # Magenta
drone.drone_buzzer(392, 300)          # Mid tone
time.sleep(0.4)

# Step 3: High ready-beep with Bright Green LED
drone.set_drone_LED(0, 255, 0, 100)    # Green
drone.drone_buzzer(523, 400)          # High tone
time.sleep(0.5)

# --- CLEANUP / POWER DOWN LIGHTS & BUZZER ---
drone.set_drone_LED(0, 0, 0, 0)        # Turn LED off


drone.disconnect()