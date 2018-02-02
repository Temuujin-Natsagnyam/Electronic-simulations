# This animation shows the frequency of the graph increasing and decreasing. You can see that the Low pass filter lowers voltage output
# when the frequency increase, and increase when the frequency lowers.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def init():
    line.set_ydata(np.ma.array(t, mask=True))
    line2.set_ydata(np.ma.array(t, mask=True))
    return line, line2

def lag(V_input,T,V_previous_output):  #lag function
    V_new_output = V_previous_output + (V_input - V_previous_output)/T
    return V_new_output

#-------------tuning------------------------------------------
T = 25
my_interval = 25  #is the rate of animation msec
my_Zoomin = 15 #For zooming in on lower Hz
my_Amplitude = 100 # amplitude
my_max_x = 8 #seems to affect speed of animation
my_animation_start = -300
my_animation_end = 300

#--------declaring array/buffers----------------
fig, ax = plt.subplots()
t = np.arange(0, my_max_x, 0.01)
y_input = my_Amplitude * np.sin(t)
y_output = my_Amplitude * np.sin(t)

line, = ax.plot(t, y_input)
line2, = ax.plot(t, y_output)

#--------------animation part---------------
def animate(Hz):    #Our animation is displaying on change in frequency
    line.set_ydata(my_Amplitude * np.sin(t*Hz/my_Zoomin))
    #------Adding in lag function----------
    ctr_x = 0
    y_output[0] = my_Amplitude * np.sin((Hz*ctr_x/my_Zoomin)/100)
    ctr_x = 1
    while (ctr_x < (my_max_x * 100)):
        Vin = my_Amplitude * np.sin((Hz*ctr_x/my_Zoomin)/100)
        prev = ctr_x - 1
        y_output[ctr_x] = lag(Vin,T,y_output[prev])

        ctr_x = ctr_x + 1
    line2.set_ydata(y_output)
    return line, line2

ani = animation.FuncAnimation(fig, animate, np.arange(my_animation_start, my_animation_end),
                              init_func=init,
                              interval=my_interval,
                              blit=True)
ojo = plt.title('LAG filter(LPF) Animation by Temuujin')
plt.grid(True)
plt.show()
