import binascii
import glob,os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import time
import matplotlib.pyplot as plt
model_path = './models/weights-improvement-10-0.92.hdf5'
model = load_model(model_path)
# model.load_weights(model_weights_path)
img_width, img_height = 150, 150

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
#   plt.imshow(x)
#   plt.show()
  x = img_to_array(x)
  x = x.reshape((1,) + x.shape)
  x /= 255
  array = model.predict(x)
  result = array[0,0]
  
  answer = np.argmax(result)
  if result < 0.5:
    print("{file} Predicted to be a cat")
  elif result > 0.5:
    print("{file} Predicted to be a dog")
  return answer



print("Enter path you want to scan:")
strDrive=input()
print()
print("File Name\t\t|\t\tMasqueraded?")
print("_____________________________________________________")
masqueraded=[]
i =0
for path in glob.glob(strDrive+"**/*", recursive=True):
    if os.path.isfile(path):
        name=os.path.basename(path) 
        i += 1
        with open(path, 'rb') as f:
            content = f.read()
        var=(binascii.hexlify(content).decode("utf-8"))
        if name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', )):
            print (f"{name}\t\t|\t\tNo")
        elif  var.startswith("ffd8ffdb"):
            print (f"{name}\t\t|\t\tYes  (JPG)")
            masqueraded.append(path)
#             predict(path)
        elif var.startswith("ffd8ffe000104a4649460001"):
            print (f"{name}\t\t|\t\tYes (JPG)")
            masqueraded.append(path)
#             predict(path)
        elif var.startswith("ffd8ffee"):
            print (f"{name}\t\t|\t\tYes (JPG)")
            masqueraded.append(path)
#             predict(path)
        elif var.startswith("89504e470d0a1a0a"):
            print (f"{name}\t\t|\t\tYes (PNG)")
            masqueraded.append(path)
#             predict(path)
        elif var.startswith("ffd8ffe1????457869660000"):
            print (f"{name}\t\t|\t\tYes  (JPG)")
            masqueraded.append(path)
#             predict(path)
        elif var.startswith("424D"):
            print (f"{name}\t\t|\t\tYes")
            masqueraded.append(path)
#             predict(path)
        elif var.startswith("474946383761"):
            print (f"{name}\t\t|\t\tYes (GIF)")
            masqueraded.append(path)
#             predict(path)
        else:
            print (f"{name}\t\t|\t\tNo")
print(f"{i} files scanned successfully.")
print()
print(f"{len(masqueraded)} masqueraded files scanned successfully.")
print("list of all masqueraded images:")
print()
for j in masqueraded:
    predict(j)