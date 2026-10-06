from utils.llm import analyze_document

sample_text = """
College Scholarship Notification

Students can apply for the scholarship before 20 October 2026.

Required documents:
Aadhaar Card
Income Certificate
Mark Sheet
Bank Details
"""

result = analyze_document(sample_text)

print(result)