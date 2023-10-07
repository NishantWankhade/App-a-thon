from ultralytics import YOLO
import cv2

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
            top.append(r.keypoints.xy[0][5:13].cpu().numpy())
    
    for j in top[0]:
        cv2.circle(img, (int(j[0]), int(j[1])), radius=5, color=(0, 255, 0), thickness=-1)

    return [img , top[0]]
