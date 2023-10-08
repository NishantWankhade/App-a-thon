import cv2
import pose_model_class

def scaleImg(img, pose):
    shoulder = pose.shoulder
    waist = pose.waist

    
