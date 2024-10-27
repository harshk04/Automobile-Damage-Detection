import google.generativeai as genai
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import ImageOps

#os.environ['api_key']
#API_KEY = os.environ['api_key']
genai.configure(api_key='AIzaSyDUIkj-lz2Lw8Uhj9mP0AE732mNoYccUtU')

model_cfg_path = os.path.join('.', 'model', 'cfg', 'darknet-yolov3.cfg')
model_weights_path = os.path.join('.', 'model', 'weights', 'model.weights')
class_names_path = os.path.join('.', 'model', 'class.names')

input_dir = os.path.join('.', 'images')

# Prepare and upload image
def prep_image(image_path):
    sample_file = genai.upload_file(path=image_path, display_name='Diagram')
    print(f"{sample_file.display_name}:{sample_file.uri}")
    file = genai.get_file(name=sample_file.name)
    print(f"{file.display_name}:{sample_file.uri}")
    return sample_file

def delete_files(img_path):
    # if os.path.exists(img_path):
    #     os.remove(img_path)

    processed_img_path = f".{img_path.split('.')[1]}_processed.png"

    if os.path.exists(processed_img_path):
        os.remove(processed_img_path)

    d = genai.list_files()
    for i in d:
        print(i.name)
        genai.delete_file(i.name)

def extract_text_from_image(img_path):
    sample_file = prep_image(img_path)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = "Extract the 'Indian' vehicle number plate from the image and isolate the numerical and alphabetic characters. Remove any extraneous text, symbols, or logos that may be present on the number plate, and give the output in a single line. Remove all spaces and other characters except alphabets and numerics"
    response = model.generate_content([sample_file, prompt],
	safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH:HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT:HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:HarmBlockThreshold.BLOCK_NONE
	})
    text = response.text

    if text:
        print(img_path.split('\\')[-1])
        delete_files(img_path)
        return text
    else:
        delete_files(img_path)
        return "Failed to extract the vehicle number plate"