from __future__ import print_function
import matplotlib.pyplot as plt
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
f = 10  #Frequency
my_amplitude = 100
#----------Declaring array-------------------------------------
t = np.arange(0,Time_domain_max, 1)
y_V_input = my_amplitude * (np.sin((np.pi*f*t)/100))
y_lag_output1 = my_amplitude * (np.sin((np.pi*f*t)/100))
y_lead_output1 = my_amplitude * (np.sin((np.pi*f*t)/100))

y_lag_output2 = my_amplitude * (np.sin((np.pi*f*t)/100))
y_lead_output2 = my_amplitude * (np.sin((np.pi*f*t)/100))

y_lag_output3 = my_amplitude * (np.sin((np.pi*f*t)/100))
y_lead_output3 = my_amplitude * (np.sin((np.pi*f*t)/100))

#---------------------------------------------------
ctr_t = 0
y_lag_output1[0] = 100 * (np.sin((np.pi*f*ctr_t)/100))
y_lag_output2[0] = 100 * (np.sin((np.pi*f*ctr_t)/100))
y_lag_output3[0] = 100 * (np.sin((np.pi*f*ctr_t)/100))
ctr_t = 1
while (ctr_t < Time_domain_max):
    Vin = 100 * np.sin(np.pi*f*ctr_t/100) #new V_Input
    prev = ctr_t - 1

    y_lag_output1[ctr_t] = lag(Vin,T,y_lag_output1[prev])
    lag_out1 = y_lag_output1[ctr_t]
    y_lead_output1[ctr_t] = lead(Vin,T,lag_out1)

    y_lag_output2[ctr_t] = lag(y_lead_output1[ctr_t], T, y_lag_output2[prev])
    lag_out2 = y_lag_output2[ctr_t]
    y_lead_output2[ctr_t] = lead(y_lead_output1[ctr_t],T,lag_out2)

    y_lag_output3[ctr_t] = lag(y_lead_output2[ctr_t], T, y_lag_output3[prev])
    lag_out3 = y_lag_output3[ctr_t]
    y_lead_output3[ctr_t] = lead(y_lead_output2[ctr_t],T,lag_out3)

    ctr_t = ctr_t + 1

#------------Plotting stuff--------------------------
lines = plt.plot(t,y_V_input,t,y_lead_output3) #plotting lines against t(time)
l1, l2 = lines
plt.setp(l2, linestyle='--', linewidth=1, color='b')
plt.setp(l1,linewidth=2, color='g')

ojo = plt.title('3 stage LEAD filter (HPF) by Temuujin')

plt.grid(True)
plt.show()


