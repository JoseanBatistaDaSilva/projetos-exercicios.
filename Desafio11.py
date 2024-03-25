Msg=("Olá, seja bem vindo")
print(Msg)
print("Por favor digite os valores a seguir em metros, se for necessário faça asa devidas conversões")
Largura=float(input("Digite a largura da parede:"))
Altura=float(input("Digite a altura da parede:"))
Area=Largura*Altura
Tinta=float(Area/2)
print(f"A largura da parede é de {Largura} e sua altura {Altura}, logo sua área e de {Area}.\nSerá necessário {Tinta}","litros de tinta")

