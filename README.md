# Melanoma_Detection
This project aims at classifying Skin Lesions based on different classes. The dataset used for training the models are:
- ISIC 2018
- ISIC 2019

The repo follows the following structure:

- Documentation: Contains various project related documents with detailled explanation of processes performed.
    - PreProcessing_201X: Contains detailed explanation of step-wise approach taken to process images from all the different classes for ISIC 2018 & ISIC 2019 dataset. 
    -  ISIC_201X_augmenations_summary: The excel files corresponding to each dataset consists a summarised description of augmentations performed on each class with information on number of images augmented, parameters of techniques used and final count of images of each class.
    - CNN_Model_Development.docx -  Report presented on 12th March describing different models.

- ISIC2018: Consists of following files that contains code for performing different kinds of Tasks:
    - ISIC2018_Preprocessing_Augmentation.ipynb : Consists compiled code for all data preprocessing, augmentation and train-test splitting for xreation of final data for modelling
    - labels: Consists of mappings of manually selected images for cropping, hair removal as well as training and test data ground truths from ISIC archive.
    - Model1_2_3_4.ipynb : Contains the first four models as described in the document.
        - Model 1 : Proposed model from Research paper
        - Model 2- Modified version of Model 1.
        - Model 3 – ResNet50
        - Model 4 – InceptionV3 
    - Ensemble 1.ipynb – Contains the Ensemble of 10 Base Models (Model1) trained on randomly shuffled different sets of test train validation splits.
    - Ensemble 2.ipynb – Contains the Ensemble of 10 modified Base Models with 1 extra CNN layer, 25% dropout, trained on randomly shuffled different sets of test train validation splits.
    - Ensemble 3.ipynb – Contains the Ensemble of 10 modified Models (Model1) with 1 extra CNN layer, 40% dropout, trained on randomly shuffled different sets of test train validation splits.

## Usage

1. Download ISIC 2018 from here https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Training_Input.zip or from one drive folder shared.

2. Place the images in 'Melanoma_Detection/ISIC2018/orig'

3. Run 'Melanoma_Detection/ISIC2018_Preprocessing_Augmentation.ipynb' to perform preprocessing. All the directories get created internally in code.

4. Run Model1_2_3_4.ipynb file to create the first four models and their corresponding results. Note that the models ceated here are not getting saved since the results are not prominent.

5. Run Ensemble1.ipynb, Ensemble2.ipynb or Ensemble3.ipynb to develop ensembles fo model. Make sure to follow instructions given in the notebook. Also, these models are saved and can be loaded without explicitly training them. All the notebooks contain code to load these models at the end. 

Make sure to change path seperator if running on Windows system.