from pyrogram import Client as c

API_ID = input("\8245524:\n > ")
API_HASH = input("\b4ee2d8b7c4cb8fff5a572a0ff75bb19:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
