import easyocr


def text_recognition(file_path, text_file_name= "result.txt"):
    reader = easyocr.Reader(["ru"])#если надо добавить язык написать "en"
    result = reader.readtext(file_path, detail=0)#выведет только результат без координат

    with open(text_file_name, "w") as file:
        for line in result:
            file.write(f"{line} \n")

    return f"Result in {text_file_name} "


def main():
    file_path = input("Enter path file: ")
    #первый кортеж координаты элементов, потом результат, точность
    print(text_recognition(file_path=file_path))


if __name__ == "__main__":
    main()
