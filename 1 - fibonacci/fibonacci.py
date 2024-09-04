def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_in_fibonacci(number):
    if number < 0:
        return False
    sequence = fibonacci_sequence(number)
    return number in sequence


num = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))


if is_in_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
