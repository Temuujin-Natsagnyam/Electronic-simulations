#These are the bode plots of LPF and HPF. There is frequency on the x-axis and Voltage output on the y-axis.
# The orange one is for Low-Pass filter. 
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

#-------------------tuning---------------------
T = 10
my_max_Hz = 100
increment = 0.001
start_f = 0

#---------------------------------------------
f = np.arange(start_f,my_max_Hz,increment)
y_AC_out = 0*f    #declaring array
y_phase_shift = 0*f


idx = 0
while (idx < my_max_Hz/increment):
    w = 2*np.pi*start_f   # ω angular velocity  s = jw
    ac = w*T
    AC_hyp = np.sqrt(1 + (ac)*(ac))
    AC_out = ac / AC_hyp
    phase_shift = 90 - (np.arctan(ac) * 180 / np.pi)
    y_AC_out[idx] = 100 * AC_out + 100
    y_phase_shift[idx] = phase_shift
    if ((phase_shift > -45.2) and (phase_shift < -44.9)):
        print(phase_shift)
        print( y_AC_out[idx])
    idx = idx + 1
    start_f += increment

ax.semilogx(f,y_AC_out,f,y_phase_shift)
ax.grid(True)

plt.show()
