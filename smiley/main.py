
from sense_hat import SenseHat

X = [0, 255, 0]
O = [0,0,0]
R = [255,0,0]

frown = [
O, O, O, O, O, O, O, O,
O, R, R, O, O, R, R, O,
O, O, R, O, O, R, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, R, R, R, R, O, O,
O, R, O, O, O, O, R, O,
R, R, O, O, O, O, R, R
]

wink = [
O, O, O, O, O, O, O, O,
O, X, X, O, O, X, X, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, O, O, O,
X, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, X, X, O, O, O
]

def smiley():
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
    smiley()
