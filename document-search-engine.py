import string
#------------- FUNCTIONS -------------------------------------------------------------------------------------
def create_doc_list():
    """This is a function that opens the document and sorts them into a list, made up of each document
    iterated as a string. """
    my_file = open("ap_docs2.txt", "r")
    file_read = my_file.read()
    my_file.close()
    document_list = file_read.split("<NEW DOCUMENT>")
    del document_list[0]
#    print("Number of documents: ", len(document_list))
    return (document_list)


def create_dict(document_list):
    """This is a function that takes the documents and orders them into a dictionary, with the format as
    word: document number"""
    word_dictionary = {}
    iterator = 1
    document_list = [document.lower() for document in document_list]
    document_list = [document.replace("\n", " ") for document in document_list]
    for c in string.punctuation:
        document_list = [document.replace(c, "") for document in document_list]
    for document in document_list:
        for word in document.split():
            if word not in word_dictionary:
                word_dictionary[word] = {iterator}
            else:
                word_dictionary[word].add(iterator)
        iterator += 1
    return word_dictionary

def search_dictionary(searchwords):
    """This is a function that searches the dictionary using the searchwords"""
    print("searchwords:",searchwords)

    intersection_set = set()
    for i in range(0, len(searchwords)):
        if i == 0:
            intersection_set = document_dictionary[searchwords[i]]
        else:
            intersection_set = intersection_set.intersection(document_dictionary[searchwords[i]])
    print("int_set;", intersection_set)
    return intersection_set

def main_prompt():
    """This is the main prompt of the program. It contains mini functions
    inside it to run the search, printdoc and quit functions"""
    while True:
        inputnum = input("\nWhat would you like to do? Type in the number"
                 "\n1. Search for Documents.\n2. Read Document.\n3. Quit Program\n>")
        if inputnum == '1':
            HowManyWords = int(input("How many words would you like to search for? "))
            searchwords = []
            while True:
                for i in range(HowManyWords):
                    word = input("Enter a word to search: ")
                    searchwords.append(word.lower())
                try:
                    intersection_set = search_dictionary(searchwords)
                except KeyError:
                    print("One word not found.")
                    searchwords = []
                else:
                    break
            print("Documents fitting search:")
            for i in intersection_set:
                print(i, end=' ')
            print("")
            print("")
        elif inputnum == '2':
            while True:
                print("Input is two")
                try:
                    WhatDoc = int(input("What document number would you like to read? Enter a number from 1 to 226"))
                    print(document_list[WhatDoc - 1])
                except ValueError:
                    WhatDoc = input("Wrong input. Please enter a number.")
                except IndexError:
                    WhatDoc = input("Must be a number between 1 and 226. Please input another number")
                else:
                    break

        elif inputnum == '3':
            print("Input is three")
            exit()
        else:
            print("Please enter a number between 1 and 3")


#------------- MAIN CODE -------------------------------------------------------------------------------------

create_doc_list()
document_list = create_doc_list()
create_dict(document_list)
document_dict = dict()
document_dictionary = create_dict(document_list)
main_prompt()