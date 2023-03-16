from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from sort import main as sort


COMMANDS={'sort directory':sort}

command_completer = WordCompleter(COMMANDS.keys(),ignore_case=True)

while True:
    print('Hello! I am your personal PADAVAN helper')
    print("How can I help you?")
    commands_string = prompt(
            'Enter what do you want to do:',completer=command_completer,complete_while_typing=False).lstrip()
    command=commands_string
    COMMANDS[command]()

