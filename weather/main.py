import os
import time
from sense_hat import SenseHat

# get CPU temperature
def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)


def check_weather():
    sense = SenseHat()

    while True:
      t1 = sense.get_temperature_from_humidity()
      t2 = sense.get_temperature_from_pressure()
      t_cpu = get_cpu_temp()
      h = sense.get_humidity()
      p = sense.get_pressure()

      # calculates the real temperature compesating CPU heating
      t = (t1+t2)/2
      t_corr = t - ((t_cpu-t)/1.5)
      t_corr = get_smooth(t_corr)

      event = sense.stick.wait_for_event(emptybuffer=True)
      if event.direction == 'UP':
          sense.show_message("{:.1f}C".format(t_corr))
      elif event.direction == 'down':
          sense.show_message("{:.1f}%".format(h))
      else:
          sense.clear()

if __name__:
     check_weather()
