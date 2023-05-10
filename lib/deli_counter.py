def line(deli):
    if len(deli) == 0:
        print("The line is currently empty.")
    else:
        queue = ""
        for p in deli:
            queue += f"{deli.index(p)+1}. {p} "
        print(f"The line is currently: {queue.strip()}")


def take_a_number(deli, name):
    deli.append(name)
    print(f"Welcome, {name}. You are number {len(deli)} in line.")


def now_serving(deli):
    if len(deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {deli[0]}.")
        del deli[0]
