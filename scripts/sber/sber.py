import pandas as pd
import numpy as np
import json
with open('/home/akozlov/Загрузки/citi.json') as f:
    templates = json.load(f)
js1=[]
js2 = []
ids = templates[0].keys()
for i in ids:
    js1.append(i)
# ids = templates[1].keys()
# for i in ids:
#     js2.append(i)
# js = list(set(js1 + js2))
top_players = pd.read_excel('/home/akozlov/Документы/Project/Marvel/pimcore/pimcore/public/excelTemplates/sber/Струйное МФУ.xlsx', 'Струйное МФУ')
hed = top_players.values[1].tolist ()
result = list(set(js1) - set(hed))
result2 = list(set(hed) - set(js1))
print(f'Отличие в : {result}')
# print(hed)
# print(len(js2))