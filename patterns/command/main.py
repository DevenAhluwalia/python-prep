from clients.on_off_client import OnOrOffClient
from clients.undo_client import UndoClient

print(f"\n\nExecuting on_off_client \n{'-'*50}\n")
OnOrOffClient().execute()

print(f"\n\nExecuting undo_client \n{'-'*50}\n")
UndoClient().execute()
