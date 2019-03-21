from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import argparse
import facenet
import detect_face
import subprocess
import os
import sys
import math
import pickle
from sklearn.svm import SVC

# Ensure that pwd is where this file lives
RD = os.path.dirname(os.path.realpath(__file__))
os.chdir(RD)

# Get the IP of edge device
p = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE)
IPaddr = p.communicate()[0].strip()

with tf.Graph().as_default():
    with tf.Session() as sess:
        nodedir = '../classifiers/node_' + IPaddr 
        # Make nodedir if does not exist
        subprocess.call("if [ -z $(ls ../classifiers | grep "+IPaddr+") ] ; then mkdir "+nodedir+" ; fi", shell=True)

        dataNamesDir = '../datasets/data'
        datadir = './output_dir'
        dataset = facenet.get_dataset(datadir)
        paths, labels = facenet.get_image_paths_and_labels(dataset)
        print('Number of classes: %d' % len(dataset))
        print('Number of images: %d' % len(paths))

        print('Loading feature extraction model')
        
        modeldir = '../models/20170511-185253/20170511-185253.pb'
        facenet.load_model(modeldir)

        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
        embedding_size = embeddings.get_shape()[1]

        # Run forward pass to calculate embeddings
        print('Calculating features for images')
        batch_size = 1000
        image_size = 160 
        nrof_images = len(paths)
        nrof_batches_per_epoch = int(math.ceil(1.0 * nrof_images / batch_size))
        emb_array = np.zeros((nrof_images, embedding_size))
        for i in range(nrof_batches_per_epoch):
            start_index = i * batch_size
            end_index = min((i + 1) * batch_size, nrof_images)
            paths_batch = paths[start_index:end_index]
            images = facenet.load_data(paths_batch, False, False, image_size)
            feed_dict = {images_placeholder: images, phase_train_placeholder: False}
            emb_array[start_index:end_index, :] = sess.run(embeddings, feed_dict=feed_dict)


        classifier_filename = nodedir+"/classifier.pkl"
        classifier_filename_exp = os.path.expanduser(classifier_filename)


        mynames = open(nodedir+'/names.txt','w')
        for idx, mydir in enumerate(os.listdir(dataNamesDir)):
            mynames.write(mydir + '\n')
        mynames.seek(mynames.tell() - 1, os.SEEK_SET)
        mynames.close()
        

        # Train classifier
        print('Training classifier')
        model = SVC(kernel='linear', probability=True)
        model.fit(emb_array, labels)

        # Create a list of class names
        class_names = [cls.name.replace('_', ' ') for cls in dataset]
        # Saving classifier model
        with open(classifier_filename_exp, 'wb') as outfile:
            pickle.dump((model, class_names), outfile)
        print('Saved classifier model to file "%s"' % classifier_filename_exp)
        print('Goodluck')