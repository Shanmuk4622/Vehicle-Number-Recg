import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
import pytesseract
from datetime import datetime
from config.settings import MODEL_PATH, CLASS_LIST

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

model = YOLO(MODEL_PATH)

def process_video(video_path, area, processed_numbers, output_file):
    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        ret, frame = cap.read()
        count += 1
        if count % 3 != 0:
            continue
        if not ret:
            break

        frame = cv2.resize(frame, (1020, 500))
        results = model.predict(frame)
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")

        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])

            d = int(row[5])
            cx = int(x1 + x2) // 2
            cy = int(y1 + y2) // 2
            result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
            if result >= 0:
                crop = frame[y1:y2, x1:x2]
                gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
                gray = cv2.bilateralFilter(gray, 10, 20, 20)

                text = pytesseract.image_to_string(gray).strip()
                text = text.replace('(', '').replace(')', '').replace(',', '').replace(']', '')
                if text not in processed_numbers:
                    processed_numbers.add(text)
                    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(output_file, "a") as file:
                        file.write(f"{text}\t{current_datetime}\n")
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                    cv2.imshow('crop', crop)

        cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 0), 2)
        cv2.imshow("RGB", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()