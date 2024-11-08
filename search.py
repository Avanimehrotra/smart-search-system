from sentence_transformers import SentenceTransformer, util
import json
from model import load_course_data

# Load the model (you can use any available model from SentenceTransformers library)
model = SentenceTransformer('all-MiniLM-L6-v2')  # Example model

# Load course data from JSON file
course_data = load_course_data()

# Function to search for courses based on the query
def search_courses(query):
    # Convert the query to its embedding
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Create embeddings for course descriptions
    course_embeddings = model.encode([course['description'] for course in course_data], convert_to_tensor=True)

    # Compute cosine similarities between the query and course descriptions
    similarities = util.pytorch_cos_sim(query_embedding, course_embeddings)[0]

    # Get top 5 most similar courses
    top_results = similarities.topk(5)

    # Retrieve the top 5 courses based on similarity score
    results = []
    for score, idx in zip(top_results[0], top_results[1]):
        course = course_data[idx]
        results.append({'title': course['title'], 'description': course['description'], 'url': course['url'], 'score': score.item()})

    return results

# Example usage
if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = search_courses(query)

    print("\nTop 5 matching courses:")
    for idx, result in enumerate(results, 1):
        print(f"{idx}. {result['title']}\n   {result['description']}\n   URL: {result['url']}\n   Score: {result['score']}\n")
