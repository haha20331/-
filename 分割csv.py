

import pandas as pd
import glob
import cv2
import os
path="./Train_Dev/train_labels/"
path_img="./Train_Dev/training/"
os.makedirs(path+'new_csv', exist_ok=True)
for x in glob.glob(path+'*.csv'):
    
    
    data=pd.read_csv(x)
    print(os.path.splitext(os.path.basename(x))[0])
    img = cv2.imread(path_img+os.path.splitext(os.path.basename(x))[0]+'.jpg')
    p_x=img.shape[1]
    p_y=img.shape[0]
    a=float(data.columns[0])
    
    b=float(data.columns[1])
    data.columns = ['x','y']
    data.loc[len(data.index)+1]=(a,b)
    

    o_x=int(p_x/224)
    o_y=int(p_y/224)
    
    for name in range(o_x*o_y):

        mask=(data["x"]>=224*(name%o_x)) & (data["x"]<224*(1+name%o_x)) & (data["y"]>=224*(name/o_x))&(data["y"]<224*(1+name/o_x))
    
        ans = pd.DataFrame()
    
        ans=ans.append(data[mask],ignore_index=True)
    
        ans["x"]=ans["x"]%224
    
        ans["y"]=ans["y"]%224
    
        ans.to_csv(path+'new_csv/' + os.path.splitext(os.path.basename(x))[0]+'_'+ str(name)+'.csv')
        
    
    