def count_letter_a(input_string):
   
    lower_string = input_string.lower()
    
    
    count = lower_string.count('a')
    
    return count


input_string = input("Informe uma string para verificar a ocorrência da letra 'a': ")


count = count_letter_a(input_string)


if count > 0:
    print(f"A letra 'a' aparece {count} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
