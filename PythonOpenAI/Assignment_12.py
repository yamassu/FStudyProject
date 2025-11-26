# Assignment_12.py

# Required installations:
# pip install langchain-openai pillow requests pydantic

import os
import base64
import requests
from PIL import Image
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

# --- Azure OpenAI Config ---
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_DEPLOYMENT_NAME"] = "GPT-4o-mini"

# --- Setup LLM ---
llm = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_DEPLOYMENT_NAME"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2024-02-15-preview",
)

# --- Output Schema ---
class WeatherResponse(BaseModel):
    accuracy: float = Field(description="The accuracy of the result")
    result: str = Field(description="The result of the classification")

llm_with_structured_output = llm.with_structured_output(WeatherResponse)

# --- Sample image URLs ---
image_urls = [
    "https://images.pexels.com/photos/53594/blue-clouds-day-fluffy-53594.jpeg",
    "https://images.pexels.com/photos/158163/clouds-cloudporn-weather-158163.jpeg",
    "https://images.pexels.com/photos/110874/pexels-photo-110874.jpeg"
]

# --- Prompt Template ---
system_prompt = """Based on the satellite image provided, classify the scene as either:
'Clear' (no clouds) or 'Cloudy' (with clouds).
Respond with only one word: either 'Clear' or 'Cloudy' and Accuracy. Do not provide explanations."""

user_prompt_text = "Classify the scene as either: 'Clear' or 'Cloudy' and Accuracy."

# --- Process each image ---
for image_url in image_urls:
    try:
        response = requests.get(image_url)
        image_bytes = response.content
        image_data_base64 = base64.b64encode(image_bytes).decode("utf-8")

        message = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": user_prompt_text},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data_base64}"}}
            ]}
        ]

        result = llm_with_structured_output.invoke(message)
        print(f"Image URL: {image_url}")
        print(f"Prediction: {result.result}")
        print(f"Accuracy: {result.accuracy}%\n")

    except Exception as e:
        print(f"Error processing image {image_url}: {e}")
