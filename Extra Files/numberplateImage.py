import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
import pytesseract
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

model = YOLO('../weights/best.pt')

# Load the image
image_path = '../data/04.jpg'  # Replace with your image file path
frame = cv2.imread(image_path)
frame = cv2.resize(frame, (1020, 500))

# Load class list
my_file = open("../data/coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n")

# Define the area of interest
area = [(27, 350), (16, 500), (1015, 400), (992, 350)]

# Set to store processed numbers
processed_numbers = set()

# Open file for writing car plate data
with open("../data/car_plate_data.txt", "a") as file:
    file.write("NumberPlate\tDate\tTime\n")  # Writing column headers

# Function to display mouse position
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = (x, y)
        temp_frame = frame.copy()
        cv2.putText(temp_frame, f"Position: {point}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Image", temp_frame)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', RGB)

# Perform object detection
results = model.predict(frame)
a = results[0].boxes.data
px = pd.DataFrame(a).astype("float")

for index, row in px.iterrows():
    x1 = int(row[0])
    y1 = int(row[1])
    x2 = int(row[2])
    y2 = int(row[3])

    d = int(row[5])
    c = class_list[d]
    cx = int(x1 + x2) // 2
    cy = int(y1 + y2) // 2
    result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
    if result >= 0:
        crop = frame[y1:y2, x1:x2]
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 10, 20, 20)

        text = pytesseract.image_to_string(gray).strip()
        text = text.replace('(', '').replace(')', '').replace(',', '').replace(']', '')
        print(text)
        if text not in processed_numbers:
            processed_numbers.add(text)
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("../data/car_plate_data.txt", "a") as file:
                file.write(f"{text}\t{current_datetime}\n")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

# Draw the area of interest
cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 0), 2)

# Display the image
while True:
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()