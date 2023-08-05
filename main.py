
import numpy as np
import matplotlib.pyplot as plt

# Define reference values and 5 samples
ref = [1, 2, 3, 4, 5]
s1 = [0.8, 2.1, 2.9, 4.2, 4.6]
s2 = [1.1, 1.8, 3.1, 4.0, 5.0]
s3 = [1.3, 2.2, 2.8, 3.9, 4.8]
s4 = [0.9, 1.9, 3.0, 4.1, 4.9]
s5 = [1.2, 2.0, 2.7, 4.0, 4.7]

# Calculate statistics for each sample
std_ref = np.std(ref, ddof=1)
corr_s1 = np.corrcoef(ref, s1)[0,1]
std_s1 = np.std(s1, ddof=1)
corr_s2 = np.corrcoef(ref, s2)[0,1]
std_s2 = np.std(s2, ddof=1)
corr_s3 = np.corrcoef(ref, s3)[0,1]
std_s3 = np.std(s3, ddof=1)
corr_s4 = np.corrcoef(ref, s4)[0,1]
std_s4 = np.std(s4, ddof=1)
corr_s5 = np.corrcoef(ref, s5)[0,1]
std_s5 = np.std(s5, ddof=1)

# Plot Taylor diagram
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Add reference point
ax.plot(np.arccos(0), std_ref, 'k+', markersize=15)

# Add each sample to the plot
ax.plot(np.arccos(corr_s1), std_s1, 'bo', markersize=10, label='Sample 1')
ax.plot(np.arccos(corr_s2), std_s2, 'go', markersize=10, label='Sample 2')
ax.plot(np.arccos(corr_s3), std_s3, 'ro', markersize=10, label='Sample 3')
ax.plot(np.arccos(corr_s4), std_s4, 'mo', markersize=10, label='Sample 4')
ax.plot(np.arccos(corr_s5), std_s5, 'co', markersize=10, label='Sample 5')

# Set the radial limits and gridlines
ax.set_ylim(0, 6)
ax.grid(True)

# Add labels and legend
ax.set_xticklabels(['0', '$\pi/4$', '$\pi/2$', '$3\pi/4$', '$\pi$'])
ax.set_xlabel('Correlation Coefficient')
ax.set_ylabel('Standard Deviation')
ax.set_title('Taylor Diagram')
ax.legend(loc='best')

plt.show()
