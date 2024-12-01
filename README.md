# Background Remover

A simple web application that removes backgrounds from images using OpenCV's segmentation methods. Built with Gradio for an easy-to-use interface.

## Features

- Upload images (supports PNG, JPG, JPEG)
- Instant background removal
- Preview processed images
- Download processed images
- Example images included
- Public sharing capability

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
python main.py
```

2. The application will start and provide two URLs:
   - Local URL (usually http://127.0.0.1:7860)
   - Public URL (temporary, for sharing)

3. Open the provided URL in your web browser

4. Use the application:
   - Upload an image using the upload button
   - The processed image will appear automatically
   - Download the processed image if desired

## Technical Details

The background removal process uses the following steps:
1. Converts the image to grayscale
2. Applies binary thresholding to create a mask
3. Uses the mask to extract the foreground

## Requirements

- Python 3.6+
- gradio
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