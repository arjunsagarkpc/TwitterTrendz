##import pandas as pd
##
##def copy_csv(filename):
##    df = pd.read_csv('output_got.csv')
##    df.to_csv('HT1.csv')
##copy_csv('file.csv')


import pandas as pd

def copy_csv1():
    df = pd.read_csv('output_got.csv')
    return(df.to_csv('HT1.csv'))

def copy_csv2():
    df = pd.read_csv('output_got.csv')
    return(df.to_csv('HT2.csv'))

def copy_csv3():
    df = pd.read_csv('output_got.csv')
    return(df.to_csv('HT3.csv'))

def copy_csv4():
    df = pd.read_csv('output_got.csv')
    return(df.to_csv('HT4.csv'))

def copy_csv5():
    df = pd.read_csv('output_got.csv')
    return(df.to_csv('HT5.csv'))

if __name__ == "__main__":
    copy_csv1()
    copy_csv2()
    copy_csv3()
    copy_csv4()
    copy_csv5()       
                     
