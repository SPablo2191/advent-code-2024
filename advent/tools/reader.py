def read_output(fileName):
    with open(fileName, "r") as file:
        return file.readlines()


def read_output_full(fileName):
    with open(fileName, "r") as file:
        return file.read()
