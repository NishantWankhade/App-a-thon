import cv2
import pose_detection

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
    keypoints = li[1]
    
    # Display the captured frame
    cv2.imshow("Camera Feed", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
