import cv2
import numpy as np
from datetime import datetime
from utils.mouse_callbacks import RGB
from utils.video_processing import process_video
from utils.file_operations import clear_file
from config.settings import TESSERACT_CMD, MODEL_PATH, VIDEO_PATH, AREA, OUTPUT_FILE, CLASS_LIST

# Set up Tesseract OCR path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

# Clear the output file before starting
clear_file(OUTPUT_FILE)

# Set up mouse callback
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Process the video
processed_numbers = set()
process_video(VIDEO_PATH, AREA, processed_numbers, OUTPUT_FILE)