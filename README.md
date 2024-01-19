# Image assembler

This script is a simple tool for generating a mosaic image based on a set of input images. It takes a collection of images, positions them on a virtual board, and creates a mosaic output image. The script requires the OpenCV library (`cv2`) and operates via command line arguments.

## Usage

### Prerequisites
Make sure you have the following installed:
- Python
- OpenCV (`cv2`)

### Command Line Arguments
1. **Output File:** Specify the path for the output mosaic image file.
2. **Resize Factor:** Set the resize factor for the input images.
3. **X-Min, X-Max, Y-Min, Y-Max:** Define the bounding box coordinates for selecting input images.
4. **Void Image Path:** Provide the path to the background tiles.

### Example
```bash
python script.py output_mosaic.jpg 0.5 10 50 20 80 void.jpg
