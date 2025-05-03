from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator

# loading env variables
load_dotenv()


class OpenAIModel(BaseModel):
    model_name: str
    
    @field_validator('model_name')
    def validate_model_name(cls, v):
        allowed_models = ["gpt-4o-mini", "gpt-4o"]
        if v not in allowed_models:
            raise ValueError(f"Invalid model name: {v}. Allowed models are {allowed_models}")
        return v


class OpenAIIntegration:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        self.client = OpenAI(api_key=api_key)
    
    def openai_search(self, query, model_name="gpt-4o-mini"):
        # Validate model using Pydantic
        model = OpenAIModel(model_name=model_name)
        
        response = self.client.chat.completions.create(
            model=model.model_name,
            messages=[
                {"role": "user", "content": query}
            ]
        )
        return response 

# testing
if __name__ == "__main__":
    openai_integration = OpenAIIntegration()
    response = openai_integration.openai_search("What is the capital of France?", model_name="gpt-4o-mini")
    print(response.choices[0].message.content) 