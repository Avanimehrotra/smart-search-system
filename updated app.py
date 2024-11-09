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
                <a href="{result['url']}" target="_blank" style="color: red;">Visit Course</a>  <!-- Change color to red -->
            </div>
        </div>
        """
    
    return formatted_results  # Return the formatted HTML content for the results

# Create the Gradio interface using Blocks
with gr.Blocks() as interface:
    # Add the logo image independently
    gr.Image("/Users/avanimehrotra/Library/Mobile Documents/com~apple~CloudDocs/Desktop/SUBJECTS/Projects/projectsjune/smart_search_tool/assets/logo copy.png", label="Logo", type="filepath")  # Display the logo above the input bar
    
    # Add the title beside the logo
    gr.HTML("""
        <h1 style="font-size: 24px; font-style: italic; text-align: center; margin: 10px 0;">Smart Search Tool</h1>
    """)  # Italics and larger font for the title
    
    # Add the input box with placeholder and lines
    query_input = gr.Textbox(label="Enter Search Query (for free courses)", placeholder="Enter course topic or keyword example Python", lines=2)  # Removed examples
    
    # Output area for results
    output_area = gr.HTML()  # Display results as HTML
    
    # Button to trigger the search
    search_button = gr.Button("Search")
    
    # Button to clear the input and output
    clear_button = gr.Button("Clear")
    
    # Define the action for the search button
    search_button.click(gradio_interface, inputs=query_input, outputs=output_area)

    # Define the action for the clear button
    clear_button.click(lambda: ("", ""), inputs=None, outputs=[query_input, output_area])  # Clear both input and output


# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch(share=True)  # The `share=True` parameter allows public sharing
