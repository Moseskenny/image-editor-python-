import os
from PIL import Image, ImageEnhance
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

def enhance_image(input_path, output_path, brightness, contrast, color, sharpness):
try:
img = Image.open(input_path)

```
    edit = img
    edit = ImageEnhance.Brightness(edit).enhance(brightness)
    edit = ImageEnhance.Contrast(edit).enhance(contrast)
    edit = ImageEnhance.Color(edit).enhance(color)
    edit = ImageEnhance.Sharpness(edit).enhance(sharpness)

    edit.save(output_path)

except Exception as e:
    print(f"Error processing {input_path}: {e}")
```

def process_folder(input_folder, output_folder, brightness, contrast, color, sharpness):
count = 0

```
for filename in os.listdir(input_folder):
    if filename.lower().endswith(SUPPORTED_EXTENSIONS):
        input_path = os.path.join(input_folder, filename)
        new_name = os.path.splitext(filename)[0] + "_edited.jpg"
        output_path = os.path.join(output_folder, new_name)

        enhance_image(input_path, output_path, brightness, contrast, color, sharpness)
        count += 1

messagebox.showinfo("Done", f"{count} images processed successfully!")
```

def start_processing():
input_folder = filedialog.askdirectory(title="Select Input Folder")
output_folder = filedialog.askdirectory(title="Select Output Folder")

```
if not input_folder or not output_folder:
    messagebox.showwarning("Cancelled", "Please select both folders.")
    return

process_folder(
    input_folder,
    output_folder,
    brightness_scale.get(),
    contrast_scale.get(),
    color_scale.get(),
    sharpness_scale.get()
)
```

# GUI Setup

root = tk.Tk()
root.title("Image Editor - Batch Enhancer")
root.geometry("500x400")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.theme_use('clam')

style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 11))
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('Horizontal.TScale', background='#2c3e50')

main = ttk.Frame(root, padding=20)
main.pack(fill="both", expand=True)

def create_slider(label_text, default, row):
label = ttk.Label(main, text=label_text)
label.grid(row=row, column=0, sticky="w")

```
scale = ttk.Scale(main, from_=0.1, to=3.0, orient="horizontal")
scale.set(default)
scale.grid(row=row, column=1, sticky="ew", padx=10)

value_label = ttk.Label(main, text=f"{default:.2f}")
value_label.grid(row=row, column=2)

def update_label(val):
    value_label.config(text=f"{float(val):.2f}")

scale.config(command=update_label)

return scale
```

brightness_scale = create_slider("Brightness", 0.8, 0)
contrast_scale = create_slider("Contrast", 1.2, 1)
color_scale = create_slider("Color", 1.3, 2)
sharpness_scale = create_slider("Sharpness", 2.0, 3)

start_btn = ttk.Button(main, text="Select Folders & Process Images", command=start_processing)
start_btn.grid(row=4, column=0, columnspan=3, pady=20, sticky="ew")

main.columnconfigure(1, weight=1)

root.mainloop()
