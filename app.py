import chainlit as cl
import google.generativeai as genai
import os
import asyncio

# Initialize the Gemini model
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate a response using Gemini
async def response_generator(text):
    try:
        # Generate text with the provided model
        response = model.generate_content(text)
        if response and hasattr(response, 'text'):
            return response.text  # Access the generated text correctly
        return "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Define what happens on each user message
@cl.on_message  # Called when the user sends a message
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response, then the final response from the generator.
    """
    # Send an intermediate message to indicate processing
    intermediate_response = await cl.Message(content="Processing your request...").send()

    # Generate the final answer directly
    final_answer = await response_generator(message.content)
    await asyncio.sleep(2)
    # Update the intermediate message with the final content
    intermediate_response.content = final_answer
    await intermediate_response.update()
