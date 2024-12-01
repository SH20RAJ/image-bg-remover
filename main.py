import streamlit as st
from rembg import remove
from PIL import Image
import io

# Page Configuration
st.set_page_config(
    page_title="Background Remover",
    page_icon="🖼️",
    layout="wide"
)

st.title("🎨 Background Remover")
st.markdown("""
Effortlessly remove backgrounds from images using AI-powered background removal.  
- **Upload** your image.  
- **Preview** the background-removed image.  
- **Download** the result!
""")

def remove_background(image):
    # Remove background using rembg
    return remove(image)

# Sidebar for uploading
st.sidebar.header("📂 Upload Image")
uploaded_file = st.sidebar.file_uploader("Upload an image (PNG, JPG)", type=["png", "jpg", "jpeg"])

# Main app area
if uploaded_file:
    st.subheader("📥 Original Image")
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Background Removal
    with st.spinner("Removing background... This may take a moment."):
        processed_image = remove_background(image)
        st.success("Background removed successfully!")

    # Display the output
    st.subheader("📤 Background Removed")
    st.image(processed_image, caption="Processed Image", use_column_width=True)

    # Download Button
    st.sidebar.subheader("💾 Download Processed Image")
    
    # Convert PIL image to bytes
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.sidebar.download_button(
        label="Download Image",
        data=byte_im,
        file_name="background_removed.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to proceed.")

# Footer
st.markdown("---\nBuilt with ❤️ using Streamlit and rembg")
