# Background Remover 🌌

This is a Streamlit-based web application designed to remove backgrounds from images effortlessly. The app uses the rembg library for background removal and provides an intuitive, user-friendly interface for uploading and downloading images.

## Features
* **Upload Images**: Accepts .jpg, .jpeg, and .png formats.

* **Background Removal**: Removes the background of uploaded images seamlessly.

* **Download Option**: Provides the processed image in .png format for download.

* **Dark Mode UI**: Comes with a visually appealing dark theme and gradient styling.

* **Cancel Option**: Allows users to cancel the upload process at any time.

* **Responsive Design**: Works well on both desktop and mobile devices.

## Technologies Used
* **Python**: Core programming language.

* **Streamlit**: For building the interactive web application.

* **Pillow (PIL)**: For image handling and manipulation.

* **rembg**: For removing image backgrounds.

* **Custom CSS**: For enhanced styling and responsiveness.

## Installation

#### Prerequisites
- Python 3.7 or higher.
- Virtual environment (optional but recommended).

## Steps
**Clone the repository**:

```bash
git clone https://github.com/RaksithSivakumar/BackgroundRemover.git
cd BackgroundRemover
```
**Install the required packages**:

```bash
pip install -r requirements.txt
```
**Run the application**:

```bash
streamlit run app.py
Open the application in your browser (usually at http://localhost:8501).
```

## How to Use
- Upload an image by clicking on the "Upload your image here" button.
- Wait while the app processes your image.
- View the original and processed images side-by-side.
- Download the processed image by clicking on the "⬇️ Download Background Removed Image" button.

## About the Developer
Name: Raksith
- **LinkedIn**: [Raksith S.S](https://www.linkedin.com/in/raksith-s-s-2aa49928b/)
- **GitHub**: [RaksithSivakumar](https://github.com/RaksithSivakumar)


## Future Enhancements
- Add support for batch processing multiple images.
- Include additional customization options like resizing and cropping.
- Explore AI-based enhancement for more accurate edge detection.
