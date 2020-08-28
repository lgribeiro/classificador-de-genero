# classificador-de-genero

## Desafio Classificação de Gênero
Este projeto consiste em :
- Analisar dados de pacientes
- Construir um modelo de predição de gênero {Masculino: M, Feminino:F}

## Instalação do python3.X e atualizações de suas bibliotecas.

### 1. Instalando python3.x no Unix ou Windows
Uma boa prática de programação é criar um ambiente isolado de desenvolvimento para o Python3 e suas dependências (Virtual Environments - env). Abaixo alguns tutoriais de como criar um ambiente virtual.

https://virtualenvwrapper.readthedocs.io/en/latest/
https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

Como alternativa prática, o Framework Anaconda pode ser instalado. Por ser uma ferramente computacional gratuita e de fácil instalação que permite gerir distribuições de Python (e meu S.O é windows) eu preferi usa-la.
Abaixo segue o link da documentação do Anaconda com o passo-a-passo da instalação em vários sistemas operacionais.

https://docs.anaconda.com/anaconda/install/

### 2. Instalando e atualizando bibliotecas

Se você criou seu prórpio ambiente (Virtual Environments - env) execute no terminal o comando  abaixo para atualizar as bibliotecas necessárias.

```
pip install -r requirements.txt

```
Se optou pelo Anaconda execute o comando abaixo no terminal da aplicação:

```
conda update --all
```
### 3. Executando o classificador de gênero
O modelo classificará a partir de um lote de dados de pacientes, arquivo .csv, se o genêro é masculino: M ou feminino: F. O resultado e exportado na raiz da pasta do projeto como 'newsample_PREDICTIONS_Luiz_Ribeiroo.csv'.
Para executar o classificador use o seguinte comando 

```
python gender_predictor.py --input_file newsample.csv
```
### 4. Base de dados
A base de dados, test_data_CANDIDATE.csv, que se encontra na raiz do projeto será usada para treinar o modelo de classificação de gênero. 
Observação: A base de dados fornecida carece de fonte.

## Descrição da base de dados 

- age: in years
- sex: (M = male; F = female)
- cp: chest pain type
- trestbps: resting blood pressure (in mm Hg on admission to the hospital)
- chol: serum cholesterol in mg/dl
- fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
- restecg: resting electrocardiographic results
- thalach: maximum heart rate achieved
- nar: number of arms
- exang: exercise induced angina (1 = yes; 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: the slope of the peak exercise ST segment
- hc: patient's hair colour
- sk: patient's skin colour
- trf: time spent in traffic daily (in seconds)
- ca: number of major vessels (0-3) colored by flourosopy
- thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

### 5. Modelos de classificação



<img src="/images/scikit-learn.png" alt="Scikit-Learn"/>


![Scikit-Learn](https://github.com/lgribeiro/classificador-de-genero/blob/dev/scikit-learn.png)


A Scikit-Learn é uma biblioteca  para trabalhar com machine learning em python. Essa poderosa ferramente construida em NumPy, SciPy e matplotlib é simple e eficiente para análise preditiva de dados.
Vamos usa-lá em nosso classificador!
Com base na análise da descrição dos dados, foram escolhido os seguintes classificadores:
- Decision Tree 
- Random Forest
- Logistic Regression 
- SVC
- Naive Bayes
- KNN
- MLP

#### Explicando os modelos
TODO
### 6. Análise dos Resultados
TODO
#### Métricas analisadas
TODO

## Referencias:

https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py

https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix

https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation

https://scikit-learn.org/stable/tutorial/basic/tutorial.html

https://www.vooo.pro/insights/fundamentos-dos-algoritmos-de-machine-learning-com-codigo-python-e-r/

https://www.vooo.pro/insights/6-passos-faceis-para-aprender-o-algoritmo-naive-bayes-com-o-codigo-em-python/

https://semantix.com.br/10-algoritmos-de-machine-learning-que-voce-precisa-conhecer/

http://www.inf.ufpr.br/menotti/am-17/slides/ML-08cluster-regression.pdf

https://andersonuyekita.github.io/notebooks/blog/2019/03/21/como-usar-o-gridsearchcv/
