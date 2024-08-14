# Delete a File

import os
'''os.remove("./files/demofile.txt")'''


if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



  # Delete Folder

  os.rmdir("myfolder")