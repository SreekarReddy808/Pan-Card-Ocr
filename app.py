from src.image_preprocessing import preprocess_image
from src.ocr_engine import extract_text
from src.pan_extractor import extract_pan_details
import json

IMAGE_PATH = "images/sample_pan.jpg"

def main():

    processed_image = preprocess_image(IMAGE_PATH)

    text = extract_text(processed_image)

    pan_details = extract_pan_details(text)

    print("\nExtracted PAN Details:\n")
    print(json.dumps(pan_details, indent=4))

    with open("output/extracted_data.json", "w") as f:
        json.dump(pan_details, f, indent=4)

if __name__ == "__main__":
    main()
