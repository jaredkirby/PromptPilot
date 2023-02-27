import openai
import streamlit as st
from streamlit_chat import message
import time
import webbrowser
# import random


st.set_page_config(page_icon="🚀", page_title="PromptPilot")

st.image(
    "https://i.imgur.com/WAWX9t4.jpeg",
    width=100,
)

st.title("PromptPilot")
st.subheader("Effortlessly create effective LLM prompts")

# Sidebar
st.sidebar.title("About")
st.sidebar.markdown('''
**PromptPilot** is a powerful software tool that helps you generate the perfect GPT3 prompt every time. Using natural language processing and machine learning, PromptPilot analyzes your input sentence and generates a refined and targeted prompt based on your specific needs and goals. 

If you would like to help us improve this application, please click the button below.
''')

if st.sidebar.button("Give Feedback"):
    webbrowser.open_new_tab(
        "https://docs.google.com/forms/d/e/1FAIpQLSeAY1nRJFEple8TgpWl3gQz-HjI6QUzKyoBaehQR-PcT-m9hQ/viewform?usp=sf_link")

st.sidebar.markdown('''
Our goal is to make our AI system more natural and safe to interact with. Your feedback will help us improve.
''')
st.sidebar.markdown("---")

st.sidebar.header("Example Questions")
st.sidebar.markdown('''
Not sure what to ask?  Here are some example questions you can try out:
- "I need help writing an essay for my college application."
''')
st.sidebar.markdown("---")

st.sidebar.markdown(
    "Made by [Jared Kirby](https://www.linkedin.com/in/jared-kirby/)")


# Initialize variables.
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

if "history" not in st.session_state:
    st.session_state["history"] = {}

# Get the openAI API key
openai.api_key = st.secrets['openai_api_key']


def get_text() -> str:
    # Get user input
    user_input = st.text_input(
        "Ask Anything: ", "Hello, who are you?", key="input")
    return user_input


user_input = get_text()

# If user input exists, query the API and update the session variables.
if user_input:

    # Query the API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=(f"You are an expert GPT-3 prompt designer named Pilot. You read the user's desired output from GPT-3 as User INPUT, written in natural language. You will analyze the user's input and ask follow-up questions if needed, in order to understand the user's intent. With that knowledge, you will create a prompt designed to maximize the user's intended use of GPT-3. Make sure to include all the relevant details to ensure the best possible outcome.\n\nExample INPUT and RESPONSE:\nExample #1\nUser: I need help writing an essay for my English class.\nPilot: If available, please provide an outline of the subject of the essay, the length of the essay, any key topics that need to be discussed, and any other relevant information that would help me generate a high-quality prompt for ChatGPT or GPT-3.\nUser: The essay is about the tech impact of Nicola Tesla. It needs to be 3 paragraphs long.\nPilot: Here is your optimized prompt: \"Write an essay about the tech impact of Nikola Tesla, approximately three paragraphs long. Include the contributions and innovations of Tesla, how his work has had an impact on technology today, and how it will continue to shape the future of technology.\"\nExample #2\nUser: I need help writing blog posts for a golf website.\nPilot: Here is your optimized prompt: \"Write one or more blog posts about golf for a website. Include topics such as golf tips and tricks, the history of golf, golf equipment and apparel, golf courses, golfers and their stories, and the latest trends in golf. Also, provide information on how to get started in golf, and address any questions that beginners may have.\" If this prompt inspired you to focus on a specific topic, let me know what it is for a new optimized prompt.\nUser: Focus on golfers and their stores.\nPilot: Here is your optimized prompt: \"Write one or more blog posts about golfers and their stories for a website. Include topics such as the background of the golfer, accomplishments, wins, and losses, their journey, and any advice they have for aspiring golfers. Also, provide information on how to get started in golf, and address any questions that beginners may have."
                f"User: {user_input}\n"
                f"Pilot:"),
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["User: "]
    )
    output = response.choices[0].text

    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(output)

if st.session_state['generated']:

    # Display the chat messages.
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        time.sleep(1)
        message(st.session_state["past"][i],
                is_user=True, key=str(i) + "_user")
