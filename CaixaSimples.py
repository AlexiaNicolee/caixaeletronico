def caixa_eletronico(saque):
    notas_disponiveis = [100, 50, 10, 5, 1] 
    notas_fornecidas = {}

    for nota in notas_disponiveis:
        notas_fornecidas[nota] = saque // nota
        saque %= nota

    return notas_fornecidas


def main():

    valor_minimo = 10
    valor_maximo = 600
    
    while True:
        try:        
            saque = int(input("Qual o valor do saque desejado (entre {} e {})? ".format(valor_minimo, valor_maximo)))
            
            if valor_minimo <= saque <= valor_maximo:
                resultado = caixa_eletronico(saque)
                print("Notas fornecidas:")
                
                for nota, quantidade in resultado.items():
                    if quantidade > 0:
                        print("{} nota(s) de {} reais".format(quantidade, nota))
                
            else: 
                print("Valor inválido. O valor deve estar entre {} e {} reais".format(valor_minimo, valor_maximo))

            continuar = input("Deseja realizar outro saque? (Digite 's' para sim ou digite qualquer outra tecla para sair): ")
            if continuar.lower() != 's': 
                break
        except ValueError:
            print("Valor inválido, tente novamente com valores inteiros.")


if __name__ == "__main__":
    main()

