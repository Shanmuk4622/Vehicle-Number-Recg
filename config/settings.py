TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
MODEL_PATH = 'weights/best.pt'
VIDEO_PATH = 'data/video1.mp4'
OUTPUT_FILE = 'data/car_plate_data.txt'

AREA = [(27, 350), (16, 500), (1015, 400), (992, 350)]

# Load class list
try:
    with open('data/coco1.txt', 'r') as file:
        CLASS_LIST = file.read().split("\n")
except FileNotFoundError:
    print("Error: coco1.txt not found.")
    CLASS_LIST = []