import matplotlib.pyplot as plt
import numpy as np

def negate(B):
    array = B.copy()
    array[np.where(array == 1)] = -1
    return array

def check(B, y, x):
    if not 0 <= x < B.shape[0]:
        return False
    if not 0 <= y < B.shape[1]:
        return False
    if B[y, x] != 0:
        return True
    return False


def neighbors2(B, y, x):
    left = y, x-1
    top = y - 1, x
    if not check(B, *left):
        left = None
    if not check(B, *top):
        top = None
    return left, top

def exists(neighbors):
    return not all([n is None for n in neighbors])

def find(label, linked):
    j = label
    while linked[j] != 0:
        j = linked[j]
    return j

def union(label1, label2, linked):
    j = find(label1, linked)
    k = find(label2, linked)
    if j != k:
        linked[k] = j


def two_pass_labeling(binary_image):
    labeled = np.zeros_like(binary_image)
    label = 1
    linked = np.zeros(len(binary_image), dtype="uint")
    for y in range(binary_image.shape[0]):
        for x in range(binary_image.shape[1]):
            if binary_image[y, x] != 0:
                ns  = neighbors2(binary_image, y, x)
                if ns[0] is None and ns[1] is None:
                    m = label
                    label += 1
                else:
                    lbs = [labeled[i] for i in ns if i is not None]
                    m = min(lbs)
                labeled[y, x] = m

                for n in ns:
                    if n is not None:
                        lb = labeled[n]
                        if lb != m:
                            union(m, lb, linked)


    #print(linked[:20])
    mas={0:0}
    k=1
    for y in range(binary_image.shape[0]):
      for x in range(binary_image.shape[1]):
        if binary_image[y,x]!=0:
          new_label=find(labeled[y,x], linked)
          if(new_label !=labeled[y,x]):
            labeled[y,x]=new_label
    for y in range(labeled.shape[0]):
      for x in range(labeled.shape[1]):
        if(labeled[y,x]!=0 and not(labeled[y,x] in mas)):
          mas[labeled[y,x]]=k
          k=k+1
    for y in range(labeled.shape[0]):
      for x in range(labeled.shape[1]):
        labeled[y,x]=mas[labeled[y,x]]
    return labeled


if __name__ == "__main__":
    B = np.zeros((20, 20), dtype='int32')
    
    B[1:-1, -2] = 1
    
    B[1, 1:5] = 1
    B[1, 7:12] = 1
    B[2, 1:3] = 1
    B[2, 6:8] = 1
    B[3:4, 1:7] = 1
    
    B[7:11, 11] = 1
    B[7:11, 14] = 1
    B[10:15, 10:15] = 1
    
    B[5:10, 5] = 1
    B[5:10, 6] = 1

    LB = two_pass_labeling(B)
    
    print("Labels - ", list(set(LB.ravel()))[1:])
    
    
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(B, cmap="hot")
    plt.colorbar(ticks=range(int(2)))
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(LB.astype("uint8"), cmap="hot")
    plt.colorbar()
    plt.axis("off")
    plt.tight_layout()
    plt.show()
