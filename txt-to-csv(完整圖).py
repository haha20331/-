import pandas as pd
import glob
import cv2
import os
path="./train_labels/"
path_img="./training/"
os.makedirs('./new_csv', exist_ok=True)
def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
           if old_str in line:
                line = line.replace(old_str,new_str)
           file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
for x in glob.glob(path+'*.csv'):
    
    
    data=pd.read_csv(x)
    print(os.path.splitext(os.path.basename(x))[0])
    img = cv2.imread(path_img+os.path.splitext(os.path.basename(x))[0]+".JPG")
    p_x=img.shape[1]
    p_y=img.shape[0]
    a=float(data.columns[0]) 
    b=float(data.columns[1])

    data.columns = ['x','y']
    data.loc[len(data.index)+1]=(a,b)
    data.info()

    o_x=int(p_x/224)
    o_y=int(p_y/224)
    
    
    ans = pd.DataFrame()
    ans["class"]=0
    ans=ans.append(data,ignore_index=True)
        
    ans["x"]=(ans["x"])/p_x
    
    ans["y"]=(ans["y"])/p_y
          
        
    ans["w"]=28/p_x
        
    ans["h"]=28/p_y
        
    #ans.loc[ans.x < 0,"x"] = 0
    #ans.loc[ans.y < 0,"y"] = 0
    #ans.loc[ans.x+ans.w > 223/224,"w"] = 223/224-ans["x"]
    #ans.loc[ans.y+ans.h > 223/224,"h"] = 223/224-ans["y"]
    ans["class"]=0
 
    ans.to_csv('./new_csv/' + os.path.splitext(os.path.basename(x))[0]+'.txt',index=False,header=False)
    alter('./new_csv/' + os.path.splitext(os.path.basename(x))[0]+'.txt',',',' ')

    
    
    