# python-document-search-engine
A command line based document search engine that takes in a list of documents in the form of a text file, splits them into separate articles and allows the user to search via keyword or article number.


def create_doc_list():

The purpose of this function is to open the file, read the file, and append each document to a list as a string. 
I closed the file after opening using my_file.close(). I then created a list, and used file_read to insert the whole file into a list. 
Then I split the documents into list elements.  I did this using the .split method using (“<NEW DOCUMENT>”) to split the file. 
I then deleted the first element of the created list as it was an empty string, due to how the document split. 
The for loops were not iterating over nothing. This then returned my document_list.

  
def create_dict(document_list):

This function is to create the dictionary.
Firstly I tidied up the document_list by using the .lower function and by replacing the newlines in the strings with a space “ ”. Then I stripped each string of its punctuation, using import string, and replacing each punctuation with nothing (“”)
I created an empty dictionary, and then I created an iterator to help me make the dictionary. I then iterated through all the documents, and then through each word in the strings using two for loops and document.split to get at the words. I used a count method (iterator) to count through each document as it came across the words. The word was assigned as the key using dictionary[word]. The iterator was then assigned as the value of the key. I then returned the dictionary. It is to be noted that the value is a set. This is to stop the values getting repeated as words will inevitably be in the same strings multiple times, i.e. “the”

search_dictionary(searchwords):

This function uses sets to find the common documents of the inputted words. I used the range function to iterate through all the searchwords (which are created in a list in the prompt function). I then used set intersection to find the common documents.

  
main_prompt():
  
Firstly I designed the program using a prompt. I went for a command line style where the user inputs a number from 1 to 3 
and this sets off the program in motion. To check the user was inputting the correct type I put the user input into a while True loop. 
Then it iterates through if/elif statements. 
  
1 = Search Words. To search the words, I appended the user input into a list using  the range function. I asked the user to input how many words they wanted to check and added this to the range, and then appended each word to a searchwords list. This also prints the results_set underneath from before. I checked KeyError within a while True loop, and if the user inputted a word that was not in the document I asked them to input it again.

2 = Print Doc. To print the doc, I asked the user to input what document they would like to read, and used this number to get at the list element using the index key, minus 1. I have minused 1 as indexes start at 0, but documents start at 1! It returns the document printed. I checked for user inputted errors using a while True Loop, and checked for index errors and value errors.

3 = exit the program. I did this using exit()
