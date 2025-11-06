import openai

def ten_ham(tham_so1, tham_so2):		
    # Khối lệnh bên trong hàm		
    return gia_tri		
		
def tinh_tong(a, b):		
    return a + b		
		
#Gọi hàm
ket_qua = tinh_tong(3, 5)
print(ket_qua)  # Kết quả: 8	

client = OpenAI(api_key="XXXX")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_completion_tokens=150,
  messages=[
    {"role": "system", "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "user", "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)

input("Nhấn Enter để tiếp tục...")