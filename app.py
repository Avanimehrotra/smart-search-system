import gradio as gr
from search import search_courses  # Import the search function from search.py

# Define a Gradio interface with a more interactive and dynamic UI
def gradio_interface(query):
    results = search_courses(query)

    # Debugging: Print the structure of the results for inspection
    print("Search Results:", results)

    # Create HTML content to display the results as cards with thumbnails
    formatted_results = ""
    for result in results:
        # Get thumbnail URL or fallback to a placeholder image if not available
        thumbnail_url = result.get('thumbnail', None)
        if not thumbnail_url:
            thumbnail_url = "https://via.placeholder.com/100"  # Fallback to a placeholder image if no thumbnail is found
        
        # Debugging: Print the thumbnail URL to check if it's correct
        print(f"Thumbnail URL: {thumbnail_url}")

        # Embed the thumbnail in the card layout
        formatted_results += f"""
        <div style="border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 8px; display: flex; align-items: center;">
            <img src="{thumbnail_url}" alt="Thumbnail" style="width: 100px; height: 100px; margin-right: 15px; border-radius: 8px;">
            <div>
                <h3>{result['title']}</h3>
                <p>{result['description']}</p>
                <p><strong>Score:</strong> {result['score']}</p>
                <a href="{result['url']}" target="_blank" style="color: blue;">Visit Course</a>
            </div>
        </div>
        """
    
    return formatted_results  # Return the formatted HTML content for the results

# Create the Gradio interface
interface = gr.Interface(
    fn=gradio_interface,  # Function to call when the user submits a query
    inputs=gr.Textbox(label="Enter Search Query", placeholder="Enter course topic or keyword", lines=2),
    outputs=gr.HTML(),  # Display results as HTML
    allow_flagging="never",  # Disable flagging
    examples=[  # Add example queries to make it more user-friendly
        ["Machine Learning"],
        ["Data Science"],
    ]
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch(share=True)  # The `share=True` parameter allows public sharing
