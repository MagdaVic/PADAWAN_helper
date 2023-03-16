from collections import UserList
from datetime import datetime


class NoteBook(UserList):
    def __init__(self):
        self.data = []

    def generator(self):
        for it in self.data:
            yield f"  > {it}"

    
    def iterator(self, value):

        value = value
        gen = self.generator()

        while value > 0:
            try:
                if self.data == []:
                    print("  > Your notebook is empty(")
                print(next(gen))
                value -= 1
            except StopIteration:
                return ""
        print("  > Thats all!") 

    def add(self, rec):
        self.data.append(rec)
        print(f"  > You have added a note: {rec.name}")
        print(f"  > {rec}")

    def remove(self, name):
        for it in self.data:
            if str(it.name) == name:
                print(f"  > You have deleted the note {name}")
                self.data.remove(it)
            else:
                print("  > Note with this name was not found.")

    def edit(self, name):
        for it in self.data:
            if str(it.name) == name.title():  
                while True:
                    value = (input("    > Choose what to edit. Name/Tags/Note: ")).title()
                    if value == "Name":
                        it.name = NoteName()
                        it.time = TimeRec()
                        print(f"  > {it}")
                        break
                    elif value == "Tags":
                        it.tags = Tag()
                        it.time = TimeRec()
                        print(f"  > {it}")
                        break
                    elif value == "Note":
                        it.note = Note()
                        it.time = TimeRec()
                        print(f"  > {it}")
                        break
                    else:
                        print("  > I don't know what it is(")
            else:
                print("  > Note with this name was not found.")



######################################

class NoteName:
    def __init__(self):
        while True:
            self.inp = input("    > Name of the note: ")
            if len(self.inp.replace(" ", "")) > 20:
                print("  > The title is too long......... Must be less than 20.")
            elif self.inp == "":
                print("  > Please enter the name of the note.")
            else:
                self.value = self.inp.title()
                break
                

    def __repr__(self):
        return f"{self.value}"
    

class Tag:
    def __init__(self):
        while True:
            self.inp = (input("    > Enter tags separated by a space: ")).split(" ")
            if len(self.inp) < 10:
                self.value = self.inp
                break
            else:
                print("  > Too long......... Must be less than 10.")

    def __repr__(self):
        return f"#{' #'.join(self.value)}"


class Note:
    def __init__(self):
        while True:
            self.inp = input("    > Note: ")
            if len(self.inp.replace(" ", "")) < 500:
                self.value = self.inp
                break
            else:
                print("  > Too long......... Must be less than 500.")

    def __repr__(self):
        return f"{self.value}"


class TimeRec:
    def __init__(self):
        self.value = datetime.today()

    def __repr__(self):
        return f"{self.value.strftime('%d %b %Y, %H:%M')}"


######################################

class Record:

    def __init__(self, name="", tags="", note="", time=""):

        self.name = name
        self.tags = tags
        self.note = note
        self.time = time

    def __repr__(self):
        return f"{self.name}     {self.time}\n{self.tags}\n{self.note}\n"

######################################

class Bot:
    def __init__(self):
        self.book = NoteBook()

    def handle(self, comand):
        if comand == 'add':
            name = NoteName()
            tags = Tag()
            note = Note()
            time = TimeRec()
            record = Record(name, tags, note, time)
            return self.book.add(record)
        elif comand == "show":
            while True:
                try:
                    num = int(input("    > How much: "))
                    return self.book.iterator(num)
                except ValueError:
                    print("    > Enter a number")
        elif comand == "remove":
            name = (input("    > Enter the name of the note you want to delete: ")).title()
            return self.book.remove(name)
        elif comand == "edit":
            name = input("    > Enter the name of the note you want to edit: ")
            return self.book.edit(name)
        else:
            print(f"  > I don't know such a command(")



######################################
            
def main():
    print("    > Hello. I am a notebook assistant. Shall we add a note?")
    bot = Bot()
    while True:
        comand = (input("    > Your command: ")).lower()
        if comand in ["exit", "close"]:
            return
        else:
            bot.handle(comand)

######################################
    
if __name__ == "__main__":
    main()
    



