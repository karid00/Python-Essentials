import pandas as pd
import matplotlib.pyplot as plt

def ejercicio2_1():
    Datos_2021 = (1, 2, 3, 4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302)
    
    df = pd.DataFrame(Datos_2021)
    
    df.head()
    
    df.describe()
    
    Q1 = float(df.quantile(0.25))
    Q2 = float(df.quantile())
    Q3 = float(df.quantile(0.75))
    RIC = Q3-Q1
    
    
    atpMax = Q3+RIC*1.5
    atpMax
    
    plt.boxplot(df, vert=False)
    
    
    atipicos = []
    pares = []
    impares = []
    
    for i in Datos_2021:
        if i > atpMax:
            atipicos.append(i)
    
    
        if i%2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    print(f"Los valores atípicos de acuerdo a la formula [ Atípicos > Q3+1.5xRIC ] son: {atipicos}")
    print(f"Los valores pares son: {pares}")
    print(f"Los valores impares son: {impares}")