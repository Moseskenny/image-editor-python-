
from PIL import Image ,ImageEnhance, ImageFilter
import sys
import os
from tkinter import filedialog


path = filedialog.askdirectory(title="select folder to edit")
pathout= filedialog.askdirectory(title="Select a Folder to save edited images")


for filename in os.listdir(path): 

    img = Image.open(f"{path} /{filename}")

    edit = img
    
    brightness =ImageEnhance.Brightness(edit)
    edit =brightness.enhance(0.8)

    contrast=ImageEnhance.Contrast(edit)
    edit=contrast.enhance(1.19)

    color=ImageEnhance.Color(edit)
    edit=color.enhance(1.34)

    sharpness=ImageEnhance.Sharpness(edit)
    edit=sharpness.enhance(2)

    new_name=os.path.splitext(filename)[0]
    
    edit.save(f'{pathout}/{new_name}_edited.jpg')



