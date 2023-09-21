import datetime


def perf(f):
    def monitor(*args, **kwargs):
        s = datetime.datetime.now()
        r = f(*args, **kwargs).title()
        e = datetime.datetime.now()
        return f"{r} ({e.microsecond - s.microsecond})"

    return monitor


actions = {
    "boire": lambda: perf(lambda: "Cheers")(),
    "manger": lambda: perf(lambda: "Miam")(),
    "dormir": lambda: perf(lambda: "zzzZZZzzz")()
}



@perf
def start():
    while True:
        command = input("Que faire ? ").lower()

        if len(command) == 0 or command == "rien":
            break

        print(actions.get(command, lambda: "Je ne connais pas cette action")())

    return "A une prochaine fois"


if __name__ == '__main__':
    start()
