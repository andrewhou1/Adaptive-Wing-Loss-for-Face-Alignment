import numpy as np
import scipy.io
import os
import sys
import cv2

all_imgs = sorted(os.listdir('/scratch1/tranluan/data/300W_LP_crop/image/LFPW_Flip/'))
#test_imgs = all_imgs[:3666]
train_imgs = all_imgs[3666:]
landmark_file = scipy.io.loadmat('../../Landmarks_by_dataset/LFPW_Flip_landmarks.mat')['landmarks']
training_landmarks = landmark_file[3666:, :, :]
#testing_landmarks = landmark_file[:3666, :, :]
#not_LP_test_imgs = [i for i in range(len(testing_landmarks)) if '_0.png' in test_imgs[i]]
#testing_landmarks = testing_landmarks[not_LP_test_imgs, :, :]

for i in range(len(train_imgs)):
    img = cv2.imread('/scratch1/tranluan/data/300W_LP_crop/image/LFPW_Flip/'+train_imgs[i])
    cv2.imwrite('../training_data/LFPW_Flip/'+train_imgs[i], img)

#for i in range(len(not_LP_test_imgs)):
#    img = cv2.imread('/scratch1/tranluan/data/300W_LP_crop/image/LFPW/'+test_imgs[not_LP_test_imgs[i]])
#    cv2.imwrite('../testing_data/LFPW/'+test_imgs[not_LP_test_imgs[i]], img)
   
output_mat = {}
output_mat['landmarks'] = training_landmarks
scipy.io.savemat('../training_data/LFPW_Flip_training_landmarks.mat', output_mat)

#output_mat = {}
#output_mat['landmarks'] = testing_landmarks
#scipy.io.savemat('../testing_data/LFPW_testing_landmarks.mat', output_mat)
