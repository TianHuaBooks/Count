"""Count words."""
import re

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    # Convert to lowercase
    text2 = text.lower()
    
    # Split text into tokens (words), leaving out punctuation
    # Use regex to split on non-alphanumeric characters '\w'
    matchObjs = re.findall(r'[\w]+', text2)
    
    # Aggregate word counts using a dictionary
    for obj in matchObjs:
        if obj in counts:
            counts[obj] += 1 #add one into an existing entry
        else:
            counts[obj] = 1 #set entry to count of one
    
    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()

