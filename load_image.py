import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image

class LoadImageNode:
    def __init__(self):
        self.title = "Load Image"
        self.inputs = []  # No manual input required
        self.outputs = [("Loaded Image", "image")]

    def process(self):
        """
        Opens a file dialog for the user to select an image and loads it.
        Returns:
            A PIL.Image object if successful, otherwise None.
        """
        # Initialize tkinter and hide the main window
        root = tk.Tk()
        root.withdraw()

        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )

        if not file_path:
            print("⚠️ No file selected.")
            return None

        try:
            # Read the image using OpenCV
            image = cv2.imread(file_path)
            if image is None:
                print("❌ Failed to load the image. Please verify the file path and format.")
                return None

            # Convert the image from BGR (OpenCV default) to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Convert the image from a NumPy array to a PIL Image
            pil_image = Image.fromarray(image)
            return pil_image
        except Exception as e:
            print(f"❌ Error loading image: {e}")
            return None
