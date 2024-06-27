# Function to filter words from a file and return the top ten most frequent words

def filter_words():

    #Open the file 'filter_file.txt' in read mode
    with open('filter_file.txt','r') as file:

        # Read the contents of the file and split the text into words
        text = file.read().split()

    
        filter_text = {}

    
        for i in text:

        
            if i.isalpha():

                # If the word is alphabetic, add it to the filter_text dictionary
                # If the word is already present, increment its frequency count
                filter_text.setdefault(i,0)
                filter_text[i] += 1
            
        # Sort the words based on their frequencies in descending order
        sorted_words = sorted(filter_text.items(),key=lambda x: x[1],reverse=True)
        
        # Select the top ten most frequent words
        top_ten = sorted_words[:10]

        
        return top_ten


top_words = filter_words()

# Iterate through the top ten most frequent words and print each word along with its frequency
for k,w in top_words:
    print(k,w)









