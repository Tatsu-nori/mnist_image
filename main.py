import mnist_img
import numpy as np
from PIL import Image

def main():
  img, num = mnist_img.load_data_wrapper()
  for i in range(10):
    np_d = np.array(img[i]).reshape(28, -1)
    np_d = np_d * 256
    img_d = Image.fromarray(np_d)
    img_d = img_d.convert("L")
    img_d.save("./img/mnist_" + str(i).zfill(2) + "_" + str(num[i]) + ".bmp")

if __name__ == "__main__":
  main()


