def main():
    file_path = "input.png"
    filebytes = []
    with open(file_path, "rb") as file:
        data = file.read()
        print(data) 
        filebytes.append(file.read(1))


if __name__ == "__main__":
    main()
