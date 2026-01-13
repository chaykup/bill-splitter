from paddleocr import PaddleOCR

file = str(input("\nPlease provide filename or path to file: "))

print(f"\nInitializing model...\n")
ocr = PaddleOCR(
    lang="en",
    use_textline_orientation=False,
    ocr_version="PP-OCRv4"
)

print(f"\nAnalyzing and extracting text from {file}...")
result = ocr.predict(file)
result[0].save_to_img("backend/output")

print(f"\n{'=' * 25} Successfully extracted text from {file}! {'=' * 25}\n")
data = result[0]["rec_texts"]
for item in data:
    print(f"{item}\n")