import streamlit as st  # Import the Streamlit library for web application development.
from nltk.chat.util import Chat, reflections  # Import Chat and reflections from NLTK for chatbot functionalities.

# Define chat pairs and reflections.
pairs = [
    [r"\b(hi|hello|hey)\b", ["Hello!", "Hi there!", "Hi! How can I assist you today?"]],
    [r"\bhow are you\b", ["I'm doing well, thanks for asking. How about you?"]],
    [r"i(?: am|'m) (feeling|doing) (.+)", ["Why do you feel %2?", "What made you feel %2?"]],
    [r"i am looking for (a|an) (.+)", ["I can help you find %2. What are the specifications?", "Finding %2, please provide more details."]],
    [r"what can you do\?", ["I can chat with you and remember what you tell me!"]],
    [r"what is your name\?", ["I'm a chatbot created by Streamlit and NLTK."]],
    [r"\bquit\b", ["Goodbye!", "See you later!"]]
]

# Initialize the chat object with pairs and reflections.
chat = Chat(pairs, reflections)

# Define a function to get responses from the chatbot based on user input.
def chatbot_response(user_input):
    response = chat.respond(user_input)  # Use the chat object to respond to the input.
    if not response:  # If no response is found, prompt the user to ask something else.
        response = "I'm not sure how to respond to that. Can you try asking something else?"
    return response

# Streamlit web interface setup.
st.title('Chatbot Demo')  # Set the title of the web page.
st.write('Type "reset" to clear conversation or "quit" to end the session.')  # Instructions for user.

# Initialize session state variables if they haven't been initialized before.
if 'history' not in st.session_state:
    st.session_state.history = []
    st.session_state.feedback_given = False

# Create an input box for user input with placeholder text.
user_input = st.text_input("Talk to the bot:", key="user_input", placeholder="Type your message here...").strip()

# Handling user input.
if user_input.lower() == "reset":
    st.session_state.history.clear()  # Clear the conversation history.
    st.session_state.feedback_given = False  # Reset feedback flag.
    st.success("Chat history reset.")  # Notify user of history reset.
elif user_input.lower() == "quit":
    st.session_state.history.append("Chat ended. Thank you for chatting!")  # Append closing message to history.
    st.success("Session ended. Thank you for using the chatbot!")
else:
    if user_input:
        response = chatbot_response(user_input)  # Get response from chatbot.
        st.session_state.history.append(f"You: {user_input}")  # Append user input to conversation history.
        st.session_state.history.append(f"Bot: {response}")  # Append chatbot response to conversation history.

# Display conversation history in a visually appealing format.
st.markdown("### Conversation History")
for line in st.session_state.history:
    if line.startswith("You:"):
        st.markdown(f"<p style='color: yellow; font-size: 18px;'>{line}</p>", unsafe_allow_html=True)  # Style user lines.
    else:
        st.markdown(f"<p style='color: green; font-size: 18px;'>{line}</p>", unsafe_allow_html=True)  # Style bot lines.

# Apply custom CSS styles to enhance the UI aesthetics and accessibility.
st.markdown("""
<style>
.streamlit-container {
    font-family: 'Arial', sans-serif;  # Apply a universal font style.
}
.stTextInput input {
    color: white;  # Improve text color for better contrast.
    background-color: #f0f0f0;  # Apply a light background to the input boxes.
}
.stButton>button {
    color: white;  # Set button text color to white.
    background-color: blue;  # Set button background to blue.
    padding: 10px 24px;  # Add padding to button for better appearance.
    border-radius: 8px;  # Round the button corners.
}
</style>
""", unsafe_allow_html=True)  # Allow HTML tags for style customization.
