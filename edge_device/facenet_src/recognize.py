from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from scipy import misc
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
import facenet
import detect_face
import os
from os.path import join as pjoin
import sys
import time
import copy
import math
import pickle
import subprocess
from sklearn.svm import SVC
from sklearn.externals import joblib

# Function: MatchName()  
# input:    
#           model       - the trained inference engine 
#           HumanNames  - Array of names trained on model
#           face        - Image of person to recognize 
# output:     
#           two-element-array - the name and fitness level of the recognized face. 
def matchName(model,HumanNames,face):
    predictions = model[0].predict_proba(face)
    best_class_indices = np.argmax(predictions, axis=1)
    best_class_probabilities = predictions[np.arange(len(best_class_indices)), best_class_indices]
    result_names =''
    for H_i in HumanNames:
        if HumanNames[best_class_indices[0]] == H_i:
            result_names = HumanNames[best_class_indices[0]]
    #print(result_names,best_class_probabilities)
    return [result_names,best_class_probabilities]


#print('Creating networks and loading parameters')
with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.6)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():

        pnet, rnet, onet = detect_face.create_mtcnn(sess, './align')

        name = 0
        fitness_level = 1
        minsize = 20  # minimum size of face
        threshold = [0.6, 0.7, 0.7]  # three steps's threshold
        factor = 0.709  # scale factor
        margin = 44
        frame_interval = 3
        batch_size = 1000
        image_size = 182
        input_image_size = 160

        #print('Loading feature extraction model')
        model_dir = 'models/20170511-185253/20170511-185253.pb'
        facenet.load_model(model_dir)
        
        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
        embedding_size = embeddings.get_shape()[1]

        video_capture = cv2.VideoCapture(0)
        c = 0

        models = []
        names = []

        # Load Classifier and names from node directory.
        p = subprocess.Popen("ls ../classifiers", shell=True, stdout=subprocess.PIPE)
        node_dir_names_raw = p.communicate()[0]
        node_dir_names = [f for f in node_dir_names_raw.split('\n') if len(f) > 0]  
        for node in node_dir_names: 
            classifier_filename = '../classifiers/' + node + '/classifier.pkl'
            classifier_filename_exp = os.path.expanduser(classifier_filename)
            names_filename = '../classifiers/' + node + '/names.txt'
            names_filename_exp = os.path.expanduser(names_filename)

            with open(classifier_filename_exp, 'rb') as classifier_file:
                models.append(pickle.load(classifier_file))
                #print('load classifier file-> %s' % classifier_filename_exp)
            with open(names_filename_exp, 'rb') as names_file:
                names.append([name for name in names_file.read().split('\n') if len(name) > 0])
                #print('load classifier file-> %s' % classifier_filename_exp)
            classifier_file.close()
            names_file.close()
        
        #
        # TODO: Do this check BEFORE the code above by checking the classifiers/ folder.
        # Verify that there is at least one classifier
        if len(models) == 0 :
            sys.exit(" Error: no custom models/Classifiers loaded. Have you run classify.py?")

        #print('Start Recognition!')
        prevTime = 0
        while True:
            ret, frame = video_capture.read()

            frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)    #resize frame (optional)

            curTime = time.time()    # calc fps
            timeF = frame_interval
            
            if frame.ndim == 2:
                frame = facenet.to_rgb(frame)
            frame = frame[:, :, 0:3]
            bounding_boxes, _ = detect_face.detect_face(frame, minsize, pnet, rnet, onet, threshold, factor)
            nrof_faces = bounding_boxes.shape[0]
            #print('Detected_FaceNum: %d' % nrof_faces)

            if nrof_faces > 0:
                det = bounding_boxes[:, 0:4]
                img_size = np.asarray(frame.shape)[0:2]

                #cropped = []
                #scaled = []
                #scaled_reshape = []
                bb = np.zeros((nrof_faces,4), dtype=np.int32)

                for i in range(nrof_faces):
                    emb_array = np.zeros((1, embedding_size))

                    bb[i][0] = det[i][0]
                    bb[i][1] = det[i][1]
                    bb[i][2] = det[i][2]
                    bb[i][3] = det[i][3]

                    #inner exception
                    if bb[i][0] <= 0 or bb[i][1] <= 0 or bb[i][2] >= len(frame[0]) or bb[i][3] >= len(frame):
                        print(' Face is out of range to be recognized. ')
                        continue
                    
                    cropped=[]
                    scaled=[]
                    scaled_reshape=[]
                    cropped.append(frame[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :])
                    cropped[0] = facenet.flip(cropped[0], False)
                    scaled.append(misc.imresize(cropped[0], (image_size, image_size), interp='bilinear'))
                    scaled[0] = cv2.resize(scaled[0], (input_image_size,input_image_size),
                                            interpolation=cv2.INTER_CUBIC)
                    scaled[0] = facenet.prewhiten(scaled[0])
                    scaled_reshape.append(scaled[0].reshape(-1,input_image_size,input_image_size,3))
                    feed_dict = {images_placeholder: scaled_reshape[0], phase_train_placeholder: False}
                    emb_array[0, :] = sess.run(embeddings, feed_dict=feed_dict)
                    
                    name_results= []
                    for model_num in range(len(models)): 
                        name_results.append(matchName(models[model_num],names[model_num],emb_array))
                    
                    #find the one with highest fitness level
                    max_name_result = max(name_results,key= lambda m : m[1])
                    
                    #convert to percentage
                    max_name_result[fitness_level]*=100
                    
                    # Plot result idx under box
                    print("face "+ str(i) +" identified. it's " + str(max_name_result[0]))
                    text_x = bb[i][0]
                    text_y = bb[i][3] + 20
                    texttoOutput = max_name_result[0] + np.array2string(max_name_result[1],3)
                    cv2.putText(frame, texttoOutput, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1, (0, 0, 255), thickness=1, lineType=2)
                    #cv2.imshow('Video', frame)
            else:
                print('Unable to align')
            sec = curTime - prevTime
            prevTime = curTime
            fps = 1 / (sec)
            fps_str = 'FPS: %2.3f' % fps
            text_fps_x = len(frame[0]) - 150
            text_fps_y = 20
            cv2.putText(frame, fps_str, (text_fps_x, text_fps_y),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), thickness=1, lineType=2)
            # c+=1
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
