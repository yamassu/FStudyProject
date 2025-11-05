from openai import AzureOpenAI 
# Step 1: Mock Input Data 
task_descriptions = [ 
"Install the battery module in the rear compartment, connect to the highvoltage harness, and verify torque on fasteners.", 
"Calibrate the ADAS (Advanced Driver Assistance Systems) radar sensors on the front bumper using factory alignment targets.", 
"Apply anti-corrosion sealant to all exposed welds on the door panels before painting.", 
"Perform leak test on coolant system after radiator installation. Record pressure readings and verify against specifications.", 
"Program the infotainment ECU with the latest software package and validate connectivity with dashboard display." 
] 
# Step 2: OpenAI Azure Client Setup 
client = AzureOpenAI( 
    api_version="2024-07-01-preview", 
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
) 
deployment_name = "gpt-4o-mini"  # Your deployment name 
def generate_instruction(task): 
prompt = f""" 
You are an expert automotive manufacturing supervisor. Generate step-by-step 
work instructions for the following new model task. Include safety 
precautions, required tools (if any), and acceptance checks. Write in clear, 
numbered steps suitable for production workers. 
Task: 
\"\"\"{task}\"\"\" 
Work Instructions: 
""" 
response = client.chat.completions.create( 
model=deployment_name, 
messages=[{"role": "user", "content": prompt}], 
temperature=0, 
) 
return response.choices[0].message.content.strip() 
# Step 3: Example Run 
for task in task_descriptions: 
    instructions = generate_instruction(task) 
    print(f"\nTask: {task}\nWork Instructions:\n{instructions}\n") 
input("Nhấn Enter để tiếp tục...")