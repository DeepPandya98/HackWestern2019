from google.cloud import vision
import io
import os
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    ingredients = []
    if(len(texts) > 0):
        ingredients = texts[0].description.split('\n')
    return ingredients
