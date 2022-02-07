
def comparar(usuario):

    if usuario == "jhon":
        print("usuario aceito")
    if usuario != "jhon":
        print("usuario incorreto")
        print("============")
        print("nome de usuario")
        user = input()
        comparar(user)


print("usuario")
nome_user = input()
comparar(nome_user)
