import numpy as np
data = np.load("sample_treated.npz")
outputs = data['outputs']

print(np.max(outputs,axis=1)>=2*np.min(outputs,axis=1)) # if we were to only check if max is at least twice the min
print(np.max(outputs,axis=1)>=2*outputs[:,0]) # if we were to check if at least once the object doubled compared to its original size