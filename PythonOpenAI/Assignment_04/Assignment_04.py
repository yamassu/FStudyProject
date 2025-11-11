from openai import AzureOpenAI  
import time  
from tenacity import retry, wait_random_exponential, stop_after_attempt, 
retry_if_exception_type  
from openai import RateLimitError, APIError  
import os  
os.environ["AZURE_OPENAI_ENDPOINT"] = ""  
os.environ["AZURE_OPENAI_API_KEY"] = "" 
os.environ["AZURE_DEPLOYMENT_NAME"]= "GPT-4o-mini" 
# Step 1: Set your Azure OpenAI API key   
client = AzureOpenAI(   
api_version="2024-07-01-preview",   
azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),   
api_key=os.getenv("AZURE_OPENAI_API_KEY"),   
)  
# Step 2: Define your function schema for function calling  
functions = [  
{  
"name": "generate_itinerary",  
"description": "Generate a travel itinerary for a given destination and 
duration.",  
"parameters": {  
"type": "object",  
"properties": {  
                "destination": {"type": "string", "description": "Travel 
destination city or country"},  
                "days": {"type": "integer", "description": "Number of days to 
plan for"}  
            },  
            "required": ["destination", "days"],  
        },  
    }  
]  
  
  
  
# Step 3: Define a retry decorator for rate limits and transient errors  
@retry(  
    retry=retry_if_exception_type((RateLimitError, APIError)),  
    wait=wait_random_exponential(min=1, max=10),  
    stop=stop_after_attempt(5),  
    reraise=True  
)  
  
def call_openai_function(prompt, destination, days): 
    response = client.chat.completions.create(  
        model=os.getenv("AZURE_DEPLOYMENT_NAME"),  
        messages=[  
            {"role": "user", "content": prompt}  
        ],  
        functions=functions,  
        function_call={  
            "name": "generate_itinerary",  
            "arguments": f'{{"destination": "{destination}", "days": {days}}}'  
        }  
    )  
    return response  
  
  
  
# Step 4: Batch processing function  
def batch_process(inputs):  
    results = []  
    for input_data in inputs:  
        try:  
            prompt = input_data["prompt"]  
            destination = input_data["destination"]  
            days = input_data["days"]  
            res = call_openai_function(prompt, destination, days)  
            results.append(res)  
            time.sleep(1)  # Optional: prevent hitting rate limits aggressively  
        except Exception as e:  
            print(f"Error processing {destination}: {e}")  
            results.append(None)  
    return results  
  
# Step 5: Example batch inputs  
  
batch_inputs = [  
{"prompt": "Plan a travel itinerary.", "destination": "Paris", "days": 3},  
{"prompt": "Plan a travel itinerary.", "destination": "Tokyo", "days": 5},  
{"prompt": "Plan a travel itinerary.", "destination": "New York", "days": 
4},  
]  
# Step 6: Run batch processing and display results  
if __name__ == "__main__":  
outputs = batch_process(batch_inputs)  
for idx, output in enumerate(outputs):  
print(f"Result for {batch_inputs[idx]['destination']}:")  
if output:  
print(output)  
else:  
print("No result due to error or retry failure.")  
print("-" * 40)