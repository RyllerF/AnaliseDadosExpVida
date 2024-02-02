import pandas as pd 
import matplotlib.pyplot as plt

arquivo = pd.read_csv('life_expectancy.csv')
fle = arquivo['Female Life Expectancy'].mean()

#print (fle)

print(arquivo.describe())

filtro_bra = arquivo.loc[arquivo['Country Code'] == 'BRA']
tempo = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
filtro_bra_2000 = arquivo.loc[(arquivo['Country Code'] == 'BRA') & (arquivo['Year'].isin(tempo))]
#print (filtro_bra_2000)
##esta = filtro_bra.describe()
##print(filtro_bra)

plt.bar(filtro_bra_2000['Year'], filtro_bra_2000['Female Life Expectancy'],)
plt.xlabel("Anos")
plt.ylabel("Expectativa de Vida Feminina")
plt.title("Expectativa de vida Feminina Brasil (2010-2021)")
plt.xticks(rotation=90, ha="right")
plt.savefig("ExpectativaFemPaisBRA.png")
plt.show()



plt.bar(filtro_bra_2000['Year'], filtro_bra_2000['Male Life Expectancy'],)
plt.xlabel("Anos")
plt.ylabel("Expectativa de Vida Masculina")
plt.title("Expectativa de vida Masculina Brasil (2010-2021)")
plt.xticks(rotation=90, ha="right")
plt.savefig("ExpectativaMalePaisBRA.png")
plt.show()

paises_americadosul = ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'GUY', 'PRY', 'PER', 'SUR', 'URY', 'VEN']
filtro_americadosul_2021 = arquivo.loc[(arquivo['Country Code'].isin(paises_americadosul)) & (arquivo['Year'] == 2021)]
#print(filtro_americadosul_2021)

plt.bar(filtro_americadosul_2021['Country'], filtro_americadosul_2021['Female Life Expectancy'],)
plt.xlabel("Pais")
plt.ylabel("Expectativa de Vida Feminina")
plt.title("Expectativa de vida Feminina America do Sul")
plt.xticks(rotation=90, ha="right")
plt.savefig("ExpectativaFemPais.png")
plt.show()


plt.bar(filtro_americadosul_2021['Country'], filtro_americadosul_2021['Male Life Expectancy'],)

plt.xlabel("Pais")
plt.ylabel("Expectativa de Vida Masculina")
plt.title("Expectativa de vida Masculina America do Sul")
plt.xticks(rotation=90, ha="right")
plt.savefig("ExpectativaMascPais.png")
plt.show()


#print(filtro_americadosul_2021)


tipos = ['Female Life Min', 'Female Life Max', 'Male Life Min', 'Male Life Max']
df = pd.read_csv('brasil_min_max.csv')  
filtro_am = df.loc[(df['Type'].isin(tipos))]

plt.bar(filtro_am['Type'], filtro_am['Expectancy'],)
plt.xlabel("Categoria")
plt.ylabel("Expectativa")
plt.title("Expectativa de vida Minima e Maxima Brasil (1950-2021)")
plt.xticks(rotation=90, ha="right")
plt.savefig("ExpectativaMinMaxBR.png")
plt.show()

