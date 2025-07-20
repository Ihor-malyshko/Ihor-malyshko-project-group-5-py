import ui.ui_screens as ui_screens
from ui.ui_helpers import (
    parse_input,
    render_table,
    # styled_prompt,
    # styled_prompt_with_prefix,
)


from ui.ui_helpers import parse_input
from utils import convert_to_data

def wrap_args_handler(args):
    full_text = " ".join(args)
    
    # Split by comma and handle cases with missing parts
    parts = full_text.split(",")
    
    # Default values
    name = ""
    tags = ""
    description = ""
    
    # Extract parts based on what's available
    if len(parts) >= 1:
        name = parts[0].strip()
    if len(parts) >= 2:
        tags = parts[1].strip()
    if len(parts) >= 3:
        description = parts[2].strip()
    return name, tags, description


def add_note(book, args):
    name, tags, description = wrap_args_handler(args)
    
    
    # Verify that we have at least a name
    if not name:
        ui_screens.print_error_message("Contact name is required.")

        return
    
    record = book.find(name)
    if not record:
        ui_screens.print_error_message(f"Contact '{name}' not found.")
        return
    
    # Create note even if tags or description are empty
    note = (tags, description)
    record.add_note(note)
    ui_screens.print_success_message("Note added successfully")
    return

def edit_note(book, args):
  name, tags, description = wrap_args_handler(args)
  record = book.find(name)
  if not record:
      ui_screens.print_error_message(f"Contact '{name}' not found.")
      return
  if not hasattr(record, 'note') or record.note is None:
      ui_screens.print_error_message(f"Contact '{name}' has no note to edit.")
      return

  record.add_note((tags, description))
  ui_screens.print_success_message("Note edited successfully")
  return


def delete_note(book, args):
  name = args[0]
  record = book.find(name)
  if not record:
      ui_screens.print_error_message(f"Contact '{name}' not found.")
      return
  record.note = None
  ui_screens.print_success_message(f"Note for contact '{name}' deleted.")
  return



def search_contacts_by_tag(book, args):
  tag = args[0]
  results = []
  for record in book.data.values():
      if hasattr(record, 'note') and record.note and tag in record.note.tags.data:
          results.append(record)
  
  data = convert_to_data(results)
  
  
  ui_screens.print_success_message(f"Found {len(results)} contact(s) with tag:")
  render_table(data)

  return

def show_contacts_with_notes(book):
    """
    Show all contacts that have notes attached to them.
    """

    results = []
    for record in book.data.values():
        if hasattr(record, 'note') and record.note:
            # Check if the record has a note
            results.append(record)

    if not results:
        ui_screens.print_error_message("No contacts with notes found.")
        return
      
    
    data = convert_to_data(results)

    ui_screens.print_success_message(f"Found {len(results)} contact(s) with notes:")
    render_table(data)

    return