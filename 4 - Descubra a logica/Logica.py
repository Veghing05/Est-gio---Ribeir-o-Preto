# Sequência a
a = [1, 3, 5, 7]
proximo_a = a[-1] + 2

# Sequência b
b = [2, 4, 8, 16, 32, 64]
proximo_b = b[-1] * 2

# Sequência c
c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = (int(len(c)) ** 2)

# Sequência d
d = [4, 16, 36, 64]
proximo_d = ((len(d) + 1) * 2) ** 2

# Sequência e
e = [1, 1, 2, 3, 5, 8]
proximo_e = e[-1] + e[-2]

# Sequência f
f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = f[-1] + 1

print(f"Próximo elemento da sequência a: {proximo_a}")
print(f"Próximo elemento da sequência b: {proximo_b}")
print(f"Próximo elemento da sequência c: {proximo_c}")
print(f"Próximo elemento da sequência d: {proximo_d}")
print(f"Próximo elemento da sequência e: {proximo_e}")
print(f"Próximo elemento da sequência f: {proximo_f}")
