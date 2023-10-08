from ultralytics import YOLO
import cv2
import numpy as np

def process(img):
    # Load a model
    model = YOLO('Model\yolov8n-pose.pt')  # load an official model
    # model = YOLO('path/to/best.pt')  # load a custom model

    # Predict with the model
    results = model(img)  # predict on an image

    # img = results[0].plot(kpt_line = False)
    
    top = []
    for r in results:
            #Only keypoints of the fore arms and waist are sent
            top = np.array(r.keypoints.xy[0][5:13].cpu().numpy())
            break
    
    arr = []
    for i in top:
        arr.append([int(i[0]), int(i[1])])
        if(i[0] != 0 and i[1] != 0) :
            cv2.circle(img, (int(i[0]), int(i[1])), radius=5, color=(0, 255, 0), thickness=-1)

    return [img , arr]
