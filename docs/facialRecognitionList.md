# List of facial recognition software: 
## OpenFace 
	URL: https://cmusatyalab.github.io/openface/
	Descritption: The following overview shows the workflow for a single input image of Sylvestor Stallone from the publicly available LFW dataset.

	* Detect faces with a pre-trained models from dlib or OpenCV.
	* Transform the face for the neural network. This repository uses dlib's real-time pose estimation with OpenCV's affine transformation to try to make the eyes and bottom lip appear in the same location on each image.
	* Use a deep neural network to represent (or embed) the face on a 128-dimensional unit hypersphere. The embedding is a generic representation for anybody's face. Unlike other face representations, this embedding has the nice property that a larger distance between two face embeddings means that the faces are likely not of the same person. This property makes clustering, similarity detection, and classification tasks easier than other face recognition techniques where the Euclidean distance between features is not meaningful.
	* Apply your favorite clustering or classification techniques to the features to complete your recognition task. See below for our examples for classification and similarity detection, including an online web demo.

## Amazon "Rekognition" API:

