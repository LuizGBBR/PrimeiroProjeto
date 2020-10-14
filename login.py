from PyQt5 import uic,QtWidgets
import sqlite3

def chama_segunda_tela():
    #faz com q a lab 4 não apareça nada e limpa o campo depois de colocar a informação certa
    primeira_tela.label_4.setText("")
    #criar uma variavel chamando a 1tela no lineedit(que é o nome da area do login) e colocando como texto
    nome_usuario = primeira_tela.lineEdit.text()
    #fez a mesma coisa de cima
    senha = primeira_tela.lineEdit_2.text()
    #agr a condiç para aparecer a proxima tela
    if nome_usuario == "ifpe123" and senha == "ifpe321":
        #se a condiç de cima passar ele fecha a 1 tela e abre a 2
        primeira_tela.close()
        segunda_tela.show()
    else:
        #na 1 tela na label 4 vai mostrar o texto...
        primeira_tela.label_4.setText("Dados de login incorretos!")


def sair():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()

def abre_tela_adicionar_produto():
    adicionar_produto.show()

def sair1():
    adicionar_produto.close()
    segunda_tela.show()

def abre_tela_estoque():
    estoque.show()

def sair2():
    estoque.close()
    segunda_tela.show()

def abre_tela_atendimento():
    atendimento.show()

def sair3():
    atendimento.close()
    segunda_tela.show()



def cadastrar():
    #aqui vamos salvar os dados informados em cada campo em uma variavel
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    #aqui vemos se as senhas estão iguais
    if (senha == c_senha):
        try:
            #essa parte cria um banco de dados nas pastas ao lado, se ja existir ele n é executado
            banco = sqlite3.connect('banco_cadastro.db')
            #esse cursor serve para manipular os dados do banco
            cursor = banco.cursor()
            #aqui fazemos comandos no banco de dados
            #no 1 criamos uma tabela caso n exista com nome cadastro, com os seguintes campos...
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            #comita as alterações/executa elas...
            banco.commit()
            #fecha o banco
            banco.close()
            #dps disso a pessoa informa que foi feito com sucesso 
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        #se der erro ou senha errada...
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")

def sair4():
    tela_cadastro.close()



#aqui vamos fazer a declaração dos arquivos feitos no QTdesigner
app=QtWidgets.QApplication([])
#aqui vamos chamar a 1 e 2 tela, elas devem esta nas pastas ao lado
#nome da tela = uic.loadUI("nome do arquivo ao lado")
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
adicionar_produto = uic.loadUi("adicionar_produto.ui")
atendimento = uic.loadUi("atendimento.ui")
estoque = uic.loadUi("estoque.ui")

#aqui vamos conectar a primeira tela com a segunda ou ao contrario
#na 1 tela quando clicar no pushbutton vai connect a variavel chama_segunda_tela...
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
#na 2 tela quando clicar no pushb_4 vai retornar a função 'sair' que fecha a segunda e abre a 1...
segunda_tela.pushButton_4.clicked.connect(sair)
#isso ira transformar a senha naquelas bolinhas...
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
#quando clicar no pushb_2 vai conectar a função abre_tela... e abrir o cadastro
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
#aqui é o botao de cadastro na tela de cadastrar
tela_cadastro.pushButton.clicked.connect(cadastrar)
#sair cadastro
tela_cadastro.pushButton_2.clicked.connect(sair4)
#abrir tela de add prod no estoque
segunda_tela.pushButton.clicked.connect(abre_tela_adicionar_produto)
#aqui quando clicar no sair da tela de add prod ele volta para a principal
adicionar_produto.pushButton.clicked.connect(sair1)
#aqui abre a tela de estoque
segunda_tela.pushButton_3.clicked.connect(abre_tela_estoque)
#aq sai da tela de estoque
estoque.pushButton.clicked.connect(sair2)
#abrir tela de atendimento
segunda_tela.pushButton_2.clicked.connect(abre_tela_atendimento)
#sair tela de atend
atendimento.pushButton.clicked.connect(sair3)

#quando der play ele vai começar nessa tela...
primeira_tela.show()
app.exec()
