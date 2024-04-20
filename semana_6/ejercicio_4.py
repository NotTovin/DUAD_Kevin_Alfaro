def reverse_string(text):
    text = text[::-1]
    return text

def main():
    text = 'Hola mundo'
    backwards_string = reverse_string(text)
    print(backwards_string)

if __name__ == "__main__":
    main()