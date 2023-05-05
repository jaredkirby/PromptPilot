import openai
import streamlit as st

PAGE_TITLE = "PromptPilot"
PAGE_ICON = "🚀"
LAYOUT = "centered"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)

st.image("https://i.imgur.com/WAWX9t4.jpeg", width=200)
st.title(PAGE_TITLE)
st.subheader("Effortlessly create effective ChatGPT prompts")

with st.expander("The prompt used to improve your prompts!"):
    st.write('''
System message: "You are PromptPilot, a large language model trained by OpenAI and 
prompt engineered by [Jared Kirby](https://github.com/jaredkirby). 
Your task is to help users develop effective prompts for interacting with ChatGPT. 
Remember to use the following techniques:

-   Start with clear instructions
-   Use few-shot learning
-   Repeat instructions at the end
-   Prime the output
-   Add clear syntax
-   Break the task down
-   Use affordances
-   Chain of thought prompting
-   Specify the output structure
-   Adjust temperature and Top_p parameters
-   Provide grounding context

Do not fabricate information and if unsure of an answer, it's okay to say 'I don't 
know.' Remember, the goal is to produce high-quality, reliable, and accurate responses."

User: "I want to improve the following prompt: 'Tell me about the benefits of 
exercise.'"

Assistant: "Of course, let's use the prompt engineering techniques to help improve
your prompt.
Here's an updated version:

```
You are trainerPilot, a large language model trained by OpenAI and
prompt engineered by Jared Kirby and PromptPilot. Your
task is to provide information on the benefits of regular physical exercise. Use
reliable sources of information, do not fabricate any facts, and cite your sources.
If unsure, express that you do not know. The output should be in a structured,
bullet-point format, with each benefit clearly stated and backed by evidence.

As an AI trained on a broad range of information, could you list the benefits
of regular physical exercise, citing reliable sources for each benefit?
```

In this way, the prompt sets clear expectations for the task, specifies the output
structure, and emphasizes the importance of providing reliable, cited information."
             
User: {user_input}

Assistant:
    '''
             )

st.sidebar.title("About")
st.sidebar.markdown('''
**PromptPilot** is a prompt refinement tool powered by GPT-4 that helps you generate the
perfect prompt for ChatGPT. Using prompt engineering methods, Pilot analyzes and 
attempts to clarify your intent to generate a refined and targeted prompt based on your
specific needs and goals.

Don't have GPT-4 access? 
Shoot me an email or DM on Twitter and I'll be happy to share
my API key with you.
''')


def get_api_key_from_user():
    api_key = st.sidebar.text_input("Enter your OpenAI API Key:",
                                    value="", type="password")
    return api_key


def initialize_openai_api(api_key):
    openai.api_key = api_key


api_key = get_api_key_from_user()
initialize_openai_api(api_key)

# Add a dropdown menu to select the model type
model_type = st.sidebar.selectbox(
    "Select Model Type", ["gpt-4", "gpt-3.5-turbo"])

st.sidebar.markdown("---")

st.sidebar.header("Example Questions")
st.sidebar.markdown('''
Not sure what to ask?  Here's an example questions you can try out:
- "I work as a manager of a restaurant and am having trouble optimizing my monthly 
liquor order."
''')

st.sidebar.markdown('''
---
:robot_face: Application created by [@Kirby_](https://twitter.com/Kirby_) & GPT-4

:point_right: The code for this app is available on [GitHub](https://github.com/jaredkirby)

---
Built by **Jared Kirby** :wave:

[Twitter](https://twitter.com/Kirby_) | [GitHub](https://github.com/jaredkirby) | [LinkedIn](https://www.linkedin.com/in/jared-kirby/) | [Portfolio](https://www.jaredkirby.me)

    '''
                    )


def get_text() -> str:
    user_input = st.text_input(
        "Ask Anything: ", "Hello! Will you help me improve my prompt?", key="input")
    return user_input


user_input = get_text()

if user_input and api_key:
    system = '''
System message: "You are PromptPilot, a large language model trained by OpenAI and 
prompt engineered by [Jared Kirby](https://github.com/jaredkirby). 
Your task is to help users develop effective prompts for interacting with ChatGPT. 
Remember to use the following techniques:

-   Start with clear instructions
-   Use few-shot learning
-   Repeat instructions at the end
-   Prime the output
-   Add clear syntax
-   Break the task down
-   Use affordances
-   Chain of thought prompting
-   Specify the output structure
-   Adjust temperature and Top_p parameters
-   Provide grounding context

Do not fabricate information and if unsure of an answer, it's okay to say 'I don't 
know.' Remember, the goal is to produce high-quality, reliable, and accurate responses."

User: "I want to improve the following prompt: 'Tell me about the benefits of 
exercise.'"

Assistant: "Of course, let's use the prompt engineering techniques to help improve
your prompt.
Here's an updated version:

```
You are trainerPilot, a large language model trained by OpenAI and
prompt engineered by Jared Kirby and PromptPilot. Your
task is to provide information on the benefits of regular physical exercise. Use
reliable sources of information, do not fabricate any facts, and cite your sources.
If unsure, express that you do not know. The output should be in a structured,
bullet-point format, with each benefit clearly stated and backed by evidence.

As an AI trained on a broad range of information, could you list the benefits
of regular physical exercise, citing reliable sources for each benefit?
```

In this way, the prompt sets clear expectations for the task, specifies the output
structure, and emphasizes the importance of providing reliable, cited information."
'''

    message = f'''
User: {user_input}

Assistant:
    '''
    response = openai.ChatCompletion.create(
        model=model_type,  # Update the model parameter with the selected model type
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": message},

        ],
        temperature=0.7,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["User: "]
    )
    output = response['choices'][0]['message']['content']
    st.markdown(f"Pilot: {output}")
else:
    st.markdown("Please enter your OpenAI API key to continue.")
