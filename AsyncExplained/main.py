import time

def my_func1():
    print("1.fonk başlıyor")
    time.sleep(5)
    print("1.fonk bitti ")
    return 5

def my_func2():
    print("2.fonk başlıyor")
    time.sleep(5)
    print("2.fonk bitti ")
    return 10

if __name__ == "__main__":
    x = my_func1()
    y = my_func2()

    print(f"my func 1'in çalışması sonucu x'in degeri {x}")
    print(f"my func 2'in çalışması sonucu y'in degeri {y}")
