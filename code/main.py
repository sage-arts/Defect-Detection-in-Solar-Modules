import numpy as np
import cv2
from load_dataset import load_dataset
from load_train_set import load_train_set
from morphology import morphology
from ica import *
# images is a 3d matrix consists of 2624 solar cell images (image[i]->ith image)
# probs is probability of defectiveness of the images (0.0 : Non-defective)
# types array tells image is mono crystalline or poly crystalline
images,probs,types=load_train_set()

good_mono=[] #3d matrix of Non-defective mono crystalline images 
good_poly=[] #3d matrix of Non-defective poly crystalline images

for i in range(images.shape[0]):
    if(probs[i]==0.0) and (types[i]=='mono'):
        good_mono.append(images[i])
    if(probs[i]==0.0) and (types[i]=='poly'):
        good_poly.append(images[i])
good_mono=np.array(good_mono)
good_poly=np.array(good_poly)


print(images.shape)
print(probs.shape)
print(types.shape)


morph=[] # morphologically transformed images
for i in range(50,80):
    temp=morphology(good_poly[i],16)
    morph.append(temp)
morph=np.array(morph)

print(morph.shape)
X=np.uint8(np.zeros([30,90000]))

for i in range(morph.shape[0]):
    for j in range(morph.shape[1]):
        for k in range(morph.shape[2]):
            X[i][j+k*300] = morph[i][j][k]


U=ica(X,iterations=100) 

print(U.shape)
U_inv=np.linalg.pinv(U)
X_inv=np.linalg.pinv(X)
print(U_inv.shape)

sample=load_dataset()
print(sample.shape)
morph=[]
for i in range(300,350):
    temp=morphology(sample[i],21)
    morph.append(temp)
morph=np.array(morph)

print(morph.shape)
data=np.uint8(np.zeros([50,90000]))

for i in range(morph.shape[0]):
    for j in range(morph.shape[1]):
        for k in range(morph.shape[2]):
            data[i][j+k*300] = morph[i][j][k]
print(data.shape)
result=[]   
result1=[]     
for z in range(50):
    y=data[z]
    b=y @ U_inv
    norm_b=np.linalg.norm(b)
    ans=1
    for i in range(X.shape[0]):
        
        b_i=X[i] @ U_inv
        norm_b_i=np.linalg.norm(b_i)
        
        product=norm_b * norm_b_i
        dot = np.dot(b,b_i)
        
        d_i = 1-(dot/product)
        
        ans=min(ans,d_i)

    ycap= (y @ X_inv) @ X
    norm_ycap=np.linalg.norm(ycap)      
    norm_y=np.linalg.norm(y)          
    c=norm_y/norm_ycap
    e=np.linalg.norm(y-c*ycap)

    result.append(ans)
    result1.append(e)

for i in range(len(result)):
    print("cell0 %d"%i,".png: %.2f"%result[i]," %.2f" %result1[i],end= " ")
    if result1[i]<=100.0 :
        print("Non-Defective")
    else :
        print("Defective")