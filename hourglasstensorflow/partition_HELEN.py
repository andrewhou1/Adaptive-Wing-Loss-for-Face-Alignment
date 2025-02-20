import numpy as np
import scipy.io
import os
import sys
import cv2

all_imgs = sorted(os.listdir('/scratch1/tranluan/data/300W_LP_crop/image/HELEN/'))
test_imgs = all_imgs[32324:]
train_imgs = all_imgs[:32324]
landmark_file = scipy.io.loadmat('../../Landmarks_by_dataset/HELEN_landmarks.mat')['landmarks']
training_landmarks = landmark_file[:32324, :, :]
testing_landmarks = landmark_file[32324:, :, :]
not_LP_test_imgs = [i for i in range(len(testing_landmarks)) if '_0.png' in test_imgs[i]]
testing_landmarks = testing_landmarks[not_LP_test_imgs, :, :]

for i in range(len(train_imgs)):
    img = cv2.imread('/scratch1/tranluan/data/300W_LP_crop/image/HELEN/'+train_imgs[i])
    cv2.imwrite('../training_data/HELEN/'+train_imgs[i], img)

for i in range(len(not_LP_test_imgs)):
    img = cv2.imread('/scratch1/tranluan/data/300W_LP_crop/image/HELEN/'+test_imgs[not_LP_test_imgs[i]])
    cv2.imwrite('../testing_data/HELEN/'+test_imgs[not_LP_test_imgs[i]], img)
   
output_mat = {}
output_mat['landmarks'] = training_landmarks
scipy.io.savemat('../training_data/HELEN_training_landmarks.mat', output_mat)

output_mat = {}
output_mat['landmarks'] = testing_landmarks
scipy.io.savemat('../testing_data/HELEN_testing_landmarks.mat', output_mat)
