import csv #Importamos o CSV

with open("lista_de_compras.tsv","w",newline="",encoding="utf-8") as csvFile:
   CsvWriter = csv.writer(csvFile,delimiter="\t",lineterminator="\n")
   
   CsvWriter.writerow(["maçãs","bananas","morangos"])
   CsvWriter.writerow(["leite","iogurte","queijo"])
   CsvWriter.writerow(["sabão","detergente","esponja"])

