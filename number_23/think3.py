"""
Сколько разных чисел может быть получено из числа 1 с помощью 
программ, состоящих из 9 команд?
"""
from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def f(x, y):
    if y == 9:
        return 1
    return f(x + 1, y + 1) + f(x + 5, y + 1) + f(x * 3, y + 1)

def main():
    print(f(1, 0))
    vs.make_animation("FIB1.gif", delay=2)

# 19683

if __name__ == "__main__":
    main()