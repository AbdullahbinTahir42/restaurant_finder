from secret_key import GEMINI_API_KEY
import os
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.6,
    api_key=SecretStr(GEMINI_API_KEY)
)


def restaurant_finder(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a {cuisine} restaurant. Suggest a name."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="List some popular {restaurant_name} dishes. In a comma-separated list."
    )
    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )
    response = chain({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    cuisine = "Pakistani"
    result = restaurant_finder(cuisine)
    print(result)
