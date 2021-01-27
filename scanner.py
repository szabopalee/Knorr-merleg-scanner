with open("/dev/hidraw0", "r") as file:      # meg kell nezni melyik hidraw-t kapja, lehet hogy nem a 0-t
        while True:
                data = ""
                while True:
                        char = file.read(1)
                        if char == "\n":
                                break

                        x = ord(char)
                        if 48 < x < 90:
                                data += char

                print (data)