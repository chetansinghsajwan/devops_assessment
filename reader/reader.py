from time import sleep

try:
    print("WELCOME TO COUNTER READER")
    old = 0
    while (True):
        with open('/shared/data.txt', 'r') as file:
            new = file.read()
            if old != new:
                old = new
                print(f"counter updated : {old}")
        sleep(2)
except Exception as ex:
    print(ex)
