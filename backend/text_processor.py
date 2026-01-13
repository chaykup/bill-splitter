from paddleocr import PaddleOCR

file = str(input("\nPlease provide filename or path to file: "))

print(f"\nInitializing model...")
ocr = PaddleOCR(
    lang="en",
    use_angle_cls=False,
    ocr_version="PP-OCRv4",
)

print(f"\nAnalyzing text...")
result = ocr.predict(file) 

print(f"\nSaving results...")
for res in result:  
    res.print()  
    res.save_to_img("backend/output")  
    res.save_to_json("backend/output")

print(f"{'=' * 25}Successfully extracted text from {file}!{'=' * 25}")