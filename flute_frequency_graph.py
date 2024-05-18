from matplotlib import pyplot as plt
import numpy as np

# Define data.
lengths = [0.262, 0.278, 0.323, 0.395, 0.395, 0.421, 0.451, 0.600, 0.483] #from embouchure
frequencies = [554, 493, 440, 392, 415, 349, 329, 293, 311]
recips = [1/f for f in frequencies]

lengths2 = [0.262, 0.278, 0.323, 0.395, 0.395, 0.421, 0.451, 0.483] #from embouchure
frequencies2 = [554, 493, 440, 392, 415, 349, 329, 311]
recips2 = [1/f for f in frequencies2] #with the eighth data point removed

# Make plot.
plt.scatter(lengths2, recips2, edgecolor='none', s=40)
plt.xlim([0,max(lengths2)*1.1])
plt.ylim([0,max(recips2)*1.1])

#Make regression.
#coef = np.polyfit(lengths2,recips2,1) #1 for linear
#poly1d_fn = np.poly1d(coef)

#xrange = np.arange(0,max(lengths)*1.1,0.01)
#plt.plot(xrange,poly1d_fn(xrange),'--k')
#print(coef)

# Customize plot.
plt.title("Reciproal of Frequencies vs. Length of the tube for flute" , fontsize=16)
plt.xlabel('Lengths from Embouchure (m)', fontsize=12)
plt.ylabel('Reciprocals of Frequencies (s)', fontsize=12)
plt.tick_params(axis='both', labelsize=12)

# Show plot.
plt.show()