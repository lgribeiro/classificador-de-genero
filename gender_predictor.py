from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from os import listdir, rename, makedirs, remove
from os.path import isfile, join, exists, isdir, abspath
import pandas as pd
import numpy as np
import pickle
import argparse
import sys
import os

def Preprocessing_data(df):
    col = df.columns
    if any("index" in s for s in col):
        # removendo a coluna index
        df = df.drop("index", axis=1)
        print("removeu coluna index")   

        
    # identificando valores NaN
    if (df.isnull().any().any()) :
        df = df.dropna()
        print("removeu linhas com valores ausentes")

    # removendo linhas duplicadas
    if(df.duplicated().any().any()):
        df = df.drop_duplicates()
        print("removeu linhas duplicadas")
        
    col = df.columns    
    if any("sex" in s for s in col):
        # removendo a coluna sex
        labels = df['sex'].str.upper()
        df = df.drop("sex", axis=1)
        print("removeu coluna sex")

    # usando propriedades do desvio padrao para encontrar e remover colunas com o mesmo valor
    df = df.drop(df.std()[(df.std() == 0)].index, axis=1)
    # decompondo variaveis categoricas 
    cat_df = pd.get_dummies(df, columns=['fbs', 'restecg', 'exang', 'slope', 'nar', 'hc', 'sk'])


    # padronizando variaveis continuas
    cont_col = ['trestbps', 'chol', 'thalach', 'oldpeak', 'ca', 'thal', 'trf'] 
    scaler = ColumnTransformer ([('scaler', StandardScaler(), cont_col)], remainder='passthrough')

    scaler.fit(cat_df)
    features = scaler.transform(cat_df)

    return features

def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Code for predict sex.')
    parser.add_argument('--input_file', type=str, required=True,
                    help='path of input file.csv', default='/')
    return parser.parse_args(argv)

def main(args):

    print('Caminho do diretorio analisado: {}'.format(args.input_file))
    filename = abspath(args.input_file)
    print(filename)
    df = pd.read_csv(filename)
    features = Preprocessing_data(df)

    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)

    out_predict = model.predict(features)

    pd.DataFrame(out_predict, columns=['sex']).to_csv('newsample_PREDICTIONS_Luiz_Gustavo_Ribeiro.csv', index=False)


if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))