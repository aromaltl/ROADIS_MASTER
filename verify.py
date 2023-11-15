import pandas as pd 
import numpy as np
import glob
def run():
    try:
        for x in glob.glob('./*.csv'):
            df=pd.read_csv(x)
            for i in filter(lambda ff:True if 'RIGH' in ff or 'LEFT' in ff else False,df.columns):
                
                for j in df[i]:
                    t=eval(j)
                    for c in t:
                        if len(c)!=6:
                            print(x,c,'not correct')
                            return None
                        if len(c[1])<3:
                            print(x,c,'position invalid')
        print("!!!!!!!!!!!!!!!! all good !!!!!!!!!!!!!!!!!!!")
    except Exception as ex:
        
        try:
            print('error occured',x,i)
            print("########",t,"########")
        except:
            pass
        print(ex) 
run()
#!!!!!!!!!!!!!!!! all good !!!!!!!!!!!!!!!!!!!





