import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from scipy.ndimage import morphology

image = np.load('ps.npy')

mask0 = np.array([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
])

mask1 = np.array([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,0,0,1,1],
    [1,1,0,0,1,1]
])

result = morphology.binary_opening(image, mask0)
labeled = label(result)
print(mask0)
print(np.max(labeled),' figures with this mask')
image -= result
res=0
for i in range(4):
  result = morphology.binary_opening(image, mask1)
  labeled = label(result)
  res += np.max(labeled)
  mask1 = np.rot90(mask1)
print()
print(mask1)
print(res,' figures with this mask')