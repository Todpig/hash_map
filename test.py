class User:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return 'Nome: {}\nMatricula: {}'.format(self.nome, self.matricula)

def hash_value(key):
    return key % 10

def insert(hash_table, key,  value):
    hash = hash_value(key)
    if hash_table[hash]:
        [hash_table[hash]].append(value)
    else:
        hash_table[hash] = value

def seach(hash_table, key):
    hash = hash_value(key)
    if type(hash_table[hash]) == list:
        for i in range(len(hash_table[hash])):
            if hash_table[hash][i].matricula == key:
                return hash_table[hash][i]
    else:
        return hash_table[hash]

if __name__ == "__main__":
    hash_table = [[] for _ in range(10)]
    insert(hash_table, 1, User('Joao', 10))
    insert(hash_table, 2, User('Maria', 20))
    insert(hash_table, 3, User('Jose', 30))
    insert(hash_table, 4, User('Pedro', 40))
    insert(hash_table, 5, User('Ana', 50))
    insert(hash_table, 6, User('Paulo', 60))
    insert(hash_table, 7, User('Joana', 70))
    insert(hash_table, 8, User('Carlos', 80))
    insert(hash_table, 9, User('Marcos', 90))
    insert(hash_table, 10, User('Lucas', 100))
    seach(hash_table, 10)

    for i in range(10):
        print(hash_table[i])