import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is missing. Add it to the .env file.")

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)

MODEL = "openai/gpt-oss-120b"


def analyze_document(text):

    prompt = f"""
You are SmartDoc AI, an intelligent document understanding assistant.

The following text was extracted from a document using OCR.
OCR may contain spelling mistakes, broken characters, or formatting errors.

Your task is to understand the document carefully and organize the
information without inventing anything.

OCR TEXT:
{text}

Return the result using exactly these sections:

DOCUMENT TYPE:
Identify the most likely type of document.

SUMMARY:
Give a simple 3-5 sentence summary.

KEY INFORMATION:
Extract important information such as:
- Organization
- Person/Customer name
- Consumer or reference number
- Receipt number
- Bill number
- Transaction number
- Account number
Only include fields that are actually present.

AMOUNT:
Identify the total amount and currency.
If the amount is unclear, say "Amount unclear from OCR."

PAYMENT STATUS:
Identify whether the document indicates Paid, Unpaid, Pending,
or another status.

PAYMENT METHOD:
Identify the payment method if present.

IMPORTANT DATES:
List important dates and explain what each date means.

REQUIRED ACTIONS:
Explain what the reader needs to do, if anything.

IMPORTANT:
1. Do not invent information.
2. Do not create missing values.
3. Correct obvious OCR mistakes only when the surrounding context
   clearly supports the correction.
4. If information is uncertain, clearly say that it is uncertain.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise document analysis assistant. "
                    "Never hallucinate document information."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1200,
        temperature=0.1
    )

    return response.choices[0].message.content