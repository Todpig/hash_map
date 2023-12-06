import time

hash_table = {}

def collatz(value):
    sequence = [value]
    while value != 1:
        if value % 2 == 0:
            value = value // 2
            sequence.append(value)
        else:
            value = (3 * value) + 1
            sequence.append(value)
    return sequence  
   
def value_grand_sequence(value):
    grand_sequence = 0
    grand_value = 0
    for i in range(1, value + 1):
        sequence = collatz(i)
        if len(sequence) > grand_sequence:
            grand_sequence = len(sequence)
            grand_value = i
    return grand_sequence, grand_value

if __name__ == "__main__":
    number_repeat = int(input("Digite o número de repetições: "))
    
    start_time = time.time()
    grand_sequence, grand_value = value_grand_sequence(number_repeat)
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"O valor {grand_value} possui a maior sequência de {grand_sequence} passos.")
    print(f"Tempo de execução: {elapsed_time} segundos.")
