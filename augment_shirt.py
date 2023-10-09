import cv2
import pose_model_class
import resize_image

def augment(person_image , pose , t_shirt):

    # Scale image according to pose
    t_shirt = resize_image.scaleImg(t_shirt, pose)
    print(t_shirt.shape)

    # result_image = person_image.copy()
    shape = t_shirt.shape

    h = shape[0]
    w = shape[1]
    input_shape = person_image.shape
    input_height = input_shape[0]
    input_width = input_shape[1]

    if(h <= input_height and w <= input_width):
        for i in range(0, h):
            for j in range(0, w):
                r,g,b,a = t_shirt[i][j]
                if(a != 0):
                    person_image[i][j][0] = r
                    person_image[i][j][1] = g
                    person_image[i][j][2] = b
            
        return person_image
    else :
        return person_image


    
