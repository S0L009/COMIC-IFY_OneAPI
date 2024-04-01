import cv2
from imgtxt3gen import draw_text_on_image
from PIL import Image
import streamlit as st

def generate_final_image(full_page_image_path, img0, img1, headings, texts, positions, font_path, font_size, font_color):
    full_page_image = cv2.imread(full_page_image_path)
    im0 = img0
    im1 = img1

    final_image = full_page_image.copy()

    # Inserting Images
    x0, y0 = 1320, 531
    x1, y1 = 80, 2021

    imsize = (1080, 1080)
    im0 = cv2.resize(im0, imsize)
    im1 = cv2.resize(im1, imsize)

    final_image[y0:y0 + im0.shape[0], x0:x0 + im0.shape[1]] = im0
    final_image[y1:y1 + im1.shape[0], x1:x1 + im1.shape[1]] = im1

    # Inserting Text
    for i in range(len(headings)):
        content = [headings[i], texts[i]]
        position = positions[i]
        final_image = draw_text_on_image(final_image, content, font_path, font_size, font_color, position)

    return final_image

def generate_main(imgs, texts):
    
    full_page_image_path = "./Templates/template1.png"
    headings = ["", ""]
    positions = [(149, 600, 950, 950), (1394, 2126, 950, 950)]
    font_path = ["franklin.otf", "franklinh.otf"]
    font_size = [50, 50]
    font_color = "#48716E"
    import numpy as np
    
    img0 = cv2.cvtColor(np.array(imgs[0]), cv2.COLOR_BGR2RGB)
    if len(imgs) == 1: 
        img1 = cv2.imread(r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\codes\Templates\comicify_logo.jpg")
        texts.append("Why Comic-IFY? Comic-ify isn't just about making content pretty; it's about making it accessible. We believe that knowledge should be a joy to consume, not a burden to bear. With Comic-ify, you'll not only understand the content better, but you'll actually enjoy the process. It's a win-win situation.")
    else:
        img1 = cv2.cvtColor(np.array(imgs[1]), cv2.COLOR_BGR2RGB)

    final_image = generate_final_image(full_page_image_path, img0, img1, headings, texts, positions, font_path, font_size, font_color)

    final_image = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
    return final_image


if __name__ == "__main__":
    generate_main()
