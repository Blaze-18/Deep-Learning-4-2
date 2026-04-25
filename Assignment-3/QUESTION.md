## Question

1. **Visualization and Analysis of Feature Maps**  
a. Select a pretrained convolutional neural network (CNN) and process an input image of your own face through the network.  
b. Extract feature maps from at least three layers (early, middle, deep).  
c. Visualize the selected feature maps and provide a concise analysis describing what each layer’s feature maps reveal about learned representations.  
d. Explain how the feature maps relate to edge, texture, and semantic information across layers.

2. **Design and Architectural Justification of a Custom CNN**
a. Propose a custom CNN architecture for image classification; include a diagram or layer-by-layer specification (layer type, kernel size, stride, padding, number of filters, activation, pooling, normalization, and parameter count).  
b. Justify each architectural choice with respect to computational cost, receptive field, depth, capacity to generalize, and suitability for small-to-medium image datasets.  
c. Describe any regularization and optimization strategies used (dropout, batch norm, weight decay, learning rate schedule, etc.) and justify their inclusion.

3. **Implementation and Training on CIFAR-10**
a. Implement the proposed CNN in a deep learning framework of your choice (specify framework and versions).  
b. Train the model on the CIFAR-10 dataset and report: training/validation accuracy and loss curves, final test accuracy, training hyperparameters (batch size, epochs, optimizer, initial learning rate), and total training time.  
c. Include code snippets or references to scripts used for data loading, augmentation, training loop, and evaluation.

4. **Comparative Analysis of Activation Functions**
a. Train and evaluate the same CNN architecture using three different activation functions (choose from ReLU, Leaky ReLU, ELU, SELU, GELU, or others—specify which three you used).  
b. For each activation, report convergence behavior, training stability, final test accuracy, and any observed differences in loss/accuracy curves.  
c. Analyze and discuss how each activation affected gradient flow, sparsity of activations, learning speed, and generalization.

5. **Critical Discussion on Convolution Kernel Types**
a. Explain the principles, advantages, and limitations of the following convolution kernel types: regular kernels, deformable kernels, dilated (atrous) kernels, depthwise separable kernels, modified depthwise-separable kernels, and pointwise kernels.  
b. For each kernel type, discuss expected effects on receptive field, parameter efficiency, computational cost, ability to model geometric transformations, and suitability for different tasks (e.g., classification, detection, segmentation).  
c. Provide concise recommendations on when to prefer each kernel type in practical CNN design, supported by theoretical reasoning or literature references where appropriate.

***Deliverables***:  
- Well-commented code or notebooks implementing the experiments.  
- Visualizations (feature maps and training curves).  
- A concise report containing architecture specification, training details, comparative results, and the critical discussion.
