import pandas as pd 
import numpy as np
import glob
def run():
    try:
        for x in glob.glob('./*.csv'):
            df=pd.read_csv(x)
            for i in df.columns:
                for j in df[i]:
                    t=eval(j)
                    for c in t:
                        if len(c)!=5:
                            print(x,c,'not correct')
                            return None
        print("!!!!!!!!!!!!!!!! all good !!!!!!!!!!!!!!!!!!!")
    except Exception as ex:
        

        print('error occured',x,i)
        try:
            print("#####",t,"########")
        print(ex) 
run()





