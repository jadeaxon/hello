def hello():
    with open("hello.txt", "w") as f:
        f.write("Hello, world!\n")


if __name__ == "__main__":
    hello()
