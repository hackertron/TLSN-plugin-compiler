import json
import os

# Load the JSON payload
with open("payload.json", "r") as f:
    payload = json.load(f)

# Ensure directories exist
os.makedirs("src", exist_ok=True)
os.makedirs("utils", exist_ok=True)

# Write index.d.ts
with open("src/index.d.ts", "w") as f:
    f.write(payload["index.d.ts"])

# Write index.ts
with open("src/index.ts", "w") as f:
    f.write(payload["index.ts"])

# Write utils/hf.js
with open("utils/hf.js", "w") as f:
    f.write(payload["utils/hf.js"])

print("Files have been written successfully.")
