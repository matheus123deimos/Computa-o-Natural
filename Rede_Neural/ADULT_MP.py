from Neural_Network_Implematation import M_Perceptron
from random import shuffle

#Declarações
INsB = []
INsC = []
INsD = []
INsE = []
EPOCA_L = []
TESTE_L = []
TB = {}
TBT = {}
NUMERO_DE_EPOCAS = 35

#Hiper_Parametros
CAMADAS_OCULTAS= 1
TAXA_DE_APRENDIZADO= 0.75
CONSTANTE_DE_MOMENTO= 0.0
VARIANTE_DE_TRANSFERENCIA=1
INTERVALO_DOS_PESOS= 19
APROX_CASAS = 3
QNCO = 8

#Dicionarios de Tratamento de Dados
WORKCLASS = {'Private':0.0,'Self-emp-not-inc':1.0,'Self-emp-inc':2.0,'Federal-gov':3.0,'Local-gov':4.0,'State-gov':5.0,'Without-pay':6.0,'Never-worked':7.0}

EDUCATION = {'Bachelors':0.0,'Some-college':1.0,'11th':2.0,'HS-grad':3.0,'Prof-school':4.0,'Assoc-acdm':5.0,'Assoc-voc':6.0,'9th':7.0,
             '7th-8th':8.0,'12th':9.0,'Masters':10.0,'1st-4th':11.0,'10th':12.0,'Doctorate':13.0,'5th-6th':14.0,'Preschool':15.0}

MARITAL_STATUS = {'Married-civ-spouse':0.0,'Divorced':1.0,'Never-married':2.0,'Separated':3.0,'Widowed':4.0,'Married-spouse-absent':5.0,'Married-AF-spouse':6.0}

OCCUPATION = {'Tech-support':0.0,'Craft-repair':1.0,'Other-service':2.0,'Sales':3.0,'Exec-managerial':4.0,'Prof-specialty':5.0,'Handlers-cleaners':6.0,
              'Machine-op-inspct':7.0,'Adm-clerical':8.0,'Farming-fishing':9.0,'Transport-moving':10.0,'Priv-house-serv':11.0,'Protective-serv':12.0,'Armed-Forces':13.0}

RELATIONSHIP = {'Wife':0.0,'Own-child':1.0,'Husband':2.0,'Not-in-family':3.0,'Other-relative':4.0,'Unmarried':5.0}

RACE = {'White':0.0,'Asian-Pac-Islander':1.0,'Amer-Indian-Eskimo':2.0,'Other':3.0,'Black':4.0}

SEX = {'Female':0.0,'Male':1.0}

NATIVE_COUNTRY = {'United-States':0.0,'Cambodia':1.0,'England':2.0,'Puerto-Rico':3.0,'Canada':4.0,'Germany':5.0,'Outlying-US(Guam-USVI-etc)':6.0,'India':7.0,'Japan':8.0,'Greece':9.0,
                  'South':10.0,'China':11.0,'Cuba':12.0,'Iran':13.0,'Honduras':14.0,'Philippines':15.0,'Italy':16.0,'Poland':17.0,'Jamaica':18.0,'Vietnam':19.0,
                  'Mexico':20.0,'Portugal':21.0,'Ireland':22.0,'France':23.0,'Dominican-Republic':24.0,'Laos':25.0,'Ecuador':26.0,'Taiwan':27.0,'Haiti':28.0,'Columbia':29.0,
                  'Hungary':30.0,'Guatemala':31.0,'Nicaragua':32.0,'Scotland':33.0,'Thailand':34.0,'Yugoslavia':35.0,'El-Salvador':36.0,'Trinadad&Tobago':37.0,'Peru':38.0,'Hong':39.0,
                  'Holand-Netherlands':40.0}

GANHO = {'>50K':[0.0],'<=50K':[1.0]}

