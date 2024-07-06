import pyttsx3
import streamlit as st

# Function to initialize and use text-to-speech engine
def speak_text(audio):
    st.sidebar.write("speaking")
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

# Streamlit app
st.title("Text Input Talk")

# Text input for user name
talk1 = st.text_input("Enter your text:")

# Button to trigger speaking the text input
if st.button("Speak!"):
    st.write("Speaking...")
    speak_text(talk1)

# Initialize session state variables
if 'analysis_result_text' not in st.session_state:
    st.session_state.analysis_result_text = ""

# Display the analysis result
analysis_result = st.empty()
if st.session_state.analysis_result_text:
    analysis_result.write(f"Analysis Result: {st.session_state.analysis_result_text}")

# Sidebar button to speak the analysis result
if st.sidebar.button("Speak Analysis Result"):
    speak_text(st.session_state.analysis_result_text)