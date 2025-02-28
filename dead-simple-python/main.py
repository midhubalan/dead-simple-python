from hello_world import lunch_order
from joke import Joke


def main():
    print("Hello from dead-simple-python!")


if __name__ == "__main__":
    main()
    funny = Joke("funny")
    funny.tell()
    Joke("blah").tell()
    print("---")
    lunch_order()
    print("---")
