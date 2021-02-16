import csv
import gspread

#funcao para salva no csv
def save_to_csv(jobs):
  #seleciona arquivo
  file = open('jobs.csv', 'w')
  writer = csv.writer(file)
  writer.writerow(['title','company', 'location', 'how old', 'link'])
 # worksheet.insert_row(job, x)
 # worksheet.append_row(job)
  
  #para cada job da lista recebida escreve 1 linha
  for job in jobs:
    writer.writerow(list(job.values()))