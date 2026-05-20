import ollama
messages = []
while True:
    user_question = input("Ask Biff:")
    messages.append({
        'role': 'user',
       'content': user_question})
    print("><(((((o> Please Wait")
    response = ollama.chat(
        model='biff',
        messages=messages
    )
    assistant_reply = response['message']['content']
    print(assistant_reply)
    messages.append({
        'role': 'assistant',
        'content':assistant_reply
    })
    if user_question == "eat":
        print("...")
        break