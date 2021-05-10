import pandas as pd
import glob
import cv2
import os
path="./test_public/" #改成你存結果(包含圖片和csv)的資料夾路徑
path_img="./training/"#這個沒用到
def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
           if old_str in line:
                line = line.replace(old_str,new_str)
           file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write("0,x,y,w,h\n")
        f.write(file_data)




for x in glob.glob(path+'*.txt'):
    alter(x,' ',',')
    
    data = pd.read_csv(x)
    print(os.path.splitext(os.path.basename(x))[0])
    img = cv2.imread(path+os.path.splitext(os.path.basename(x))[0]+".JPG")
    p_x=img.shape[1]
    p_y=img.shape[0]
    
    data.info()
    print(data) 
    
    
    data.drop(['0','w','h'],axis=1)
    ans = pd.DataFrame()
    ans=ans.append(data,ignore_index=True)
    ans.drop(['0','w','h'],axis=1,inplace=True)
    ans['x']=ans['x']*p_x
    ans['y']=ans['y']*p_y
     
    ans.to_csv ("./ans/"+os.path.splitext(os.path.basename(x))[0]+".csv",index=False,header=False)

    
