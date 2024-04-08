# the path to the book to be used
book_path = 'books/frankenstein.txt'

# counts the words in provided string
def count_words (str):
    words = str.split()
    count = len(words)
    return count

# counts how many times each character appears in string
def count_chars (str):
    str = str.lower()
    counts = {}
    
    for char in str:
        if not char.isalpha():
            continue
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
            
    return counts

# prints a report on the provided string
def print_report (text):
    print(f'--- Begin report of {book_path} ---')
    print(f'{count_words(text)} words found in the document\n\n')
    
    chars = count_chars(text)
    counts = []
    for char in chars:
        counts.append({'char': char, 'num': chars[char]})    
        
    def sort_key (dict):
        return dict['num']
    
    counts.sort(reverse=True, key=sort_key)
    
    for count in counts:
        char = count['char']
        num = count['num']
        print(f'The \'{char}\' character was found {num} times')
    
    print('--- End report ---')

# main method to be run
def main ():
    # opens book path
    with open(book_path) as f:
        file_contents = f.read()

        # prints a report of the opened book
        print_report(file_contents)


main()