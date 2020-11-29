################################################################
# reference
# https://www.geeksforgeeks.org/python-pil-image-resize-method/
################################################################

################################################################
# prerequisite
# pip3 install pillow
################################################################

# Improting Image class from PIL module  
from PIL import Image  
  
# Opens a image in RGB mode  
im = Image.open(r"/home/hadoop/projects/work/images.png")
width, height = im.size  
print('orginal image size', width,'x',height)
newsize = (int(width/10), int(height/10)) 
im1 = im.resize(newsize) 
width, height = im1.size  
print('new image size', width,'x',height)
im1.save("/home/hadoop/projects/work/images.tumbnail.png","PNG")
