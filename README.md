# 🎨 Image Editor (Batch Image Enhancement Tool)

A Python-based batch image editor that automatically enhances brightness, contrast, color, and sharpness for all images in a selected folder.

This tool is built using Pillow and provides a simple graphical interface for selecting input and output folders.

---

## ✨ Features

* 📂 Select input & output folders using GUI dialog
* 🖼 Batch process multiple images at once
* 🎚 Automatically applies:

  * Brightness adjustment
  * Contrast enhancement
  * Color boost
  * Sharpness improvement
* 💾 Saves edited images with `_edited` suffix
* ⚡ Fast and lightweight

---
## 🎛 Customization (Adjust Editing Strength)

You can easily customize how the images are enhanced by modifying the values inside the code.

Open the file `editor.py` and locate this section:

```python
edit = ImageEnhance.Brightness(edit).enhance(0.8)
edit = ImageEnhance.Contrast(edit).enhance(1.19)
edit = ImageEnhance.Color(edit).enhance(1.34)
edit = ImageEnhance.Sharpness(edit).enhance(2)
```

### 🔧 What each value means

| Parameter  | Effect                                   |
| ---------- | ---------------------------------------- |
| Brightness | < 1 = darker, > 1 = brighter             |
| Contrast   | < 1 = less contrast, > 1 = more contrast |
| Color      | < 1 = less color, > 1 = more vibrant     |
| Sharpness  | < 1 = softer, > 1 = sharper              |

---

### ✏ Example Custom Settings

If you want brighter and sharper images, you can change to:

```python
edit = ImageEnhance.Brightness(edit).enhance(1.2)
edit = ImageEnhance.Contrast(edit).enhance(1.3)
edit = ImageEnhance.Color(edit).enhance(1.5)
edit = ImageEnhance.Sharpness(edit).enhance(2.5)
```

---

### 💡 Tip

* Start with small changes (0.1–0.3 increments)
* Very high values may reduce image quality

This makes the tool flexible for different types of images.


## 📸 Example

Before editing:

```id="k7t63g"
image1.jpg
image2.png
```

After editing:

```id="3r5t2v"
image1_edited.jpg
image2_edited.jpg
```

---

## 📂 Project Structure

```id="q9cshe"
image-editor-python/
│── editor.py
│── README.md
│── requirements.txt
│── LICENSE
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone repository

```bash id="cs9qbl"
git clone https://github.com/Moseskenny/image-editor-python-.git
cd image-editor-python-
```

### 2. Install dependencies

```bash id="b8n4q1"
pip install -r requirements.txt
```

---

## 🚀 How to Use

Run the script:

```bash id="4sg0or"
python editor.py
```

Then:

1. Select the input image folder
2. Select output folder
3. All images will be automatically enhanced and saved

---

## 🧰 Technologies Used

* Python
* Pillow (PIL)
* Tkinter (file dialog)

---

## 📦 Requirements

```id="8hmtcd"
Pillow
```

---

## 📜 License

MIT License

---

## 👤 Author

**Moses Kenny**
GitHub: https://github.com/Moseskenny

---

## ⭐ Support

If you like this project, please ⭐ the repository!
