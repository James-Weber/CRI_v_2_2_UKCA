import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
T=np.linspace(250,310,1000)

# CRI v2.2 rate coefficient for MeOO + RO2 = MeOH (or HCHO)
def meoo_ro2_meoh(T):
    return 2*1.03e-13*np.exp(365./T)*0.5*(1-7.18*np.exp(-885./T))

y=meoo_ro2_meoh(T)

def fit_func1(x,a,b,c):
    b=float(b)
    c=float(c)
    return aa*np.exp(-b/T)*(T/300)**c

popt, pcov = curve_fit(fit_func1, T, y)

# Plot CRI v2.2 rate coefficient and fitted rate coefficient
plt.figure(dpi=100)
plt.plot(T,meoo_ro2_meoh(T))
plt.plot(T,popt[0]*np.exp(-popt[1]/T)*(T/300)**popt[2],label='meoo_ro2_meoh')

# Optionally include plot explicitly showing determined fitting parameters for sanity check! 
# plt.plot(T,5.36177136e-12*np.exp(- 9.62182631e+02/T)*(T/300)**-6.15016402e+00)
plt.legend()
plt.show()

# Print fitting parameters 
print(popt)

# Calculate Root Mean Square Error over 250-310 temperature range 
rmse=np.sqrt(np.nanmean((5.36e-12*np.exp(-962/T)*(T/300)**(-6.15)-meoo_ro2_meoh(T))**2))
print(rmse)

# Print mean percentage error and max percentage error 
print(np.nanmean(100*rmse/meoo_ro2_meoh(T)))
print(np.max(100*rmse/meoo_ro2_meoh(T)))
