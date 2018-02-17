import os
from datetime import datetime
from sense_hat import SenseHat

from main import get_smooth, get_cpu_temp

def monitor():
    sense = SenseHat()
    temp = sense.get_temperature()
    t_cpu = get_cpu_temp()
    # calculates the real temperature compesating CPU heating
    t = (t1+t2)/2
    t_corr = t - ((t_cpu-t)/1.5)
    t_corr = get_smooth(t_corr)
    f = open("templog.txt", "a+")
    f.write("{},{}".format(datetime.utcnow('T'), t_corr))
    f.close()


if __name__ == '__main__':
    monitor()
