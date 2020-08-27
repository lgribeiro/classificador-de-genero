
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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
    # removendo a coluna index se existir.
    if any("index" in s for s in col):        
        df = df.drop("index", axis=1)
        print("Removeu coluna: index")
            
    # identificando valores NaN
    if (df.isnull().any().any()) :
        df = df.dropna()
        print("Removeu linhas com valores ausentes")

    # removendo linhas duplicadas    
    if(df.duplicated().any().any()):
        df = df.drop_duplicates()
        print("removeu linhas duplicadas")
    
    col = df.columns 
    # removendo a coluna sex se existir, vamos predizer essa coluna!   
    if any("sex" in s for s in col):        
        df = df.drop("sex", axis=1)
        print("Removeu coluna: sex")

    # usando propriedades do desvio padrao para encontrar e remover colunas com o mesmo valor
    df = df.drop(df.std()[(df.std() == 0)].index, axis=1)

    # transformando int em float para todo dataframe
    numeric_columns = df.select_dtypes(['int64']).columns
    df[numeric_columns] = df[numeric_columns].astype('float32')

    return df

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
    df = Preprocessing_data(df)

    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
        
    features = df.values.tolist()
    features = StandardScaler().fit_transform(features)

    out_predict = model.predict(features)

    pd.DataFrame(out_predict, columns=['sex']).to_csv('newsample_PREDICTIONS_Luiz_Gustavo_Ribeiro.csv', index=False)


if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))