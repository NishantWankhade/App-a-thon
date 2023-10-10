import cv2
import pose_model_class
import resize_image

def augment(person_image , pose , t_shirt):

    # Scale image according to pose
    t_shirt = resize_image.scaleImg(t_shirt, pose)
    # print(t_shirt.shape)

    start_y = pose.shoulder[1][1]
    start_x = pose.shoulder[1][0]

    # result_image = person_image.copy()
    shape = t_shirt.shape
    # print(shape)
    # return person_image

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
                    x = (i + start_y)
                    y = (j + start_x)
                    if (x >= input_height):
                        x = input_height - 1
                    
                    if(y > input_width):
                        y = input_width - 1

                    person_image[x][y][0] = r
                    person_image[x][y][1] = g
                    person_image[x][y][2] = b
            
        return person_image
    else :
        return person_image


    
