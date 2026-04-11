## Assignemnt-01

**Question: Image Collection, Classification, and Feature Representation Analysis Using Pre-trained Deep Learning Models**

1. **Face Image Collection**
   Capture images of human faces using a mobile device. The dataset should include:

* Your own face, along with those of three male and three female participants.
* Images captured from five different angles for each individual (e.g., front, left profile, right profile, top, and slight tilt).
* Ensure that informed consent is obtained from all participants prior to data collection, adhering to ethical considerations.

2. **Flower Image Collection**
   Collect a dataset of flower images using a mobile phone:

* Select five distinct types of flowers.
* Capture five images for each type under varying conditions (e.g., lighting, background, orientation) to ensure diversity.

3. **Classification Using Pre-trained Models**
   Utilize ten pre-trained convolutional neural network models available in Keras (e.g., VGG, ResNet, Inception, MobileNet, etc.) to perform image classification on both datasets. For each image:

* Record the Top-1 predicted class label.
* Record the Top-5 predicted class labels along with their associated probabilities.
* Compare the classification outputs across different models.

4. **Feature Extraction and Visualization**
   Investigate the feature extraction capabilities of the selected pre-trained models:

* Extract high-dimensional feature vectors from one of the deeper layers of each model.
* Apply three dimensionality reduction techniques (such as Principal Component Analysis (PCA), t-Distributed Stochastic Neighbor Embedding (t-SNE), and Uniform Manifold Approximation and Projection (UMAP)) to project the features into a 2D space.
* Generate visualizations of the reduced feature representations and analyze clustering patterns.

5. **Discussion**
   Provide a detailed analysis addressing the following:

* Evaluate how effectively different models separate distinct classes in the 2D feature space.
* Identify which model demonstrates superior feature representation.
* Justify the observations based on architectural differences, depth, and learned feature hierarchies of the models.


### Google colab link:

[**Open in Google Colab**](https://colab.research.google.com/drive/1tZ1HjY9KtrK6Lq8WSHxKjsE4YkEFbqRd?usp=sharing)