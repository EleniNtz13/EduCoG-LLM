from openai import OpenAI

client = OpenAI(
    api_key="Εισάγετε το API key"
)

try:
    with open("prompt.txt", "r", encoding="utf-8") as prompt_file:
        prompt = prompt_file.read().strip()
except FileNotFoundError:
    print("Error: Το αρχείο 'prompt.txt' δεν βρέθηκε. Ελέγξτε τον τρέχοντα φάκελο εργασίας και το όνομα αρχείου.")
    exit(1)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

output_message = completion.choices[0].message.content

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(output_message)

print("Τα αποτελέσματα έχουν αποθηκευτεί στο αρχείο output.txt")
