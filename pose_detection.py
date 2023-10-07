from ultralytics import YOLO

def process(img):
    # Load a model
    model = YOLO('yolov8n-pose.pt')  # load an official model
    # model = YOLO('path/to/best.pt')  # load a custom model

    # Predict with the model
    results = model(img)  # predict on an image

    annotated_frame = results[0].plot()
    
    for r in results:
        print(r.keypoints)

    return annotated_frame
