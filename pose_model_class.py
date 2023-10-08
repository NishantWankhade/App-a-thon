
class Pose:
    def __init__(self, kp):
        self.shoulder = [kp[1],kp[0]]
        self.elbow = [kp[3],kp[2]]
        self.wrist = [kp[5],kp[4]]
        self.waist = [kp[7],kp[6]]
    

    def show_points(self):
        print("shoulders :- " + str(self.shoulder))
        print("waist :- " + str(self.waist))