from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_course_data():
    with open('data/course_data.json', 'r') as f:
        return json.load(f)

def generate_embeddings(course_data):
    return [model.encode(course['description']) for course in course_data]

# Example: Load data and generate embeddings
course_data = load_course_data()
course_embeddings = generate_embeddings(course_data)
