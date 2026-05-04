import chromadb

SEPARATOR = "-" * 70

client = chromadb.PersistentClient("./chroma_db")

def load_chunks(filename):
    with open(filename) as f:
        text = f.read()

    sections = text.split(SEPARATOR)

    chunks = []
    for section in sections:
        chunks.append(section.strip())
    return chunks


print(load_chunks('roster_2026.txt'))

files_and_collections = [
    ("roster_2026.txt",roster_2026),
    ("scouting_2027.txt",scouting_2027),
    ("opponents_2026.txt",opponents_2026)
]