import os

os.chdir('C:/Users/student/Desktop/DBs_python/SSAFY')

files = os.listdir()
print(type(os.listdir()))

for file in files :
    #os.rename(file, "samsung"+file)
    os.rename(file, file.replace("SSAFY","samsung"))