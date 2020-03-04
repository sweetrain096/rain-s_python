import os
from PIL import Image

path = "C:/Users/한단비/Pictures/Screenshots/"

file_list = os.listdir(path)
print("file_list : {}".format(file_list))

for file in file_list:
    if file[-1] != "g":
        continue
    # print(path+file[:-3])
    im = Image.open(path+file)
    # im.save(path+file[:-3]+'jpeg',"JPEG", quality=85)
    cropped_img = im.crop((294, 161, 614, 651))
    cropped_img.save(path+file, "PNG", quality=85)
    # print(im.size)