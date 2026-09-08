import numpy as py
#import matplotlib.pyplot as plt - need to install
color=np.array([255,255,255])
brighter=np.clip(color * 1.5, 0, 255)
print(brighter)
darker=np.clip(color * 0.5, 0, 255)
print(darker)
colors=np.array([color, brighter, darker], dtype=np.uint8)