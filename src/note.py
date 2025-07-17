from collections import UserDict


class Tags(UserDict):
    def __init__(self, tags):
        super().__init__()
        self.data = tags

    def __repr__(self):
        return f"Tags({self.data})"


class Note:
    def __init__(self, data):
        tags, description = data[0], data[1]
        self.tags = Tags(tags)
        self.description = description

    def __repr__(self):
        return f"Note(tags={self.tags}, description={self.description})"
      
      
def note_handler(book, args):
    command = args[0]
    name = args[1]
    
    if command == "show":
        record = book.find(name)
        if not record:
            print("❌ Contact not found.")
            return
        note = record.note if record.note else "No note"
        if not note:
            print("❌ No notes found for this contact.")
            return
        print(f"Notes for {name}:")
        print(note.tags, note.description)
        return
    elif command == "add":
        record = book.find(name)
        print (f"Adding note to contact: {name}")
        tags = args[2].split(",")
        description = args[3]
        print(f"Tags: {tags}, Description: {description}")
        note = (tags, description)
        record.add_note(note)
        print("Note added:", note)
        return
    print("Handling notes with args:", args)
    return 
    