import math

def f(x):
    """
    Função a ser integrada: x * exp(2x)
    """
    return x * math.exp(2 * x)

def trapezoidal_rule(f, a, b, n):
    """
    Implementação da regra do trapézio para calcular a integral de uma função.

    Args:
        f: Função a ser integrada.
        a: Limite inferior do intervalo.
        b: Limite superior do intervalo.
        n: Número de subintervalos.

    Returns:
        Integral aproximada da função no intervalo [a, b].
    """
    h = (b - a) / n  # Tamanho do subintervalo
    integral = 0.5 * (f(a) + f(b))  # Primeiro e último termo da soma

    for i in range(1, n):
        x = a + i * h  # Pontos intermediários
        integral += f(x)

    integral *= h  # Multiplica pela largura do subintervalo

    return integral

# Valores do intervalo e número de subintervalos
a = 2
b = 3
n = 4

# Calculando a integral usando a regra do trapézio
integral = trapezoidal_rule(f, a, b, n)

print(f"A integral de x * exp(2x)dx no intervalo de 2 a 3 é aproximadamente: {integral}")
