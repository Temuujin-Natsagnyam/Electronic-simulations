#This filter blocks out low frequencies. Try changing values for f on line 16 to see effects
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import numpy as np

def lag(V_input,T,V_previous_output):  #lag function
    V_new_output = V_previous_output + (V_input - V_previous_output)/T
    return V_new_output
def lead(V_input,T,V_previous_output):
    V_new_output = V_input - V_previous_output
    return V_new_output

#-------------tuning------------------------------------------
Time_domain_max = 250   #controls the length of X axis
T = 10 #Time constant
f = 1  #Frequency
#----------Declaring array-------------------------------------
t = np.arange(0,Time_domain_max, 1)
y_V_input = 100 * (np.sin((np.pi*f*t)/100))
y_lag_output = (np.sin((np.pi*f*t)/100))
y_V_output = 100 * (np.sin((np.pi*f*t)/100))


ctr_t = 0
y_lag_output[0] = 100 * (np.sin((np.pi*f*ctr_t)/100))
ctr_t = 1
while (ctr_t < Time_domain_max):

    Vin = 100 * np.sin(np.pi*f*ctr_t/100) #new V_Input
    prev = ctr_t - 1

    y_lag_output[ctr_t] = lag(Vin,T,y_lag_output[prev])
    lag_out = y_lag_output[ctr_t]
    v_out = lead(Vin,T,lag_out)
    y_V_output[ctr_t] = v_out

    ctr_t = ctr_t + 1

#------------Plotting stuff--------------------------
lines = plt.plot(t,y_V_input,t,y_V_output) #plotting lines against t(time)
l1, l2 = lines
plt.setp(l2, linestyle='--', linewidth=1, color='b')
plt.setp(l1,linewidth=2, color='g')

ojo = plt.title('LEAD filter (HPF) by Temuujin')
legend([l1, l2], ["Voltage input", "Voltage Output"])
plt.grid(True)
plt.show()


