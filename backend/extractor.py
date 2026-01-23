from paddleocr import PaddleOCR, LayoutDetection, PPStructureV3

file = str(input("\nPlease provide filename or path to file: "))

print(f"\nInitializing model...\n")
ocr = PPStructureV3(
    text_recognition_model_name="en_PP-OCRv4_mobile_rec",
    lang="en",
    use_doc_unwarping=True
    )

print(f"\nAnalyzing and extracting text from {file}...")
result = ocr.predict(input=file)
result[0].save_to_img("backend/output")

print(f"\n{'=' * 25} Successfully extracted text from {file}! {'=' * 25}\n")
data = result[0]
for item in data:
    print(f"- {item}\n")