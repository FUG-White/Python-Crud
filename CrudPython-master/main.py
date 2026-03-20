from db import Usuario, Session

# # GET - Buscar usuários

# with Session() as sessao:
#     usuarios = sessao.query(Usuario).all()

#     for usuario in usuarios:
#         print(usuario.nome)
#         print(usuario.email)
#         print(usuario.idade)
#         print("===========")


# GET - Buscar usuário por id

# with Session() as sessao:
#     usuario = sessao.query(Usuario).filter_by(nome= "Rafael ").first()

#     if usuario:
#         print(usuario.nome)
#         print(usuario.email)
#         print(usuario.idade)


# POST  Criar usuário
# with Session() as sessao:
#     while True:
#      nome = input("Nome: ")
#      email = input("Email: ")
#      idade = input("Idade: ")
 
#      novo_usuario = Usuario(nome=nome, email=email, idade=idade)
#      sessao.add(novo_usuario)
#      sessao.commit()




# # PUT/PATCH - Atualizar usuário

# with Session() as sessao:
#     usuario = sessao.query(Usuario).filter_by(id=1).first()

#     if usuario:
#         usuario.nome = "Lucas"
#         sessao.commit()


# DELETE - Deletar usuário
# with Session() as sessao:
#     usuario = sessao.query(Usuario).filter_by(id=1).first()

#     if usuario:
#         sessao.delete(usuario)
#         sessao.commit()
