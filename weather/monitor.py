import os
from datetime import datetime
from sense_hat import SenseHat

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return t

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return xs

def monitor():
    sense = SenseHat()
    temp = sense.get_temperature()
    t_cpu = get_cpu_temp()
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    # calculates the real temperature compesating CPU heating
    t = (t1+t2)/2
    t_corr = t - ((t_cpu-t)/1.5)
    t_corr = get_smooth(t_corr)
    f = open("templog.txt", "a+")
    f.write("{},{}".format(datetime.utcnow('T'), t_corr))
    f.close()
    return


if __name__ == '__main__':
    monitor()
