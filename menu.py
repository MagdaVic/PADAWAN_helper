import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from sort import main as sort
from addressbook import main as addressbook

def exit_from_chat():
    sys.exit('Good bye!')

COMMANDS={'use addressbook':addressbook,'sort directory':sort,'exit': exit_from_chat}

command_completer = WordCompleter(COMMANDS.keys(),ignore_case=True)
print('Hello! I am your personal PADAWAN helper')
print("How can I help you?")
while True:
    commands_string = prompt(
            'Enter what do you want to do:',completer=command_completer,complete_while_typing=False).lstrip()
    for i in COMMANDS.keys():
        if commands_string.lower().startswith(i):
            command = commands_string[:len(i)].lower()
            COMMANDS[command]()
            break

