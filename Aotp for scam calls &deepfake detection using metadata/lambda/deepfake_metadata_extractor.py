from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    metadata = {}
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value
    return metadata

if __name__ == "__main__":
    image_path = "sample.jpg"
    metadata = extract_metadata(image_path)
    for key, value in metadata.items():
        print(f"{key}: {value}")
