# Background Remover

A simple web application that removes backgrounds from images using OpenCV's segmentation methods. Built with Streamlit for an easy-to-use interface.

## Features

- Upload images (supports PNG, JPG, JPEG)
- Instant background removal
- Preview processed images
- Download processed images
- Clean, intuitive interface
- Side-by-side image comparison

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd background-remover
```

2. Create a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:

```bash
streamlit run main.py
```

2. The application will start and open in your default web browser
   - Local URL (usually http://localhost:8501)
   - Network URL (for local network access)

3. Use the application:
   - Upload an image using the sidebar upload button
   - The original and processed images will be displayed
   - Download the processed image using the sidebar download button

## Technical Details

The background removal process uses the following steps:
1. Converts the image to grayscale
2. Applies binary thresholding to create a mask
3. Uses the mask to extract the foreground

## Requirements

- Python 3.6+
- streamlit
- opencv-python
- numpy
- Pillow

## Development

To modify the background removal algorithm, edit the `remove_background()` function in `main.py`. The current implementation uses a simple threshold-based approach, but you could implement more sophisticated methods like:
- Grab Cut
- Deep learning-based segmentation
- Color-based segmentation

## License

[MIT License](LICENSE)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

For support, please open an issue in the GitHub repository.