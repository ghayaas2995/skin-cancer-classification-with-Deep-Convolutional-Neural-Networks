import shutil
from glob import glob
from sklearn.utils import shuffle
import os
import pandas as pd

def shuffling_tt(X):
    X= shuffle(X)
    return X

for clas in ['mel', 'nv', 'bcc', 'ak', 'bkl', 'df', 'vasc']:
    os.makedirs(f'test/{clas}')

meta = pd.read_csv('ISIC_2019_Training_GroundTruth.csv')
meta_shuffled = shuffling_tt(meta)

c1,c2,c3,c4,c5,c6,c7 = 0,0,0,0,0,0,0

for row in meta.values:
    if row[1] == 1 and c1 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/mel/{row[0]}.jpg")
        c1+=1
    elif row[2] == 1 and c2 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/nv/{row[0]}.jpg")
        c2+=1
    elif row[3] == 1 and c3 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/bcc/{row[0]}.jpg")
        c3+=1
    elif row[4] == 1 and c4 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/ak/{row[0]}.jpg")
        c4+=1
    elif row[5] == 1 and c5 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/bkl/{row[0]}.jpg")
        c5+=1
    elif row[6] == 1 and c6 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/df/{row[0]}.jpg")
        c6+=1
    elif row[7] == 1 and c7 < 100:
        shutil.copyfile(f"ISIC_2019_Training_Input/{row[0]}.jpg", f"test/vasc/{row[0]}.jpg")
        c7+=1
    else:
        pass