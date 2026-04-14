import re

def load_dataset(file_path):
    """Load dataset from file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print("Dataset file not found!")
        return ""

def preprocess_text(text):
    """Convert text to lowercase and remove extra spaces"""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text

def search_dataset(query, dataset):
    """Search relevant sentences from dataset"""
    results = []
    
    sentences = dataset.split(".")
    
    for sentence in sentences:
        if query in sentence:
            results.append(sentence.strip())
    
    return results

def chatbot():
    print("="*50)
    print(" AI RAG Chatbot using Dataset 🤖 ")
    print("="*50)
    
    dataset = load_dataset("data.txt")
    dataset = preprocess_text(dataset)
    
    if not dataset:
        return
    
    while True:
        print("\n----------------------------------")
        query = input("Ask your question (type 'exit' to quit): ").lower()
        
        if query == "exit":
            print("Goodbye! 👋")
            break
        
        results = search_dataset(query, dataset)
        
        if results:
            print("\n✅ Relevant Answers:")
            for i, res in enumerate(results[:3], 1):
                print(f"{i}. {res}")
        else:
            print("\n❌ No exact match found.")
            print("👉 Try asking related keywords.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
