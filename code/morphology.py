import numpy as np
def morphology(img,L):
    n,m = img.shape
    morph_img=[[0 for i in range(m)]for j in range(n)]
    for x in range(n):
        for y in range(m):
            S_90,f_90 = 0,-1
            S_135,f_135 = 0,-1
            S_45,f_45 = 0,-1
            for i in range(-(L//2),(L//2)+1):
                if (x+i>=0) and (x+i<n):
                    S_90=S_90+img[x+i][y]
                    f_90=max(f_90,img[x+i][y])
                if (x+i>=0) and (x+i<n) and (y+i>=0) and (y+i<m):
                    S_135=S_135+img[x+i][y+i]
                    f_135=max(f_135,img[x+i][y+i])
                if (x+i>=0) and (x+i<n) and (y-i>=0) and (y-i<m):
                    S_45=S_45+img[x+i][y-i]
                    f_45=max(f_45,img[x+i][y-i])
            
            if (S_90<=S_135) and (S_90<=S_45):
                morph_img[x][y]=f_90
            if (S_135<=S_90) and (S_135<=S_45):
                morph_img[x][y]=f_135
            if (S_45<=S_135) and (S_45<=S_90):
                morph_img[x][y]=f_45
    
    return morph_img
                
    