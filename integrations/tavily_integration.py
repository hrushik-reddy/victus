from tavily import TavilyClient
import os 
import json
from dotenv import load_dotenv

load_dotenv()


class TavilyIntegration:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def tavily_search(self, query):
        response = self.tavily_client.search(query)
        return response

    def tavily_with_summarization(self, query):
        response = self.tavily_client.search(query, summarize=True)
        return response


#testing
if __name__ == "__main__":
    tavily_integration = TavilyIntegration()
    response = tavily_integration.tavily_search("What is the capital of France?")
    print(response)
