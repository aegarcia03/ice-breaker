from dotenv import load_dotenv
import os
from typing import Tuple
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from output_parsers import summary_parser, Summary
from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name: str) -> tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock = True)

    summary_template = """
       given the LinkedIn information {information} about a person I want you to create:
       1. A short Summary
       2. Two interesting facts about them
       \n{format_instructions}
       """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    res =  chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()
    print("Welcome to Ice Breaker")
    ice_break_with(name="Angela Garcia")

