import numpy as np
import scipy.io
import os
import sys
import cv2

all_imgs = sorted(os.listdir('/scratch1/tranluan/data/300W_LP_crop/image/IBUG/'))
landmark_file = scipy.io.loadmat('../../Landmarks_by_dataset/IBUG_landmarks.mat')['landmarks']
testing_landmarks = landmark_file
test_imgs = all_imgs
not_LP_test_imgs = [i for i in range(len(testing_landmarks)) if '_0.png' in test_imgs[i]]
testing_landmarks = testing_landmarks[not_LP_test_imgs, :, :]

for i in range(len(not_LP_test_imgs)):
    img = cv2.imread('/scratch1/tranluan/data/300W_LP_crop/image/IBUG/'+test_imgs[not_LP_test_imgs[i]])
    cv2.imwrite('../testing_data/IBUG/'+test_imgs[not_LP_test_imgs[i]], img)

output_mat = {}
output_mat['landmarks'] = testing_landmarks
scipy.io.savemat('../testing_data/IBUG_testing_landmarks.mat', output_mat)
