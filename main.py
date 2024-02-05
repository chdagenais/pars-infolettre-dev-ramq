
import pandas as pd
import tabula as tb
import openpyxl


# TODO Modifier path avec le chemin du fichier à tester 
FILEPATH="./example/info304-23.pdf"

filename = FILEPATH.split("/")[-1].strip(".pdf")
# Read pdf and output table into a dataframe
df = tb.read_pdf(FILEPATH, pages='all',stream=True)


# print all tables from the pdf to console
for i in range(len(df)):
    print(df[i])
    print("\n")


# df[0] contient le tableau de la page 1
#use column CHAMP as index
df[0].set_index('CHAMP', inplace=True)


# print table to console
print(df[0].head(30))


# Si la ligne précédant demonimation commune est nan , la fusionner avec la ligne dessous
row_denomination = df[0].index.get_loc('Dénomination commune')

if pd.isna(df[0].index[row_denomination-1]):
    row_to_merge = df[0].index.get_loc('Dénomination commune') -1
    print(df[0].iloc[row_to_merge-1])
    #for each column, prepend the row to merge value with denomination commune row value and remove NaN row value
    for i in range(len(df[0].columns)):
        df[0].iloc[row_to_merge+1,i] = df[0].iloc[row_to_merge,i] + " " + df[0].iloc[row_to_merge+1,i]
        df[0].iloc[row_to_merge,i] = None
    # delete Nan row
    df[0].dropna(inplace=True)

print(df[0].head(30))



# export data to csv
df[0].to_csv(f'example/{filename}.csv')

#to excel
df[0].to_excel(f'example/{filename}.xlsx')


