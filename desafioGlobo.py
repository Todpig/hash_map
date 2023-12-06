hash_table = {}

def hash_function(value, step):
    return hash((value, step))

def collatz(value):
    sequence = [value]

    step = 0
    while value != 1:
        key = hash_function(value, step)

        if key in hash_table:
            value = hash_table[key]
        else:
            if value % 2 == 0:
                value = value // 2
            else:
                value = (3 * value) + 1
            
            hash_table[key] = value

        step += 1
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
    grand_sequence, grand_value = value_grand_sequence(4)
    print(f"O valor {grand_value} possui a maior sequência de {grand_sequence} passos.")
