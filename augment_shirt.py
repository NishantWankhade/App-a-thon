import cv2

def augment(person_image , keypoints):
    t_shirt = cv2.imread("T-shirt.jpg", cv2.IMREAD_UNCHANGED)
    
    result_image = person_image.copy()
    alpha_mask = t_shirt[:, :, 3] / 255.0  # Extract the alpha channel
    
    for c in range(0, 3):  # Apply blending for RGB channels
        result_image[:, :, c] = (1.0 - alpha_mask) * result_image[:, :, c] + alpha_mask * t_shirt[:, :, c]

    # Display or save the augmented image
    return result_image

    
