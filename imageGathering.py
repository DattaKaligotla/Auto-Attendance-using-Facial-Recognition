import  cv2
import numpy as np
import time
import sys
import facenet
import tensorflow as tf
from align import detect_face
import sys
sess = tf.Session()
threshold = [0.6, 0.7, 0.7]
factor = 0.709
margin = 44
input_image_size = 160
cap = cv2.VideoCapture(0)
input_image_size = 160
minsize = 20
pnet, rnet, onet = detect_face.create_mtcnn(sess, 'align')

def getFace(img):
    faces = []
    img_size = np.asarray(img.shape)[0:2]
    n = 0;
    bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    if not len(bounding_boxes) == 0:
        for face in bounding_boxes:
            n = n+1
    return n
while(True):
    ret, frame = cap.read()

    faces = getFace(frame)
    
    if faces >= 1:
        link = 'C:/Users/N/sreek/Desktop/Test_gray'+str(time.time)+'.jpg'
        
        cv2.imwrite(link, frame)


    cv2.imshow("input",frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
