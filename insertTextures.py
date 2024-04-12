# insertTextures.py

from PIL import Image
import sys

if (len(sys.argv) < 4): 
  exit(1)

texturetemplate = Image.open(sys.argv[1])
insertedimage = Image.open(sys.argv[2])
ow, oh = insertedimage.size

if (sys.argv[2][0] == "F" or sys.argv[2][0]=="E"):
  newImage = Image.new(insertedimage.mode, (389,389))
if (sys.argv[2][0] == "M" or sys.argv[2][0]=="P"):
  newImage = Image.new(insertedimage.mode, (389,389))
if (sys.argv[2][0] == "W"):
  newImage = Image.new(insertedimage.mode, (600,600), (0,0,0))
newImage.paste(insertedimage, (0,0, ow, oh))

print("Sign type is " + sys.argv[2][0])
if (sys.argv[2][0] == "W"):
  insertedimagerot = newImage.rotate(210)
else:
  insertedimagerot = newImage.rotate(-90)

if (sys.argv[2][0] == "F" or sys.argv[2][0]=="E"): 
  insertedimageres = insertedimagerot.resize((255,255))
if (sys.argv[2][0] == "M" or sys.argv[2][0]=="P"):
  insertedimageres = insertedimagerot.resize((495,495))
if (sys.argv[2][0] == "W"):
  insertedimageres = insertedimagerot.resize((840,840))

image_copy = texturetemplate.copy()

position = ((385), (257))

if (sys.argv[2][0] == "F" or sys.argv[2][0]=="E"): position = ((385), (257))
if (sys.argv[2][0] == "M" or sys.argv[2][0]=="P"): position = ((10), (522))
if (sys.argv[2][0] == "W"): position = ((-275), (350))

image_copy.paste(insertedimageres, position, mask=insertedimageres)
image_copy.save(sys.argv[3])

