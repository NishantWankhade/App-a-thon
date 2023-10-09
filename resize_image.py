import cv2

def scaleImg(img, pose):
    shoulder = pose.shoulder
    waist = pose.waist
    
    width = abs(shoulder[1][0] - shoulder[0][0])
    height = abs(shoulder[1][1] - waist[1][1])
    
    print(height)
    print(width)

    if(height >= width) :
        img = cv2.resize(img, (width,height))

    return img

    
