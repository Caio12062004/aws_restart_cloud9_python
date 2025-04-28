# Importando Módulos
import csv  # Importando módulo csv para trabalhar com arquivos CSV
import copy  # Importando módulo de cópia para criar cópias profundas de objetos

# Definindo o Dicionário
myVehicle = {
    "vin": "<empty>",  # Número de Identificação do Veículo, inicialmente vazio
    "make": "<empty>",  # Fabricante do veículo, inicialmente vazio
    "model": "<empty>",  # Modelo do veículo, inicialmente vazio
    "year": 0,  # Ano de fabricação, inicialmente 0
    "range": 0,  # Alcance do veículo, inicialmente 0
    "topSpeed": 0,  # Velocidade máxima do veículo, inicialmente 0
    "zeroSixty": 0.0,  # Tempo para acelerar de 0 a 60 mph, inicialmente 0,0
    "mileage": 0,  # Quilometragem do veículo, inicialmente 0
}

# Verificando o Dicionário
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Definindo a Lista para Inventário de Carros
myInventoryList = []  # Criando uma lista vazia para o inventário de veículos

# Lendo e copiando dados do arquivo CSV
with open("car_fleet.csv") as csvFile:  # Abra o arquivo CSV para leitura
    csvReader = csv.reader(
        csvFile, delimiter=","
    )  # Crie um objeto leitor CSV para ler o arquivo
    lineCount = 0  # Inicializar um contador de linha

    for row in csvReader:  # Iterar sobre cada linha no arquivo CSV
        if lineCount == 0:  # Verifique se é a primeira linha (cabeçalho)
            print(f'Column names are: {", ".join(row)}')  # Imprima os nomes das colunas
            lineCount += 1  # Incrementa o contador de linhas
        else:
            # Imprima cada campo na linha com seu valor correspondente
            print(
                f"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}"
            )

            currentVehicle = copy.deepcopy(
                myVehicle
            )  # Crie uma cópia profunda do dicionário myVehicle

            # Atribuir valores da linha CSV às chaves correspondentes no dicionário
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            myInventoryList.append(
                currentVehicle
            )  # Adicione o dicionário preenchido à lista de inventário

            lineCount += 1  # Incrementa o contador de linhas

    print(f"Processed {lineCount} lines.")  # Imprima o número total de linhas processadas

# Imprimindo o inventário do carro
for myCarProperties in myInventoryList:  # Iterar sobre cada carro na lista de inventário
    for (
        key,
        value,
    ) in (
        myCarProperties.items()
    ):  # Iterar sobre cada par chave-valor no dicionário do carro
        print(
            "{} : {}".format(key, value)
        )  # Imprima cada chave e seu valor correspondente
    print("-----")  # Imprima um separador entre os carros