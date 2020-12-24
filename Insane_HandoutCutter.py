from PIL import Image
import os

DirPath = 'C:/Users/tyasu/Pictures/insane/'
SavePath = 'C:/Users/tyasu/Pictures/insane-Cut/'
FileName = '8'
Extention = '.png'

files = os.listdir(DirPath)
print(files)

left = 165
upper = 33
right = 829
lower = 507

width = 664
height = 474

NextLeft = 0
NextUpper = 487

HorizonLeft = 939
HorizonUpper = 0

for file in files:

    FileName = os.path.splitext(os.path.basename(file))[0]
    print(FileName)

    for j in range(2): #横方向
        for i in range(6): #縦方向
            im = Image.open(DirPath + FileName + Extention)

            im_crop = im.crop((left + NextLeft * i + HorizonLeft * j, upper + NextUpper * i + HorizonUpper * j, right + NextLeft * i + HorizonLeft * j, lower + NextUpper * i + HorizonUpper * j))
            im_crop.save(SavePath + FileName + '_' + str(j) + '-' + str(i) + Extention, quality=95)

            #im_crop.show()