#This shows the effect of multiple lag filter connected. It steepens the cut-off frequency slope (in a bode plot)
import matplotlib.pyplot as plt
import numpy as np
def lag(V_input,T,V_previous_output):  #lag function
    V_new_output = V_previous_output + (V_input - V_previous_output)/T
    return V_new_output

#-------------tuning------------------------------------------
Time_domain_max = 250   #controls the length of X axis
T = 15   #Time constant
f = 10  #Frequency

#---------------Declaring array for plotting------------------------------------------
t = np.arange(0, Time_domain_max, 1) #(start_value, max, increment)
y_V_input = 100 * (np.sin((2*np.pi*f*t)/100)) #using sin for harmonic wave # sin works with values less than 1
y_lag_1 = 100 * (np.sin((2*np.pi*f*t)/100))
y_lag_2 = 100 * (np.sin((2*np.pi*f*t)/100))
y_lag_3 = 100 * (np.sin((2*np.pi*f*t)/100))
y_V_output = 100 * (np.sin((2*np.pi*f*t)/100))  #Y values for plotting
#-------------------------------------------------------------------------------------
#--------Manipulating the second array to show effect of lag--------------------------
ctr_t = 0
y_V_output[0] = 100 * (np.sin((2*np.pi*f*ctr_t)/100)) #set initial value Because Lag function depends on previous values,
y_lag_1[0] = 100 * (np.sin((2*np.pi*f*ctr_t)/100))
y_lag_2[0] = 100 * (np.sin((2*np.pi*f*ctr_t)/100))
y_lag_3[0] = 100 * (np.sin((2*np.pi*f*ctr_t)/100))

ctr_t = 1
while (ctr_t < Time_domain_max):

    Vin = 100 * np.sin(2*np.pi*f*ctr_t/100) #new V_Input
    prev = ctr_t - 1
    y_lag_1[ctr_t] = lag(Vin,T,y_V_output[prev])
    y_lag_2[ctr_t] = lag(y_lag_1[ctr_t], T, y_lag_1[prev])
    y_lag_3[ctr_t] = lag(y_lag_2[ctr_t], T, y_lag_2[prev])
    y_V_output[ctr_t] = y_lag_3[ctr_t]
    ctr_t = ctr_t + 1

#-------------------Plotting stuff--------------------------
lines = plt.plot(t,y_V_input,t,y_V_output) #plotting lines against t(time)
l1, l2 = lines
plt.setp(l2, linestyle='--', linewidth=1, color='b')
plt.setp(l1,linewidth=2, color='g')

ojo = plt.title('3 Stage Lag filter (LPF) by Temuujin')

plt.grid(True)
plt.show()
