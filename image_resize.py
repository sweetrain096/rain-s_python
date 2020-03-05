import os
from PIL import Image

def png_to_jpg(png_path, target_img):
    # target_img.show()
    fill_color = None
    Img = target_img.convert('RGB')
    jpg_path = path + png_path[:-3] + 'jpg'
    Img.save(jpg_path, 'JPEG', quality=80)

    # if target_img.mode in ('RGBA', 'LA'):
    #     background = Image.new(target_img.mode[:-1], target_img.size, fill_color)
    #     background.paste(target_img, target_img.split()[-1])
    #     target_img = background
    #
    # target_img.save(jpg_path+'1', 'JPEG', quality=90)


path = "C:/Users/한단비/Pictures/Screenshots/"

file_list = os.listdir(path)
print("file_list : {}".format(file_list))


for file in file_list:
    if file[-1] != "g":
        continue
    # print(path+file[:-3])
    im = Image.open(path+file)
    # png_to_jpg(file, im)

    # im.save(path+file[:-3]+'jpeg',"JPEG", quality=85)
    cropped_img = im.crop((468, 60, 896, 712))
    # cropped_img.show()
    # cropped_img.save(path+file, "PNG", quality=85)
    png_to_jpg(file, cropped_img)

    # print(im.size)