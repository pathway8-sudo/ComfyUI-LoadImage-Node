import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image

class LoadImageNode:
    def __init__(self):
        self.title = "Load Image"
        self.inputs = []  # No manual input required
        self.outputs = [("Loaded Image", "image")]  # Outputs an image

    def process(self):
        """
        Opens a file dialog for the user to select an image and loads it.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

        if not file_path:
            print("⚠️ No file selected.")
            return None

        try:
            # Read image using OpenCV
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
            pil_image = Image.fromarray(image)  # Convert to PIL Image
            return pil_image
        except Exception as e:
            print(f"❌ Error loading image: {e}")
            return None

