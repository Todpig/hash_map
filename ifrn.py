class Table:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def __str__(self):
        return super().__str__()

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.table[hash_key]

        if bucket is None:
            bucket = []
            self.table[hash_key] = bucket

        for i, keyAndValue in enumerate(bucket):
            keyP, valueP = keyAndValue
            print(keyP, valueP)
            if key == keyP:
                key_exists = True
                break

        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        for i, keyAndValue in enumerate(bucket):
            keyP, valueP = keyAndValue
            if key == keyP:
                return valueP

    def delete(self, key):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, keyAndValue in enumerate(bucket):
            keyP, valueP = keyAndValue
            if key == keyP:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

class User:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return str(self.nome)


if __name__ == "__main__":
    hash_table = Table(10000)
    for i in range(hash_table.size):
        user = User(f'Kalebe-{i}', i)
        hash_table.insert(i, user) 
    
    print(hash_table.search(877))
    hash_table.delete(999)
    print(hash_table.table)