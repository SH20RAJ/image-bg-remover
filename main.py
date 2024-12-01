import gradio as gr
import cv2
import numpy as np
from PIL import Image

def remove_background(image):
    # Convert PIL Image to numpy array
    img_np = np.array(image)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    
    # Apply a binary threshold to create a mask
    _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
    
    # Extract the foreground using the mask
    bg_removed = cv2.bitwise_and(img_np, img_np, mask=mask)
    
    return Image.fromarray(bg_removed)

# Create Gradio interface
demo = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Image(type="pil", label="Background Removed"),
    title="Background Remover",
    description="Upload an image to remove its background using OpenCV's segmentation methods.",
    examples=["example1.jpg", "example2.jpg"],  # Optional: Add example images
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(share=True)