#tratamento do data_set adult_L.txt
file = open('adult_L.txt','r')
for linha in file:
   if(linha.count(' ')==14 and not('?' in linha)):
      AUXILIAR = linha.replace(' ','').replace('\n','').split(',')
      del(AUXILIAR[2])
      del(AUXILIAR[3])
      for i in range(len(AUXILIAR)):
          if(i==0):#AGE
              AUXILIAR[i] = float(AUXILIAR[i])
          elif(i==1):#WORKCLASS
               AUXILIAR[i] = WORKCLASS[AUXILIAR[i]]
          elif(i==2):#EDUCATION
               AUXILIAR[i] = EDUCATION[AUXILIAR[i]]
          elif(i==3):#MARITAL_STATUS
               AUXILIAR[i] = MARITAL_STATUS[AUXILIAR[i]]
          elif(i==4):#OCCUPATION
               AUXILIAR[i] = OCCUPATION[AUXILIAR[i]]
          elif(i==5):#RELATIONSHIP
               AUXILIAR[i] = RELATIONSHIP[AUXILIAR[i]]
          elif(i==6):#RACE
               AUXILIAR[i] = RACE[AUXILIAR[i]]
          elif(i==7):#SEX
               AUXILIAR[i] = SEX[AUXILIAR[i]] 
          elif(i==8):#CAPITAL_GAIN
               AUXILIAR[i] = float(AUXILIAR[i])
          elif(i==9):#CAPITAL_LOSS
               AUXILIAR[i] = float(AUXILIAR[i])
          elif(i==10):#HOURS-PER-WEEK
               AUXILIAR[i] = float(AUXILIAR[i])
          elif(i==11):#NATIVE-COUNTRY
               AUXILIAR[i] = NATIVE_COUNTRY[AUXILIAR[i]]
          elif(i==12):#GANHO
               AUXILIAR[i] = GANHO[AUXILIAR[i]]
               
      INsB.append(AUXILIAR[0:12])
      INsC.append(AUXILIAR[12])
                  
                          
                   
#tratamento do data_set adult_L.txt
file = open('adult_T.txt','r')
for linha in file:
      if(linha.count(' ')==14 and linha != '|1x3 Cross validator'and not('?' in linha)):
         AUXILIAR = linha.replace(' ','').replace('\n','').replace('.','').split(',')
         del(AUXILIAR[2])
         del(AUXILIAR[3])
         for i in range(len(AUXILIAR)):
            if(i==0):#AGE
                AUXILIAR[i] = float(AUXILIAR[i])
            elif(i==1):#WORKCLASS
                AUXILIAR[i] = WORKCLASS[AUXILIAR[i]]
            elif(i==2):#EDUCATION
                AUXILIAR[i] = EDUCATION[AUXILIAR[i]]
            elif(i==3):#MARITAL_STATUS
                AUXILIAR[i] = MARITAL_STATUS[AUXILIAR[i]]
            elif(i==4):#OCCUPATION
                AUXILIAR[i] = OCCUPATION[AUXILIAR[i]]
            elif(i==5):#RELATIONSHIP
                AUXILIAR[i] = RELATIONSHIP[AUXILIAR[i]]
            elif(i==6):#RACE
                AUXILIAR[i] = RACE[AUXILIAR[i]]
            elif(i==7):#SEX
                AUXILIAR[i] = SEX[AUXILIAR[i]] 
            elif(i==8):#CAPITAL_GAIN
                AUXILIAR[i] = float(AUXILIAR[i])
            elif(i==9):#CAPITAL_LOSS
                AUXILIAR[i] = float(AUXILIAR[i])
            elif(i==10):#HOURS-PER-WEEK
                AUXILIAR[i] = float(AUXILIAR[i])
            elif(i==11):#NATIVE-COUNTRY
                AUXILIAR[i] = NATIVE_COUNTRY[AUXILIAR[i]]
            elif(i==12):#GANHO
                AUXILIAR[i] = GANHO[AUXILIAR[i]]
             
         INsD.append(AUXILIAR[0:12])
         INsE.append(AUXILIAR[12])
		        
               
LIS_AUX1 = list(INsB)
LIS_AUX2 = list(INsD)

#Criação da Lista_de_Epocas
for _ in range(NUMERO_DE_EPOCAS):
    shuffle(LIS_AUX1)
    #if(not(LIS_AUX in EPOCA_L)):
    EPOCA_L.append(LIS_AUX1)

#Criação da Lista_de_Teste
for _ in range(NUMERO_DE_EPOCAS):
    shuffle(LIS_AUX2)
    #if(not(LIS_AUX in EPOCA_L)):
    TESTE_L.append(LIS_AUX2)

#Criação das Tabela_de_Época
for i in range(len(INsB)):
    TB[str(INsB[i])] = INsC[i]

#Criação das Tabela_de_Teste
for i in range(len(INsD)):
    TBT[str(INsD[i])] = INsE[i]

PARAMETROS = (CAMADAS_OCULTAS,TAXA_DE_APRENDIZADO,CONSTANTE_DE_MOMENTO,VARIANTE_DE_TRANSFERENCIA,INTERVALO_DOS_PESOS,APROX_CASAS,QNCO)              

ADULT = M_Perceptron(12,1,PARAMETROS,TB)
ADULT.learning_teste(EPOCA_L,TESTE_L,TBT)
