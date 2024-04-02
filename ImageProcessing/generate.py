import cv2
from imgtxt3gen import draw_text_on_image
from PIL import Image
import numpy as np
import pandas as pd

def generate_final_image(full_page_image_path, images, headings, texts):
    full_page_image = cv2.imread(full_page_image_path)

    im = [cv2.cvtColor(np.array(i),cv2.COLOR_BGR2RGB) for i in images]

    final_image = full_page_image.copy()

    
    df = pd.read_csv("templates/config.txt")

    entry = df[df["file_path"]==full_page_image_path]

    p1, p2 = tuple([int(i) for i in entry.iloc[0,5].split("/")]), tuple([int(i) for i in entry.iloc[0,6].split("/")])

    full_page_image_path = entry.iloc[0,0]
    positions = [p1, p2]
    font_path = [entry.iloc[0,7], entry.iloc[0,8]]
    font_size = [int(entry.iloc[0,10]), int(entry.iloc[0,11])]
    font_color = entry.iloc[0,9]
   
   
    if entry.iloc[0,1]==1:
        im0 = im[0]
        ip0 = tuple([int(i) for i in entry.iloc[0,3].split("/")])
        x0, y0 = ip0[0], ip0[1]
        imsize1 = (ip0[2], ip0[3])
        im0 = cv2.resize(im0, imsize1)
        final_image[y0:y0 + im0.shape[0], x0:x0 + im0.shape[1]] = im0
        # Inserting Text
        for i in range(len(headings)):
            content = [headings[i], texts[i]]
            position = positions[i]
            final_image = draw_text_on_image(final_image, content, font_path, font_size, font_color, position)

        return final_image
    
    if entry.iloc[0,2] == 1:
        print("\n\n\ndddddsad\n\n")
        texts = [texts[0],""]
        headings  = [headings[0],""]
        
    
    im0 = im[0]
    im1 = im[1]

    
    # Inserting Images
    
    ip1, ip2 = tuple([int(i) for i in entry.iloc[0,3].split("/")]), tuple([int(i) for i in entry.iloc[0,4].split("/")])

    
    x0, y0 = ip1[0], ip1[1]
    x1, y1 = ip2[0], ip2[1]

    imsize1 = (ip1[2], ip1[3])
    imsize2 = (ip2[2], ip2[3])
    
    im0 = cv2.resize(im0, imsize1)
    im1 = cv2.resize(im1, imsize2)

    final_image[y0:y0 + im0.shape[0], x0:x0 + im0.shape[1]] = im0
    final_image[y1:y1 + im1.shape[0], x1:x1 + im1.shape[1]] = im1

    # Inserting Text
    for i in range(len(headings)):
        content = [headings[i], texts[i]]
        position = positions[i]
        final_image = draw_text_on_image(final_image, content, font_path, font_size, font_color, position)

    return final_image


def generate_main(template_name, template_path, images, texts, headings ):


    if len(images) == 1 and template_name == "fw":
        images.append(cv2.cvtColor(cv2.imread(r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\codes\Templates\comicify_logo.jpg"), cv2.COLOR_BGR2RGB))
        texts.append("Comic-ify isn't just about making content pretty; it's about making it accessible. We believe that knowledge should be a joy to consume, not a burden to bear. With Comic-ify, you'll not only understand the content better, but you'll actually enjoy the process. It's a win-win situation.")
        headings.append("Why Comic-IFY?")
    

    final_image = generate_final_image(template_path, images, headings, texts)

    return Image.fromarray(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
   

if __name__ == "__main__":
    generate_main()
