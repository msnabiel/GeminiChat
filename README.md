
# GeminiChat

GeminiChat is a Chainlit application that integrates with Google's Gemini model to provide real-time text generation capabilities. This app uses Chainlit for the chat interface and Google's Generative AI (Gemini) for generating responses.

## Features

- Real-time text generation using the Gemini model.
- Intermediate response to indicate that the request is being processed.
- Error handling for model response issues.

## Prerequisites

1. **Python 3.8+**: Ensure you have Python 3.8 or higher installed.
2. **Chainlit**: Install Chainlit using pip.
3. **Google Generative AI**: Obtain a Google API key for accessing Gemini.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/msnabiel/GeminiChat.git
   cd GeminiChat
   ```

2. **Install Dependencies**:
   ```bash
   pip install chainlit google-generativeai
   ```

3. **Set Up Environment Variables**:
   - Obtain your Google API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Set the environment variable `GOOGLE_API_KEY` with your API key:
     ```bash
     export GOOGLE_API_KEY="your-google-api-key"
     ```

## Configuration

- **Google Generative AI**: The app uses the `gemini-1.5-flash` model from Google's Generative AI. Ensure you have the correct API key and model name.

## Usage

1. **Run the Application**:
   ```bash
   chainlit run app.py
   ```

2. **Interact with the App**:
   - Open the Chainlit interface in your browser at `http://localhost:8000`.
   - Send messages to receive generated responses from the Gemini model.

## Code Explanation

- **Imports**: Import necessary libraries for Chainlit, Google Generative AI, and asynchronous operations.
- **Model Initialization**: Configure and initialize the Gemini model using the API key.
- **Response Generator**: Define an asynchronous function to generate responses from the model.
- **Main Function**: Handle incoming messages, send an intermediate response, generate the final answer, and update the intermediate response with the final result.

## Example

Here is a brief example of how the app functions:

1. User sends a message.
2. The app responds with "Processing your request...".
3. The app generates a response using the Gemini model.
4. The intermediate response is updated with the final answer.

## Error Handling

If the model fails to generate a response, the app will return an error message indicating the issue.

## License

This project is licensed under the [MIT License](LICENSE).

---
