import gspread
from indeed import search_ideed
from stackoverflow import search_so
from save import save_to_csv

#busca
search = 'python'

#salva resultado do indeed
result_indeed = search_ideed(search)
#salva resultado do indeed
result_so = search_so(search)

#junta os resultados em all_results
all_resuts = result_indeed + result_so

#envia para salvar no csv
save_to_csv(all_resuts)

#enviar os dados para a planilha
spreadsheetId = '1uRDAuGudRxYx77JH4b1wnYNflaFo0cemk3bG3ocTh_A'
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key(spreadsheetId)
worksheet = sh.sheet1

csvFile = 'jobs.csv'
sheetName = 'CSV'

content = open('jobs.csv', 'r').read()
gc.import_csv(spreadsheetId, content.encode('utf-8'))
