def compare_word_by_word(original_file_path, repeated_file_path):
    # Read content from original file
    with open(original_file_path, 'r') as original_file:
        original_content = original_file.read()

    # Read content from repeated file
    with open(repeated_file_path, 'r') as repeated_file:
        repeated_content = repeated_file.read()

    # Tokenize content by words
    words1 = original_content.split()
    words2 = repeated_content.split()
    lt=[]
    print("original file length = ",len(words1))
    print("Given Text file length = ",len(words2))
    w1=len(words1)
    w2=len(words2)
    ct=0
    # Initialize a counter for correct words
    correct_count = 0
    print("Matching Words=")
    # Iterate through each word in the first string
    count=0
    for word2 in words2:
        # Find the most similar word in the second string
        match = difflib.get_close_matches(word2, words1, cutoff=1)
        #print(match)
        #print(words1[count])
        # If a similar word is found, increment correct_count
        w1-=1
        w2-=1
        if w1==0 and w2>0:
            w1=len(words1)
            ct+=1
            count=0
        if match and word2==words1[count]:
            print(word2)
            lt.append(word2)
            correct_count += 1
        else:
            print("Not Match=",words1[count])
        count+=1
    return correct_count,lt,len(words1),len(words2),ct+1

def main():
    #original_file_path = input("Enter the path of the original file: ")
    #repeated_file_path = input("Enter the path of the file with repeated content: ")
    original_file_path="C:\\Users\\hp\\Desktop\\dist\\11"
    repeated_file_path="C:\\Users\\hp\\Desktop\\dist\\12"

    correct_count,lt,lw1,lw2,ct = compare_word_by_word(original_file_path, repeated_file_path)
    print("CT=",ct)
    print("length should be = ",lw1*ct)
    print("Length of text = ",lw2)
    print(lt)
    print("Correct words:", correct_count)
    accuracy=(correct_count)/lw2*100
    print(f"Accuracy: {accuracy:.2f}%")
    print("Performance Score = ", (correct_count)/10)

if _name_ == "_main_":
    main()