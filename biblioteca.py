class Biblioteca():
    def __init__(self, gerente):
        self.gerente = gerente
        self.banco_dados_usuarios = []
        self.livro_emprestado = []
        self._livros_cadastrados = [
            {'Codigo do Livro': '0001', 'titulo': 'Dom Quixote', 'ano': '1605', 'autor': 'Miguel de Cervantes', 'genero': 'Romance'},
            {'Codigo do Livro': '0032', 'titulo': 'A Guerra dos Tronos', 'ano': '1996', 'autor': 'George R.R. Martin', 'genero': 'Fantasia'},
            {'Codigo do Livro': '0078', 'titulo': 'Orgulho e Preconceito', 'ano': '1813', 'autor': 'Jane Austen', 'genero': 'Romance Clássico'},
            {'Codigo do Livro': '0234', 'titulo': 'O Senhor dos Anéis: A Sociedade do Anel', 'ano': '1954', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia'},
            {'Codigo do Livro': '0321', 'titulo': 'Cem Anos de Solidão', 'ano': '1967', 'autor': 'Gabriel García Márquez', 'genero': 'Mágico'},
            {'Codigo do Livro': '0567', 'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Literatura'},
            {'Codigo do Livro': '0809', 'titulo': 'A Revolução dos Bichos', 'ano': '1945', 'autor': 'George Orwell', 'genero': 'Ficção'},
            {'Codigo do Livro': '1098', 'titulo': 'O Alquimista', 'ano': '1988', 'autor': 'Paulo Coelho', 'genero': 'Ficção'},
            {'Codigo do Livro': '1543', 'titulo': 'O Retrato de Dorian Gray', 'ano': '1890', 'autor': 'Oscar Wilde', 'genero': 'Ficção'},
            {'Codigo do Livro': '2015', 'titulo': '1984', 'ano': '1949', 'autor': 'George Orwell', 'genero': 'Ficção'},
            {'Codigo do Livro': '2356', 'titulo': 'Harry Potter e a Pedra Filosofal', 'ano': '1997', 'autor': 'J.K. Rowling', 'genero': 'Fantasia'},
        ]
#-------------------------------------------------------------------------------------------------------------------------------

        self._estoque = [
            {'Codigo do Livro': '0001', 'titulo': 'Dom Quixote', 'ano': '1605', 'autor': 'Miguel de Cervantes', 'genero': 'Romance'},
            {'Codigo do Livro': '0032', 'titulo': 'A Guerra dos Tronos', 'ano': '1996', 'autor': 'George R.R. Martin', 'genero': 'Fantasia'},
            {'Codigo do Livro': '0078', 'titulo': 'Orgulho e Preconceito', 'ano': '1813', 'autor': 'Jane Austen', 'genero': 'Romance Clássico'},
            {'Codigo do Livro': '0234', 'titulo': 'O Senhor dos Anéis: A Sociedade do Anel', 'ano': '1954', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia'},
            {'Codigo do Livro': '0321', 'titulo': 'Cem Anos de Solidão', 'ano': '1967', 'autor': 'Gabriel García Márquez', 'genero': 'Mágico'},
            {'Codigo do Livro': '0567', 'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Literatura'},
            {'Codigo do Livro': '0809', 'titulo': 'A Revolução dos Bichos', 'ano': '1945', 'autor': 'George Orwell', 'genero': 'Ficção'},
            {'Codigo do Livro': '1098', 'titulo': 'O Alquimista', 'ano': '1988', 'autor': 'Paulo Coelho', 'genero': 'Ficção'},
            {'Codigo do Livro': '1543', 'titulo': 'O Retrato de Dorian Gray', 'ano': '1890', 'autor': 'Oscar Wilde', 'genero': 'Ficção'},
            {'Codigo do Livro': '2015', 'titulo': '1984', 'ano': '1949', 'autor': 'George Orwell', 'genero': 'Ficção'},
            {'Codigo do Livro': '0001', 'titulo': 'Dom Quixote', 'ano': '1605', 'autor': 'Miguel de Cervantes', 'genero': 'Romance'},
            {'Codigo do Livro': '0032', 'titulo': 'A Guerra dos Tronos', 'ano': '1996', 'autor': 'George R.R. Martin', 'genero': 'Fantasia'}
        ]
#-------------------------------------------------------------------------------------------------------------------------------

    def cadastrar_cliente(self, nome, idade):
        cliente = {
            "Nome" : nome, 
            "Idade" : idade,
        }
        self.banco_dados_usuarios.append(cliente)
        return
    
#-------------------------------------------------------------------------------------------------------------------------------

    @property
    def cliente(self):
        return self.banco_dados_usuarios
        
#-------------------------------------------------------------------------------------------------------------------------------

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
        return

#-------------------------------------------------------------------------------------------------------------------------------

    def emprestar_livro(self, titulo, nome):
        usuario_encontrado = False
        livro_cadastrado = False

        for usario in self.banco_dados_usuarios:
            if usario["Nome"] == nome:
                usuario_encontrado = True

            
        if usuario_encontrado == True:
            for livro_pesquisado in self._livros_cadastrados:
                if livro_pesquisado["titulo"] == titulo:
                    livro_cadastrado = True
                    
            
            if livro_cadastrado == True:
                for livro_disponivel in self._estoque:
                    if livro_disponivel["titulo"] == titulo:
                        emprestimo = {
                            "Livro" : livro_disponivel,
                            "Usuario" : nome
                        }
                        self.livro_emprestado.append(emprestimo)
                        self._estoque.remove(livro_disponivel)
                        print(f"Pronto! O livro: {titulo} foi emprestado para {nome}")

            else:
                print(f"O livro: {titulo} não está no nosso sistema.")
        else: 
            print(f"O usuario {nome} não esta cadastrado no nosso sistema.")
        
#-------------------------------------------------------------------------------------------------------------------------------

    def devolver_livro(self, codigo):
        for livro in self.livro_emprestado:
            if (livro['Livro']['Codigo do Livro'] == codigo):
                self.livro_emprestado.remove(livro)
                self._estoque.append(livro["Livro"])
                return
#-------------------------------------------------------------------------------------------------------------------------------

    def pesquisar_livros(self, categoria, conteudo):
        for livro in self._livros_cadastrados:
            if livro[categoria] == conteudo:
                print("Livro: {}".format(livro["titulo"]))
        
#-------------------------------------------------------------------------------------------------------------------------------
            
    

gerente = Biblioteca('Juan')
gerente.cadastrar_cliente("Pedro", "18")
gerente.cadastrar_livro("1518","Frankenstein", "1998", "Mary Shelley", "Suspense")

print(gerente.emprestar_livro("Juan", "Pedro"))
print(gerente.devolver_livro("1518"))
print(gerente.pesquisar_livros('genero',"Ficção"))
print(gerente.cliente)

