def main():
    file_path = "example.png"
    with open(file_path, "rb") as file:
        data = file.read()
        print(data) 

if __name__ == "__main__":
    main()