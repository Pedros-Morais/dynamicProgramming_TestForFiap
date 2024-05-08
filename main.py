def getValues(list1, list2, k):
    values = []
    
    for d in list1:
        value = d.get(k)
        if value is not None:
            values.append(value)
    
    for d in list2:
        value = d.get(k)
        if value is not None:
            values.append(value)
    
    return values

listOne = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
listTwo = [{'c': 7, 'd': 8}, {'c': 9, 'd': 10}, {'c': 11, 'd': 12}]
k = 'a'
values = getValues(listOne, listTwo, k)
print(values)  

# Output: [1, 3, 5]


def calcMediaProduct(products):
    price_per_product = {}

    for product, price in products.items():
        if product in price_per_product:
            price_per_product[product].append(price)
        else:
            price_per_product[product] = [price]

    media_per_product = {}

    for product, prices in price_per_product.items():
        media = sum(prices) / len(prices)
        media_per_product[product] = media

    return media_per_product

def receber_dados():
    products = {}
    for i in range(1, 9):
        product = input(f"Digite o nome do {i}º produto: ")
        price = float(input(f"Digite o preço do {i}º produto: "))
        products[product] = price
    return products

def main():
    print("Bem-vindo ao programa de agrupamento e cálculo da média de preços!")
    print("Por favor, insira os nomes e preços de 8 produtos.")

    product = receber_dados()

    media_por_produto = calcMediaProduct(product)

    print("\nMédia de preço para cada produto:")
    for product, media in media_por_produto.items():
        print(f"{product}: R${media:.2f}")

if __name__ == "__main__":
    main()

# Calc Produto


def registerFails():
    num_machines = int(input("Digite o número de máquinas na fábrica: "))

    register_fails = {}

    for machine in range(1, num_machines + 1):
        num_fails = int(input(f"Digite o número de falhas para a máquina {machine}: "))

        fails_machine = {}

        for i in range(num_fails):
            type_fail = input(f"Digite o tipo da {i+1}ª falha para a máquina {machine}: ")
            fails_machine[type_fail] = fails_machine.get(type_fail, 0) + 1

        register_fails[f"Máquina {machine}"] = fails_machine

    return register_fails

def print_resume(register_fail):
    print("\nResumo das falhas por máquina:")
    for machine, fail_in_machine in register_fail.items():
        print(f"\n{machine}:")
        for type_fail, quanty in fail_in_machine.items():
            print(f"Tipo: {type_fail} - Quantidade: {quanty}")

def main():
    print("Bem-vindo ao sistema de registro de falhas de máquinas!")
    registeringFail = registerFails()
    print_resume(registeringFail)

if __name__ == "__main__":
    main()


#Maquina
import numpy as np

def matriz_rotacao(theta):
    theta_rad = np.radians(theta)

    matriz_rot = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                           [np.sin(theta_rad), np.cos(theta_rad)]])
    return matriz_rot

def recalcPerson(person, fact_x, fact_y):
    red = np.array([[fact_x, 0],
                                         [0, fact_y]])

    person_red = np.dot(person, red)
    return person_red

def simular_animacao(person, theta, fact_x, fact_y):
    matriz_rot = matriz_rotacao(theta)

    rotate = np.dot(person, matriz_rot)

    person_red = recalcPerson(rotate, fact_x, fact_y)

    return person_red

def showResult(personagem):
    print("Personagem inicial:")
    print(personagem)

def main():
    inicialPerson = np.array([[0, 0],[1, 0],[1, 1],[0, 1],[0, 0]])

    theta = 10  
    fact_x = 1.2  
    fact_y = 0.3  
    animatedPerson = simular_animacao(inicialPerson, theta, fact_x, fact_y)

    showResult(animatedPerson)

if __name__ == "__main__":
    main()
