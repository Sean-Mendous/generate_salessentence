import pyperclip
from app.generate_sentence import sales_sentence
from utilities.questionary.questionary import ask_format, ask_prompt

try:
    selected_format_path = ask_format()
except Exception as e:
    print(f'error: ファイルが見つかりませんでした: {e}')
    exit()

try:
    selected_prompt_path = ask_prompt()
except Exception as e:
    print(f'error: ファイルが見つかりませんでした: {e}')
    exit()

for i in range(1, 100000000):
    print(f'\n--- {i}件目の文章生成を開始します ---\n')

    regen_1 = input('名前をコピーしてください、続けるにはEnterを押してください（前回の再生成はqを入力してください）: ')

    if regen_1 == 'q':
        input_name = regen_name
        print(f'> 名前: {input_name}')
        input_info = regen_info
        print(f'> 情報: {input_info[0:200]}')
    else:
        input_name = pyperclip.paste()
        print(f'> 名前: {input_name}')

        regen_2 = input('情報をコピーしてください、続けるにはEnterを押してください: ')
        input_info = pyperclip.paste()
        print(f'> 情報: {input_info[0:200]}')
    
    if not input_name or not input_info:
        print('error: 名前か情報が入力されていません')
        continue

    try:
        generated_sentence = sales_sentence(input_name, input_info, selected_format_path, selected_prompt_path)
        print(f'\n~~~生成内容~~~\n{generated_sentence}\n~~~生成内容~~~\n')

        if generated_sentence:
            pyperclip.copy(generated_sentence)
            print('文章をクリップボードにコピーしました')
        else:
            pyperclip.copy('')
            print('error: 文章が生成されませんでした')
            continue
    except Exception as e:
        pyperclip.copy('')
        print(f'error: 文章が生成されませんでした: {e}')
        continue

    regen_name = input_name
    regen_info = input_info

