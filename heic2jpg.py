# import subprocess
# import os
# import io
# import whatimage
# import pyheif
# import traceback
# from PIL import Image
 
 
# # def decodeImage(bytesIo):
# #     try:
# #         fmt = whatimage.identify_image(bytesIo)
# #         # print('fmt = ', fmt)
# #         if fmt in ['heic']:
# #             i = pyheif.read_heif(bytesIo)
# #             # print('i = ', i)
# #             # print('i.metadata = ', i.metadata)
# #             pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
# #             # print('pi = ', pi)
# #             pi.save('heeh.jpg', format="jpeg")
# #     except:
# #         traceback.print_exc()
 
 
# # def read_image_file_rb(file_path):
# #     with open(file_path, 'rb') as f:
# #         file_data = f.read()
# #     return file_data
 

# def heicTOjpg(filename):
#     with open(filename, 'rb') as f:
#         file_data=f.read()
#     # try:
#         fmt = whatimage.identify_image(file_data)
#         # print('fmt = ', fmt)
#         # if fmt in ['heic']:
#         i = pyheif.read_heif(file_data)
#         # print('i = ', i)
#         # print('i.metadata = ', i.metadata)
#         pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
#         # print('pi = ', pi)
#         file_name = filename.split('/')[2].split('.')[0]
#         print(file_name)
#         tosave = "./heictojpg/"+file_name + '.jpg'
#         pi.save(tosave, format="jpeg")
#         # else:
#         #     print("corrupt")
#     # except:
#     #     print("except")
#     #     traceback.print_exc()

 
# if __name__ == "__main__":
#     file_path = './heic/'
#     print('file_path = ', file_path)
#     for idx, file in enumerate(os.listdir(file_path)):
#         filename = file_path + file
#         print("filename", filename)
#         heicTOjpg(filename)
#         # data = read_image_file_rb(filename)
#         # print('data = ', data)
#         # decodeImage(data)




from wand.image import Image
import os

SourceFolder="./heic"
TargetFolder="./heictojpg"

for file in os.listdir(SourceFolder):
  SourceFile=SourceFolder + "/" + file
  TargetFile=TargetFolder + "/" + file.replace(".heic",".JPG")

  img=Image(filename=SourceFile)
  img.format='jpg'
  img.save(filename=TargetFile)
  img.close()
