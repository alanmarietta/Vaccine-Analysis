import pandas as pd
import numpy as np

# Data QC
vaccine = pd.read_csv('vaccine_data.csv', header=None)
vaccine.columns = ['Region','Vaccine','Year','Percentage']
vaccine['Region'] = vaccine['Region'].str.replace('&', 'and').str.replace(' ','_')
vaccine['Year'] = vaccine['Year'].astype('string')
mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}
vaccine['Description'] = vaccine['Vaccine'].apply(lambda x: mappings[x])
vaccine = vaccine.dropna()


# Main method
def make_subset(df, region = None, vaccine = None, year = None, additive = True):
    if additive == False:
        if region != None and vaccine != None and year != None:
            df2 = df.loc[(df['Region'].isin(region)) | (df['Vaccine'].isin(vaccine)) | (df['Year'].isin(year))]
        else:
            df2 = df.copy()
    elif additive == True:
        if region == None:
            region = df['Region'].values.tolist()
        if vaccine == None:
            vaccine = df['Vaccine'].values.tolist()
        if year == None:
            year = df['Year'].values.tolist()
        df2 = df.loc[(df['Region'].isin(region)) & (df['Vaccine'].isin(vaccine)) & (df['Year'].isin(year))]
    return df2