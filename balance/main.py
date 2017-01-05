from sense_hat import SenseHat

def tipper():
    sense = SenseHat()
    while True:
        orientation = sense.get_orientation()
        roll = orientation['roll']
        #print('{:.2f}'.format(roll))
        if roll > 70 and roll < 110.0:
            sense.set_pixels(frown)
        else:
            sense.set_pixels(wink)

if __name__:
    tipper()
