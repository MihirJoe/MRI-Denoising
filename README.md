# BME5710-Final-Project

Using GANs for denoising images:
https://openaccess.thecvf.com/content/ACCV2020/papers/Tran_GAN-based_Noise_Model_for_Denoising_Real_Images_ACCV_2020_paper.pdf

- Add varying types of noise after each epoch
- Show training and validation loss over epochs
- Get close to -20db
    - Above 19.2
- K-fold cross validation
- Bioimaging techniques (Homework 5)

Denoising architecture:
https://arxiv.org/pdf/2208.14337.pdf


https://optuna.org

Pytorch:

- For training set you should shuffle, not for validation set
- One loader for each dataset
- Does the backpropogation internally 
- self.conv2D = nn.Conv2D() # double check syntax