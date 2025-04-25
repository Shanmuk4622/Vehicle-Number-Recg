# License Plate Detection Project

## Overview
This project implements an object detection system using the YOLO (You Only Look Once) model to detect car license plates from images and video feeds. The system is designed to be modular, with separate components for file operations, mouse event handling, video processing, and model management. The detected license plates are saved along with timestamps for further analysis.

---

## Features
- **Real-Time License Plate Detection**: Detects license plates in video streams using the YOLO model.
- **OCR Integration**: Extracts text from detected license plates using Tesseract OCR.
- **Modular Design**: Organized into reusable components for better maintainability.
- **Data Logging**: Saves detected license plates and timestamps to a file for future reference.
- **Customizable Settings**: Easily configure paths, model weights, and other parameters.

---

## Output
![Imange](Extra%20Files/screenshot.png)

---

## Project Structure
```
Number Plate Recg/
├── main.py                # Entry point of the application
├── README.md              # Documentation for the project
├── requirements.txt       # List of dependencies
├── config/
│   ├── __init__.py        # Initializes the config package
│   └── settings.py        # Configuration settings like paths and constants
├── data/
│   ├── coco1.txt          # Class labels for the object detection model
│   ├── car_plate_data.txt # Stores detected car plate numbers with timestamps
│   ├── 04.jpg             # Image file for testing
│   ├── 10.jpg             # Image file for testing
│   ├── 11.jpg             # Image file for testing
│   └── video1.mp4         # Video file for processing
├── utils/
│   ├── __init__.py        # Initializes the utils package
│   ├── file_operations.py # Handles file-related operations
│   ├── mouse_callbacks.py # Contains the RGB function
│   └── video_processing.py # Handles video processing logic
├── weights/
│   ├── best.pt            # Weights for the YOLO model
│   └── yolov10m.pt        # Alternative weights for the YOLO model
```

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using:
```bash
git clone <repository-url>
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Configure Settings
Update the `config/settings.py` file with the correct paths to your data and weights if necessary:
```python
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
MODEL_PATH = 'weights/best.pt'
VIDEO_PATH = 'data/video1.mp4'
OUTPUT_FILE = 'data/car_plate_data.txt'
AREA = [(27, 350), (16, 500), (1015, 400), (992, 350)]
```

### 4. Run the Application
Execute the main application:
```bash
python main.py
```

---

## Usage
- The application will process the video file specified in the settings and display the detected license plates in real-time.
- Detected license plates will be saved in `data/car_plate_data.txt` along with timestamps.

---

## Configuration Details

### `config/settings.py`
This file contains all the configurable parameters for the project:
- **TESSERACT_CMD**: Path to the Tesseract OCR executable.
- **MODEL_PATH**: Path to the YOLO model weights.
- **VIDEO_PATH**: Path to the input video file.
- **OUTPUT_FILE**: Path to the file where detected license plates will be saved.
- **AREA**: Coordinates defining the region of interest for detection.

---

## Key Components

### 1. `main.py`
The entry point of the application. It orchestrates the following:
- Initializes Tesseract OCR.
- Clears the output file before starting.
- Sets up mouse callbacks for debugging.
- Processes the video using the `process_video` function.

### 2. `utils/`
Contains utility modules:
- **`file_operations.py`**: Handles file reading, writing, and clearing.
- **`mouse_callbacks.py`**: Contains the `RGB` function to handle mouse events.
- **`video_processing.py`**: Processes the video, detects license plates, and extracts text using OCR.

### 3. `config/`
Contains configuration files:
- **`settings.py`**: Stores paths, constants, and other settings.

---

## Example Output
### Detected License Plates
The detected license plates are saved in `data/car_plate_data.txt` in the following format:
```
ABC1234    2025-04-24 14:30:15
XYZ5678    2025-04-24 14:31:10
```

### Real-Time Display
The application displays the video feed with:
- Bounding boxes around detected license plates.
- Cropped license plate images for OCR.

---

## Dependencies
The project requires the following Python packages:
- `opencv-python`
- `numpy`
- `pandas`
- `ultralytics`
- `pytesseract`
- `cvzone`

Install them using:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### 1. Import Errors
If you encounter import errors, ensure the project directory is in the Python path. You can add it dynamically in `main.py`:
```python
import sys
sys.path.append(r'c:\Users\shanm\PycharmProjects\APSCSC_Hackathon\Number Plate Recg')
```

### 2. Tesseract Not Found
Ensure Tesseract OCR is installed and the path is correctly set in `config/settings.py`:
```python
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 3. Missing Files
Ensure all required files (e.g., `weights/best.pt`, `data/video1.mp4`) are present in their respective directories.

---

## Future Enhancements
- Add support for multiple video inputs.
- Improve OCR accuracy with preprocessing techniques.
- Implement a web interface for easier interaction.
- Add logging for better debugging and monitoring.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- [YOLO](https://github.com/ultralytics/yolov5) for the object detection model.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text recognition.
- OpenCV and NumPy for image and video processing.

---


