#https://stickershop.line-scdn.net/stickershop/v1/sticker/6713345/android/sticker.png

import urllib.request
"""
How to save free images
Step 1. replace DIRECTORY variable
Step 2. replace NAME variable
"""
DIRECTORY = SET_DIR_HERE
FILENAME = SET_FILE_NAME_HERE
counter = 0

for i in range(6713300, 6713370):
    number = str(i)
    ID = str(counter)
    urllib.request.urlretrieve(f"https://stickershop.line-scdn.net/stickershop/v1/sticker/{number}/android/sticker.png", f"static/img/{DIRECTORY}/{FILENAME}-{ID}.jpg")
    counter += 1




print('> ....Saving Process Completed')
