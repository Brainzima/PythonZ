# import os
# os.remove("kaist.txt")
# print("Data deleted successfully")

import os
if os.path.exists("kaist.png"):
    os.remove("kaist.png")
    print("Data deleted successfully")
else:
    print("File does not exist")

