from time import sleep
import grovepi

ultrasonic_ranger_right = 2
ultrasonic_ranger_left = 7
led = 3

grovepi.pinMode(ultrasonic_ranger_right,"INPUT")
grovepi.pinMode(ultrasonic_ranger_left,"INPUT")
grovepi.pinMode(led,"OUTPUT")

while True:
    try:
        sleep(0.2)
        distance_left = grovepi.ultrasonicRead(ultrasonic_ranger_left)
        sleep(0.2)
        distance_right = grovepi.ultrasonicRead(ultrasonic_ranger_right)
        print("Right is: %s cm Left is: %s cm" % (distance_right, distance_left))
        if (distance_right <=10 and distance_left <=10):
            grovepi.digitalWrite(led,1)
        else:
            grovepi.digitalWrite(led,0)
            
    except TypeError:
        print("TypeError")
    except IOError:
        print("IOError")
        
    except KeyboardInterrupt:
        grovepi.digitalWrite(led, 0)
