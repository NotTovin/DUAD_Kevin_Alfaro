def align_text(text):
    string_to_list = text.split('-')
    string_to_list.sort()
    list_to_string = '-'.join(string_to_list)
    return list_to_string

def main():
    string_text = 'python-variable-funcion-computadora-monitor'
    aligned_text = align_text(string_text)
    print(aligned_text)

if __name__ == "__main__":
    main()

