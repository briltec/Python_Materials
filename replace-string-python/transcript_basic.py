transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps-lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""

print(transcript.replace("BLASTED", "😤"))

print(transcript.replace("BLASTED", "😤").replace("Blast", "😤"))

replacements = [
    ("BLASTED", "😤"),
    ("Blast", "😤"),
    ("2022-08-24T", ""),
    ("+00:00", ""),
    ("[support_tom]", "Agent"),
    ("[johndoe]", "Client"),
]

for old, new in replacements:
    transcript = transcript.replace(old, new)

print(transcript)
