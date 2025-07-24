import os
import questionary

def ask_prompt():
    dir = "input/prompts"
    files = [name for name in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, name))]
    files = [name for name in files if not name.startswith('.')] # 隠しファイルの消去

    if not files:
        raise RuntimeError("ファイルが見つかりませんでした")
    else:
        sorted_files = sorted(files, reverse=True)
        selected_file = questionary.select(
            "Select a file:",
            choices=sorted_files
        ).ask()

    print(f"Selected file: {selected_file}")
    return f'{dir}/{selected_file}'

def ask_format():
    dir = "input/formats"
    files = [name for name in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, name))]
    files = [name for name in files if not name.startswith('.')] # 隠しファイルの消去

    if not files:
        raise RuntimeError("ファイルが見つかりませんでした")
    else:
        sorted_files = sorted(files, reverse=True)
        selected_file = questionary.select(
            "Select a file:",
            choices=sorted_files
        ).ask()

    print(f"Selected file: {selected_file}")
    return f'{dir}/{selected_file}'