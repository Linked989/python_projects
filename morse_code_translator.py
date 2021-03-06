#Morse Code
#https://www.colourbox.com/vector/morse-code-letters-and-numbers-vector-27996080
morse_dict = {'a':'.-', 'b':'-...', 'c':'-.-.','d':'-..','e':'.','f':'..-.',
              'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
              'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
              's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
              'y':'-.--','z':'--..',}
while True:
    print("\n1. Encode to Morse Code")
    print("2. Decode from Morse Code")
    print("3. Press 'q' to exit")
    print()
    menu = input("Select 1 or 2: ")

    #Encode text to morse code
    if menu == '1':
        morse_encode = input("Encode text: ")
        morse_spaced = (' '.join(morse_encode.lower()))
        for key,value in morse_dict.items():
            for letter in morse_spaced:
                if letter in key:
                    morse_spaced = morse_spaced.replace(letter, value)
        print("Result: " + morse_spaced)

    #Decode morse code to text
    elif menu == '2':
        morse_decode = input('Input: ')
        word_len = morse_decode.split()
        for word in word_len:
            for key,value in morse_dict.items():
                if word == value:
                    word = word.replace(word, key)
                    print("Result: " + word.upper(),end='')
                    print()
    else:
        break
