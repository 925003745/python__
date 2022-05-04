import time

from PIL import ImageGrab

time.sleep(2)
size = (734, 463, 1420, 775)
pic = ImageGrab.grab(size)
pic.save(r"D:\Capture Information file (python)\PrtSc\picture.jpg")
# pic.show()

