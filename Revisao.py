ct = 0
soma = 0
revisao = int(input("Digite o valor correspondente ao conteudo:\n1 uso do for\n2 uso do def\n3 uso do list"))
if revisao == 1:
    alunos = int(input("Digite a quantidade de alunos:"))
    for i in range (1,alunos + 1,1):
        valor = float(input("Digite sua nota:"))
        ct = ct+1
        soma =soma +valor
    print(f"A média da sua nota é {soma/ct:.2f}")