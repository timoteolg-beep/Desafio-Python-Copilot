# Desafio de Projeto: Resolvendo Códigos em Python com o Github Copilot

def limpar_terminal():
    """Imprime linhas para separar visualmente as execuções."""
    print("\n" + "="*40 + "\n")

def ler_numero(mensagem):
    """
    Função auxiliar para ler números (int ou float) de forma robusta.
    Melhoria: Aceita tanto '.' quanto ',' como separador decimal.
    """
    while True:
        valor = input(mensagem).strip()
        # Tratamento para padrão brasileiro (vírgula)
        valor = valor.replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("❌ Erro: Entrada inválida. Por favor, digite um número.")

def concatenar_dados():
    """1 - Recebe dois dados e os concatena em uma string única."""
    info1 = input("Digite o primeiro dado: ").strip()
    info2 = input("Digite o segundo dado: ").strip()
    print(f"\n✅ Resultado Concatenado: {info1} {info2}")

def repetir_textos():
    """2 - Solicita uma string e um número inteiro, repetindo a string."""
    texto = input("Digite o texto: ").strip()
    while True:
        try:
            numero = int(input("Número de repetições (inteiro): "))
            break
        except ValueError:
            print("❌ Erro: O número de repetições deve ser um INTEIRO.")
    
    # Adiciona um espaço entre as repetições para legibilidade
    resultado = (texto + " ") * numero
    print(f"\n✅ Resultado:\n{resultado.strip()}")

def operacoes_matematicas():
    """3 - Realiza operações matemáticas básicas."""
    num1 = ler_numero("Digite o primeiro número: ")
    num2 = ler_numero("Digite o segundo número: ")
    
    operacao = input("Escolha a operação (+, -, *, /): ").strip()
    
    if operacao == '+':
        res = num1 + num2
    elif operacao == '-':
        res = num1 - num2
    elif operacao == '*':
        res = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            res = num1 / num2
        else:
            print("❌ Erro: Divisão por zero não permitida.")
            return
    else:
        print("❌ Operação inválida.")
        return

    print(f"\n✅ Resultado: {res:.2f}")

def verificar_par_impar():
    """4 - Verifica se um número inteiro é par ou ímpar."""
    while True:
        try:
            # Garante que seja inteiro, pois par/impar não se aplica a decimais de forma padrão
            entrada = input("Digite um número inteiro: ").strip()
            numero = int(entrada)
            break
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido.")

    status = "PAR" if numero % 2 == 0 else "ÍMPAR"
    print(f"\n✅ O número {numero} é {status}.")

def calcular_media():
    """5 - Calcula a média de 3 notas."""
    print("Vamos calcular a média de 3 notas.")
    notas = []
    # Loop escalável: fácil alterar para 4 ou 5 notas se necessário
    for i in range(1, 4):
        nota = ler_numero(f"Digite a nota {i}: ")
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    status_aluno = "Aprovado" if media >= 7 else "Reprovado"
    print(f"\n✅ Média: {media:.2f} - Status: {status_aluno}")

def verificar_palindromo():
    """6 - Verifica se uma palavra é um palíndromo."""
    texto = input("Digite uma palavra ou frase: ").strip()
    
    # Normalização: remove espaços e converte para minúsculas
    texto_limpo = texto.replace(" ", "").lower()
    texto_invertido = texto_limpo[::-1]
    
    if texto_limpo == texto_invertido:
        print(f"\n✅ '{texto}' é um PALÍNDROMO!")
    else:
        print(f"\n🔹 '{texto}' NÃO é um palíndromo.")
        print(f"   Invertido seria: {texto_invertido}")

def menu():
    """Função principal que gerencia o menu interativo."""
    # Mapeamento de funções (Pattern Matching)
    acoes = {
        '1': concatenar_dados,
        '2': repetir_textos,
        '3': operacoes_matematicas,
        '4': verificar_par_impar,
        '5': calcular_media,
        '6': verificar_palindromo
    }

    while True:
        limpar_terminal()
        print("🚀 === DESAFIO PYTHON + GITHUB COPILOT ===")
        print("1. Concatenar Dados")
        print("2. Repetir Textos")
        print("3. Operações Matemáticas")
        print("4. Par ou Ímpar")
        print("5. Calcular Média")
        print("6. Verificar Palíndromo")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '0':
            print("Encerrando o sistema... Até logo! 👋")
            break
        
        if opcao in acoes:
            limpar_terminal()
            acoes[opcao]() # Executa a função selecionada
        else:
            print("❌ Opção inválida, tente novamente.")
            
        # Pausa para o usuário ler o resultado
        input("\n[Pressione ENTER para voltar ao menu]")

if __name__ == "__main__":
    menu()
