import cv2
import os
import string
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to upload an image
def upload_image():
    Tk().withdraw()  # Prevents the root window from appearing
    filename = askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    return filename

# Upload the image
image_path = upload_image()
if not image_path:
    print("No image selected. Exiting.")
    exit()

img = cv2.imread(image_path)

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

# Encrypt the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    # Decrypt the message from the image
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")
