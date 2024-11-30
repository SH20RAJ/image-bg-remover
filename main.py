import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Background Remover",
    page_icon="🖼️",
    layout="wide"
)

st.title("🎨 Background Remover (Python 3.13-Compatible)")
st.markdown("""
Effortlessly remove backgrounds using OpenCV's segmentation methods.  
- **Upload** your image.  
- **Preview** the background-removed image.  
- **Download** the result!
""")

# Sidebar for uploading
st.sidebar.header("📂 Upload Image")
uploaded_file = st.sidebar.file_uploader("Upload an image (PNG, JPG)", type=["png", "jpg", "jpeg"])

# Helper function to remove the background
def remove_background(image):
    # Convert to numpy array
    img_np = np.array(image)

    # Convert image to grayscale
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    # Apply a binary threshold to create a mask
    _, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)

    # Extract the foreground using the mask
    bg_removed = cv2.bitwise_and(img_np, img_np, mask=mask)

    return Image.fromarray(bg_removed)

# Main app area
if uploaded_file:
    st.subheader("📥 Original Image")
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Background Removal
    with st.spinner("Removing background..."):
        processed_image = remove_background(image)
        st.success("Background removed successfully!")

    # Display the output
    st.subheader("📤 Background Removed")
    st.image(processed_image, caption="Processed Image", use_column_width=True)

    # Download Button
    st.sidebar.subheader("💾 Download Processed Image")
    output_buffer = st.sidebar.download_button(
        label="Download",
        data=processed_image.tobytes(),
        file_name="background_removed.png",
        mime="image/png",
    )
else:
    st.info("Please upload an image to proceed.")

# Footer
st.markdown("---\nBuilt with ❤️ using Streamlit and OpenCV.")
