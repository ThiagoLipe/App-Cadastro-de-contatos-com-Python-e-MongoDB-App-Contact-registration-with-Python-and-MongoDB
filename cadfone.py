import mongoengine as me
import pymongo
from pymongo import MongoClient
client = MongoClient()

#Conectar ao mongoDB
me.connect('senac')

#Definir o modelo de contato
class Contato(me.Document):
    nome = me.StringField(required=True)
    telefone = me.StringField(required=True)

#Função para adicionar um novo contato
def adicionar_contato(nome, telefone):
    contato = Contato(nome=nome, telefone=telefone)
    contato.save()
    print(f"Contato {nome} adicionado com sucesso!")

#Função para listar todos os contatos
def listar_contatos():
    contatos = Contato.objects()
    for contato in contatos:
        print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")

#Função para editar um contato existente
def editar_contato(nome_antigo, novo_nome, novo_telefone):
    contato = Contato.objects(nome=nome_antigo).first()
    if contato:
        contato.nome = novo_nome
        contato.telefone = novo_telefone
        contato.save()
        print(f"Contato {nome_antigo} editado com sucesso!")
    else:
        print(f"Contato {nome_antigo} não encontrado.")

#Função para excluir um contato
def excluir_contato(nome):
    contato = Contato.objects(nome=nome).first()
    if contato:
        contato.delete()
        print(f"Contato {nome} excluído com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

#Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        print("\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(nome, telefone)

        elif escolha == "2":
            print("\nLista de Contatos:")
            listar_contatos()
            
        elif escolha == "3":
            nome_antigo = input("Digite o nome do contato a ser editado: ")
            novo_nome = input("Digite o novo nome do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")
            editar_contato(nome_antigo, novo_nome, novo_telefone)
            
        elif escolha == "4":
            nome = input("Digite o nome do contato a ser excluído: ")
            excluir_contato(nome)
            
        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()