from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
from dotenv import load_dotenv
from os import getenv, environ

load_dotenv()

df1 = pd.read_csv("./job_1.csv")
df1.fillna(0, inplace=True)
df2 = pd.read_csv("./job_2.csv")
df2.fillna(0, inplace=True)

# df.info()
# df.head()
agent = create_pandas_dataframe_agent(
    OpenAI(temperature=0, model_name="text-davinci-003"), [df1, df2], verbose=True
)


def getAgentResponse(question="", user=""):
    # text-davinci-003
    # "qué trabajos requieren skills en ventas"
    response = agent.run(question)
    print(f"{user} --> results <getAgentResponse> : ", response)
    return response


if __name__ == "__main__":
    getAgentResponse(question="qué trabajos requieren skills en ventas", user="Cris")
