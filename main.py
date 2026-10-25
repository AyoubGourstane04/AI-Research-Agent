from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import agent_tools



load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

system_prompt = """
You are a research assistant that helps generate research papers.

Answer the user's query accurately.
Use available tools when necessary.
Do not invent sources or claim to have used tools that were not used.
If the question has no definitive answer, explain why.
"""


agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    response_format=ResearchResponse,
    tools=agent_tools
)


query = input("What can I help you research? ")

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": query
        }
    ]
})

structured_response = result["structured_response"]

print(structured_response)



"""
older way : 
"""

# parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """
#             You are a research assistant that will help generate a research paper.
#             Answer the user query and use neccessary tools.
#             Wrap the output in this format and provide no other text\n{format_instructions}
#             """,
#         ),
#         ("placeholder", "{chat_history}"),
#         ("human", "{query}"),
#         ("placeholder", "{agent_scratchpad}"),
#     ]
# ).partial(format_instructions=parser.get_format_instructions()) 

# agent = create_tool_calling_agent(
#     llm=llm,
#     prompt=prompt,
#     tools=[]
# )

# agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
# raw_response = agent_executor.invoke({"query": "What is the capital of canada?"})

# srtuctured_response = parser.parse(raw_response.get("output")[0]["text"])
