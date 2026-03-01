import os
from PIL import Image, ImageEnhance
import tkinter as tk
from tkinter import filedialog, messagebox

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

def enhance_image(input_path, output_path):
try:
img = Image.open(input_path)

```
    edit = img

    edit = ImageEnhance.Brightness(edit).enhance(0.8)
    edit = ImageEnhance.Contrast(edit).enhance(1.19)
    edit = ImageEnhance.Color(edit).enhance(1.34)
    edit = ImageEnhance.Sharpness(edit).enhance(2)

    edit.save(output_path)

except Exception as e:
    print(f"Error processing {input_path}: {e}")
```

def process_folder(input_folder, output_folder):
count = 0

```
for filename in os.listdir(input_folder):
    if filename.lower().endswith(SUPPORTED_EXTENSIONS):
        input_path = os.path.join(input_folder, filename)

        new_name = os.path.splitext(filename)[0] + "_edited.jpg"
        output_path = os.path.join(output_folder, new_name)

        enhance_image(input_path, output_path)
        count += 1

messagebox.showinfo("Done", f"{count} images processed successfully!")
```

def main():
root = tk.Tk()
root.withdraw()

```
input_folder = filedialog.askdirectory(title="Select Folder to Edit Images")
output_folder = filedialog.askdirectory(title="Select Folder to Save Edited Images")

if input_folder and output_folder:
    process_folder(input_folder, output_folder)
else:
    messagebox.showwarning("Cancelled", "Operation cancelled by user.")
```

if **name** == "**main**":
main()
