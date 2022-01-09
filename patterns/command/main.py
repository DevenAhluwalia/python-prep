from clients.on_off_client import OnOrOffClient
from clients.undo_client import UndoClient

print("Executing on_off_client")
print()

OnOrOffClient().execute()
print()

print("Executing undo_client")
print()

UndoClient().execute()
print()