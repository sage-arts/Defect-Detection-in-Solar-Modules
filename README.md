# Defect-Detection-in-Solar-Modules-Using-ICA-Basis-Images
The following repository is a defect detection prediction algorithm for electroluminescence (EL) images of solar cells using independent component analysis (ICA).  
Run main.py in [code]() to run the Machine Learning Model for classification of images.   

## Sample Images   
### &nbsp; &nbsp; &nbsp; Defect free Image   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Defective Image   
![alt defect_free](https://github.com/a0n0k0i0t/Defect-Detection-in-Solar-Modules-Using-ICA-Basis-Images/blob/main/images/cell0173.png?raw=true) &nbsp; &nbsp; &nbsp;
![alt defective](https://github.com/a0n0k0i0t/Defect-Detection-in-Solar-Modules-Using-ICA-Basis-Images/blob/main/images/cell0277.png?raw=true)

## Training the data:    
The ICA-based defect detection is highly dependent on defect free images."labels.csv" has well labelled images of solar cells with probability of defect(0.0-> defect-free, 1.0-> defective). We use 40 defect-free images randomly from the "images" set for a training set matrix `X`. Those 40 images are trained using ICA algorithm to get a matrix `U`. The separated components in `U`, called independent components (ICs), are required to be as mutually independent as possible.   
Also, one other method is used where we don't calculate `U` and test directly from `X` using given formula in the paper.   
`U` determines the defectiveness of a solar cell image. A test solar cell subimage is reconstructed as linear combination of the learned basis images. It is expected that a defect-free solar cell subimage can be well represented by the basis images and the reconstructed image of a defective solar cell subimage will be distinctly deviated from its original one.   
## Validation:   
Validation is done by the the matching the predicted labels value with labels in [labels.csv](https://github.com/a0n0k0i0t/Defect-Detection-in-Solar-Modules-Using-ICA-Basis-Images/blob/main/labels.csv) and checking percentage similarity.   
## Test data Prediction:   
Test data is feeded from [images](https://github.com/a0n0k0i0t/Defect-Detection-in-Solar-Modules-Using-ICA-Basis-Images/tree/main/images) file and morphology is performed same as train data. Then data is tested using two methods:
<ul>
  <li> Using ICA learned basis images matrix `U`:   
    In this method the ICA learned matrix `U` is used and to determine the presence or absence of defects in a sample cosine similarity is used.</li>
   <li> Using directly calculated matrix `U` from training sample `X`:   
     In this method the `U` matrix is not generated from training data instead test data is directly tested from `X` and reconstruction error is used to determine the presence or absence of defects.      
     Formula: <img src=https://github.com/a0n0k0i0t/Defect-Detection-in-Solar-Modules-Using-ICA-Basis-Images/blob/main/direct_formula.png?raw=true,alt='formula'></li>
</ul>
