from utilities.llm.chatgpt import chatgpt_4omini

def sales_sentence(name, info, format_path, prompt_path):
    prompt = create_prompt(name, info, format_path, prompt_path)
    response = chatgpt_4omini(prompt)
    return response

def create_prompt(input_name, input_info, format_path, prompt_path):
    with open(format_path, 'r') as file:
        format_txt = file.read()
    
    with open(prompt_path, 'r') as file:
        prompt_md = file.read()
    
    overall_prompt = f"# プロンプト\n{prompt_md}\n# 雛形\n{format_txt}\n# 貴社の会社名もしくは担当者名\n{input_name}\n# 貴社のその他の情報\n{input_info}"
    
    return overall_prompt

if __name__ == "__main__":
    import time
    import pyperclip

    for i in range(100000000):
        input = input("Enter the input: ")
        prompt = create_prompt(input)
        response = chatgpt_4omini(prompt)
        if response:
            print(f'copied to clipboard:\n{response}')
            pyperclip.copy(response)
        else:
            print("Failed to generate response")
        time.sleep(3)

