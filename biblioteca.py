
    
class Biblioteca():
    def __init__(self, usuario, genero_usuario):
        self.usuario = usuario
        self.genero = genero_usuario
        self._estoque = [{'titulo': 'Dom Quixote', 'ano': '1605', 'autor': 'Miguel de Cervantes', 'genero': 'Romance'}, 
                         {'titulo': '1984', 'ano': '1949', 'autor': 'George Orwell', 'genero': 'Distopia'}, 
                         {'titulo': 'A Guerra dos Tronos', 'ano': '1996', 'autor': 'George R.R. Martin', 'genero': 'Fantasia'}, 
                         {'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Fábula'}, 
                         {'titulo': 'Crime e Castigo', 'ano': '1866', 'autor': 'Fiódor Dostoiévski', 'genero': 'Romance'}, 
                         {'titulo': 'O Hobbit', 'ano': '1937', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia'}, 
                         {'titulo': 'Percy Jackson e o Ladrão de Raios', 'ano': '2005', 'autor': 'Rick Riordan', 'genero': 'Fantasia'}]
        

    
    def cadastrar_livro(self, titulo, ano, autor, genero):
        livro = {
            "titulo": titulo,
            "ano": ano,
            "autor": autor,
            "genero": genero 
        }
        self._estoque.append(livro)

    
class Estoque(Biblioteca):
    @property
    def estoque(self):
        return self._estoque
    pass

    def emprestar_livro(self):
        pass

    def devolver_livro(self):
        pass

    def multa(self):
        pass

    def pagmento(self):
        pass

    

    def categoria(self):
        #ordem alfabetica
        pass




    


Pessoa1 = Biblioteca("Juan", "Terror")
Pessoa1.cadastrar_livro("Frankenstein", "1998", "Mary Shelley", "Suspense")

