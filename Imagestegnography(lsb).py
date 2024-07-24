#!/usr/bin/env python
# coding: utf-8

# In[96]:


import os # for file operation
import cv2 #for  image accessing
import string # for text manipulation
from PIL import Image #for handling images

#convert message to binary
def message_to_binary(message):
    binary_message = ''.join(format(ord(char), '08b')for char in message) # Convert each character to its binary representation
    return binary_message

# Hide message in an image
def hide_message(image_path,message):
    img = Image.open(image_path)  # Open the image file
    binary_message = message_to_binary(message)  # Convert message to binary
    binary_message += '1111111111111110' # Add delimiter to indicate end of the message
    
    if img.mode !='RGB':
        img = img.convert('RGB') # Ensure image is in RGB mode
        
    width,height = img.size
    index =0
    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            r,g,b=img.getpixel((x,y)) # Get the RGB values of the pixel
            if index <len(binary_message):
                  # Modify the least significant bit of each color channel with the message bit
                img.putpixel((x, y), (r & 254 | int(binary_message[index]), 
                                      g & 254 | int(binary_message[index]), 
                                      b & 254 | int(binary_message[index])))
                index += 3  # Move to the next set of bits in the message
            else:
                break
                
    img_with_message = os.path.join(os.path.dirname(image_path),"encrypted_image.png")  # Save the image with a new name
    img.save(img_with_message)
    os.startfile(img_with_message) #Open the new image file
    return img_with_message

# Extract hidden message from an image
def messages(image_path):
   
    img = os.startfile(image_path) # Open the image file
    binary_message = ''
    
    # Iterate over each pixel in the image
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))  # Get the RGB values of the pixel
            binary_message += (bin(r)[-1] + bin(g)[-1] + bin(b)[-1])  # Extract the least significant bit from each color channel

    delimiter_index = binary_message.find('1111111111111110')  # Find the delimiter that indicates the end of the message
    if delimiter_index == -1:
        raise ValueError("No hidden message found in image.")

    binary_message = binary_message[:delimiter_index] # Extract the message up to the delimiter

    message = ''
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2)) # Convert binary to characters
    return message
                
    
if __name__ == "__main__":
    image_path=r'C:\Users\Devi Priya\OneDrive\Desktop\cyber security\car.jpg'
    if not os.path.isfile(image_path):
        printf("Image is not found. check the file path and make sure the image exists")
        exit()
        
    process = input("enter 1 for encryption and 2 for decryption: ")
   
    if process == '1':
        message= input("Enter the message to be hidden:")
        password1 = input("Please! Create your secret password")
        encrypted_image = hide_message(image_path,message)
        print(f"Message is successfully hidden in {encrypted_image}")
        
    elif process == '2':
        password2 =input("please! enter the password:")
        if password2 != password1:
            print("Please enter the correct password!")
        else :
            img = os.startfile(image_path) 
            ans = message
            print(f"The Secret message is : {ans}")
    else :
        print("Invalid input. please enter either 1 or 2.")
    


# In[ ]:




