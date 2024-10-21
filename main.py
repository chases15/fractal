import numpy as np
import matplotlib.pyplot as plt

#MANDELBROT SET

def mandelbrot(c, max_i):
  z = 0
  for i in range(max_i):
    if abs(z) > 2:
      return i
    z = z*z + c
  return max_i

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_i):
  x = np.linspace(xmin, xmax, width)
  y = np.linspace(ymin, ymax, width)
  mset = np.zeros((height, width))

  for i in range(height):
    for j in range(width):
      c = complex(x[j], y[i])
      mset[i, j] = mandelbrot(c, max_i)

  return mset

#parameters

xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
width, height = 1600, 1600
max_i = 300

mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_i)
plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap = "cool")
plt.colorbar()
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()
