from time import sleep

counter_value = 0


def action():
    global counter_value
    with open('/shared/data.txt', 'w') as file:
        counter_value = counter_value + 1
        print(f"The result has been written to result.txt {counter_value}")
        file.write(str(counter_value))


while (True):
    action()
    sleep(4)
