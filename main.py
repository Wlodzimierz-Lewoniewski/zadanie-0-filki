import re

from collections import defaultdict

def process_input():
    """
    Przetwarza dane wejściowe przy użyciu input() i zwraca oczyszczone dokumenty oraz zapytania.
    """
   
    n = int(input().strip())
  
    documents = [re.sub(r'[^\w\s]', '', input().strip()).lower() for _ in range(n)]
    
    
    m = int(input().strip())
    
    queries = [re.sub(r'[^\w\s]', '', input().strip()).lower() for _ in range(m)]
    
    return documents, queries

def process_documents_and_queries(documents, queries):
    """
    Przetwarza dokumenty i zapytania.
    Zwraca listę list z indeksami dokumentów, które zawierają dane słowa z zapytań.
    """
    
    word_to_docs = defaultdict(list)
    for doc_index, doc in enumerate(documents):
        word_count = {}
        for word in doc.split():
            word_count[word] = word_count.get(word, 0) + 1
        for word, count in word_count.items():
            word_to_docs[word].append((doc_index, count))

    
    result = [
        [doc_index for doc_index, _ in sorted(word_to_docs.get(query, []), key=lambda x: (-x[1], x[0]))]
        for query in queries
    ]
    
    return result

def main():
    documents, queries = process_input()
    results = process_documents_and_queries(documents, queries)
    
    # Drukowanie wyników w odpowiednim formacie
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
