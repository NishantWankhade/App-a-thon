import cv2
import numpy as np
import pose_detection
import augment_shirt
import pose_model_class


global pose 

# Create a VideoCapture object to access the default camera (usually camera index 0)
cap = cv2.VideoCapture(0)

cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Process for pose detection on each frame returns image and keypoints after pose detection
    li = pose_detection.process(frame)
    frame = li[0]
    keypoints = np.array(li[1])

    if(keypoints.size != 0):
        pose = pose_model_class.Pose(keypoints)

        # cv2.IMREAD_UNCHANGED will be used to also take the alpha channel in the image
        t_shirt = cv2.imread("T-shirt.jpg",cv2.IMREAD_UNCHANGED)

        # Augment the Shirt by super imposing the images
        frame = augment_shirt.augment(frame, pose, t_shirt)
    

    # Display the captured frame
    cv2.imshow("Camera Feed", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
