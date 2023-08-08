
#Sistema por tras de um biblioteca!!!
class Biblioteca():
    def __init__(self, gerente):
        self.gerente = gerente

        self.banco_dados_usuarios = []
        self.livro_emprestado = []
        # Banco de dados da biblioteca
        self._livros_cadastrados = [
            {'titulo': 'Dom Quixote', 'ano': '1605', 'autor': 'Miguel de Cervantes', 'genero': 'Romance'}, 
            {'titulo': '1984', 'ano': '1949', 'autor': 'George Orwell', 'genero': 'Distopia'}, 
            {'titulo': 'A Guerra dos Tronos', 'ano': '1996', 'autor': 'George R.R. Martin', 'genero': 'Fantasia'}, 
            {'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Fábula'}, 
            {'titulo': 'Crime e Castigo', 'ano': '1866', 'autor': 'Fiódor Dostoiévski', 'genero': 'Romance'}, 
            {'titulo': 'O Hobbit', 'ano': '1937', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia'}, 
            {'titulo': 'Percy Jackson e o Ladrão de Raios', 'ano': '2005', 'autor': 'Rick Riordan', 'genero': 'Fantasia'}
        ]
        
        self._estoque = [ 
            {'Codigo do Livro': '0001', 'titulo': 'Dom Quixote', 'ano': '1605', 'autor': 'Miguel de Cervantes', 'genero': 'Romance'},
            {'Codigo do Livro': '0032', 'titulo': 'A Guerra dos Tronos', 'ano': '1996', 'autor': 'George R.R. Martin', 'genero': 'Fantasia'}
        ]

    def cadastrar_cliente(self, nome, idade):
        cliente = {
            "Nome" : nome, 
            "Idade" : idade,
        }
        self.banco_dados_usuarios.append(cliente)
        


    def cadastrar_livro(self, codigo, titulo, ano, autor, genero):
        livro = {
            "Codigo do Livro" : codigo,
            "titulo": titulo,
            "ano": ano,
            "autor": autor,
            "genero": genero
        }
        self._livros_cadastrados.append(livro)
        self._estoque.append(livro)

        #e uma lista entao tem index
    def emprestar_livro(self, titulo, nome):
        for usuarios in self.banco_dados_usuarios:
            
            if (usuarios["Nome"] == nome):
                for livro_cadastrado in self._livros_cadastrados:

                    if livro_cadastrado['titulo'] == titulo: 
                        for livro_estoque in self._estoque:

                            if livro_estoque['titulo'] == titulo:  
                                emprestimo = {
                                    "Livro" : livro_estoque,
                                    "Usuario" : nome
                                }
                                self.livro_emprestado.append(emprestimo)
                                self._estoque.remove(livro_estoque)
                                print(f"O livro: {titulo} foi emprestado para {nome}")
                                return

                            elif livro_estoque['titulo'] not in self._estoque:
                                print(f"O livro {titulo} ja foi emprestado")
                            else:
                                print(f"O livro {titulo} nao esta disponnivel no momento")
                    else:
                        print(f"O livro: {titulo} nao esta cadastrado no nosso banco de dados")
            else:
                print("Cliente nao cadastrado")

    def devolver_livro(self, codigo):
        for livro in self.livro_emprestado:
            if (livro['Livro']['Codigo do Livro'] == codigo):
                self.livro_emprestado.remove(livro)
                self._estoque.append(livro["Livro"])
    
    def pesquisar_livros(self, categoria, conteudo):
        for livro in self._livros_cadastrados:
            if livro[categoria] == conteudo:
                print("Livro: {}".format(livro["titulo"]))
            
            
    

gerente = Biblioteca('Juan')
gerente.cadastrar_cliente("Pedro", "18")

gerente.cadastrar_livro("1518","Frankenstein", "1998", "Mary Shelley", "Suspense")
print(gerente.emprestar_livro("Frankenstein", "Pedro"))
print(gerente.devolver_livro("1518"))
print(gerente.pesquisar_livros('genero',"Suspense"))

