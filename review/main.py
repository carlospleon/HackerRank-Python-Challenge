# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def Par(x):
    r = x%2
    if r == 1:
        print("Weird")
    if x >= 2 and x <= 5 and r == 0:
        print("Not Weird")
    if x >= 6 and x <= 20 and r == 0:
        print("Weird")
    if x > 20 and r == 0:
        print("Not Weird")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Julio')

    n = int(input("Numero del 1 al 100"))
    Par(n)



#numero = int(input("Escriba un número positivo: "))
#if numero < 0:
#    print("¡Le he dicho que escriba un número positivo!")
#print(f"Ha escrito el número {numero}")