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
## 🎛 Adjustable Image Controls (GUI Sliders)

This application now includes **interactive sliders** that let you control how your images are enhanced before processing.

### 🎚 Available Controls

| Slider     | Effect                        |
| ---------- | ----------------------------- |
| Brightness | Adjust light/dark levels      |
| Contrast   | Increase or decrease contrast |
| Color      | Control color intensity       |
| Sharpness  | Adjust image clarity          |

---

### 🔧 How to Use

1. Run the application
2. Adjust the sliders to your desired values
3. Click **"Select Folders & Process Images"**
4. Choose input and output folders
5. Images will be processed using your selected settings

---

### 💡 Recommended Values

| Effect     | Suggested Range |
| ---------- | --------------- |
| Brightness | 0.7 – 1.3       |
| Contrast   | 1.0 – 1.5       |
| Color      | 1.0 – 1.5       |
| Sharpness  | 1.5 – 2.5       |

---

This makes the tool flexible and allows you to fine-tune image output visually.


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
