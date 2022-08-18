# Skin cancer classification
This project aims at classifying Skin Lesions based on different classes. The dataset used for training the models are:
- ISIC 2018
- ISIC 2019

The objective of this project is to develop a deep learning model to classify DICOM images of skin cancer among eight different diagnostic categories: Melanoma, Melanocytic nevus, Basal cell carcinoma, Actinic keratosis, Benign keratosis, Dermatofibroma, Vascular lesion, and Squamous cell carcinoma. The proposed Deep Convolutional Neural Network model is carefully designed with several layers, and multiple filter sizes, and manipulated filters and layers to improve the efficacy and accuracy. Dermatoscopic images are acquired from the International Skin Imaging Collaboration databases (ISIC-18 and 19) for experiments.

We worked in a team of 3 over a period of 5 months for this Capstone project on ISIC 2018 and 2019 datasets. The 2018 dataset consisted of 10015 skin cancer images belonging to 7 categories of cancer. We applied image preprocessing like, mapping the images, augmentations, resizing, normalization, cropping and removal of hairs in images using dull razor algorithm in python. We referred to a base CNN model published by university of Telkom, Bangkok and created ensemble model of 10 of these base models and achieved 15% more classification accuracy on classification of skin cancer images to their respective category. We also performed a similar course of preprocessing with suitable variations on the ISIC 2019 dataset and used a transfer learning approach with Xception model to classify the 8 classes images in the ISIC 2019 dataset.

Overall, the ensemble model achieved a 96% validation accuracy in classification of 7 types of skin cancer respective to ISIC 2018 dataset and the Xception model respective to ISIC 2019 was able to detect the lethal skin cancer in patients with a recall of 49%
