import cv2

path_to_image = input("Give Absolute path to the image to annotate :- ")

img = cv2.imread(path_to_image)
window_name = "Annotate Image"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name, img)

total_point = 0

#Define the events for the 
# mouse_click. 
def mouse_click(event, x, y,  
                flags, total_point): 
       
    if event == cv2.EVENT_LBUTTONDBLCLK and total_point <= 4:
        cv2.circle(img,(x,y),radius=5, color=(0, 255, 0), thickness=-1) 
        total_point += 1
        cv2.imshow(window_name, img) 
   
  
cv2.setMouseCallback(window_name, mouse_click, total_point) 

while True:
    cv2.imshow(window_name, img)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite(path_to_image, img)
        break


cv2.destroyAllWindows()


