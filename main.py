import cv2
import numpy as np
import copy
import datetime

from close_n import best_match

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('./haarcascade_profileface.xml')

cap = cv2.VideoCapture(0)
n = 0
d = np.zeros((480, 640, 3), dtype='int')

n_frames = 0

while True:
    n_frames += 1
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if n_frames % 10 == 0:
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        print len(faces)
        for ix in xrange(len(faces)):
            (x, y, w, h) = faces[ix]
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = copy.deepcopy(frame[y:y + h, x:x + w])

            ij = cv2.resize(roi_color, (100, 100))
            res, qal = best_match(ij)
            if 'img' in res:
                v = 'manoj'
            else:
                v = 'laksh'

            # print v, datetime.datetime.now()

            d[y:y + h, x:x + w] += frame[y:y + h, x:x + w]
            if n >= 5:
                pass
                # line 43
                cv2.imwrite(
                    'data/image' + str(n) + '.jpg',
                    frame[y - 10:y + h + 10, x - 10:x + w + 10])
            n += 1
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # 47-49

            # if i >= 100:
                # i = 0
            cv2.imshow('face_crop', roi_color)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print d.shape

cv2.imwrite('face.jpg', d)
# print np.max(d), np.max(frame)

cap.release()
cv2.destroyAllWindows()
