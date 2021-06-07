import os
def check_images(files, valid_extensions):
  parent_path=os.listdir(files)
  for i in range (len(parent_path)):
    another_path=os.listdir(files+'/'+parent_path[i])
    for m in range (len(another_path)):
      extent=another_path[m]
      ext=extent.rfind('.')
      ext=extent[ext+1:].lower()
      if ext in valid_extensions:
        print (f"{extent} is good with {ext}")
        continue
      if ext not in valid_extensions:
        os.remove(another_path+'/'+another_path[m])
        print (f"removed {another_path[m]} having extension {ext}")
        continue
