import cv2
import pose_model_class
import resize_image

def augment(person_image , pose):
    t_shirt = cv2.imread("T-shirt.jpg", cv2.IMREAD_UNCHANGED)

    # Scale image according to pose
    person_image = resize_image.scaleImg(person_image, pose)

    pose.show_points()
    # result_image = person_image.copy()
    # alpha_mask = t_shirt[:, :, 3] / 255.0  # Extract the alpha channel
    
    # for c in range(0, 3):  # Apply blending for RGB channels
    #     result_image[:, :, c] = (1.0 - alpha_mask) * result_image[:, :, c] + alpha_mask * t_shirt[:, :, c]

    # # Display or save the augmented image
    # return result_image

    
