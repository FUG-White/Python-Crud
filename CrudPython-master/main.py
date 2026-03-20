from db import Usuario, Session

# with Session() as sessao:
#    usuario = sessao.query(Usuario).filter_by(id=1).first()
#    sessao.delete(usuario)
#    sessao.commit()



#   usuario = sessao.query(Usuario).filter_by(id).first()
# print(usuario.nome)



#  usuarios = sessao.query(Usuario).all()
# for usuario in usuarios:
#  print(usuario.nome)
#  print(usuario.email)
#  print(usuario.idade)
#  print("===========")










with Session() as sessao:
 while True:
    nome = input("Nome: ")
    email = input("Email: ")
    idade = input("Idade: ")

    novo_usuario= Usuario(nome= nome, email=email, idade=idade)
    sessao.add(novo_usuario)
    sessao.commit()
    sessao.close()