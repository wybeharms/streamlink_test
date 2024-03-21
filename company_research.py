import streamlit as st
import anthropic

client = anthropic.Anthropic(
    api_key="ADD_API_KEY",
)

st.title('Company Research')

company = st.text_input('Enter Company Name:')
ticker = st.text_input('Enter Stock Ticker:')
button = st.button('Submit')

if button:
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0.2,
        system=f"You are an excellent investment analyst. I will ask you a question about {company} ({ticker}), a publicly-listed company. Please return a high-level overview of the company like you work at a top notch hedge fund as an analyst",
        messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What is the history of the company and in what industry does it operate? First give me a high-level explanation of the industry dynamics. It is important that you include an analysis of competitive forces using Porter's Five Forces framework when analyzing the industry dynamics and trends. What are key drivers to keep track of for this industry? Next give an overview of the company’s products/services and the company’s business model. Explain who the customers and suppliers are, and how the company distributes its product. Next, I would like you to do a very high-level analysis of the company’s revenue model by doing back-of-envelope calculations. It is particularly important to keep the analysis simple and big picture. First do a top-down approach by estimating the market size and market share. Then also do a bottom-up analysis by estimating the unit economics. It does not matter whether your guess is correct, I care about how you reason your answer. Is the company growing quickly or does it just blob along? Lastly, I would like you to analyze the cost structure. Are the costs mostly fixed or variable? How does this translate into margins?"
                        }
                    ]
                }
            ]
        )
    raw_text = message.content
    answer = raw_text[0].text
    st.write(answer)



