import cv2
from imgtxt3gen import draw_text_on_image
from PIL import Image

def generate_final_image(full_page_image_path, im0_path, im1_path, headings, texts, positions, font_path, font_size, font_color):
    full_page_image = cv2.imread(full_page_image_path)
    im0 = cv2.imread(im0_path)
    im1 = cv2.imread(im1_path)

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

# Usage
full_page_image_path = 'Templates/template1.png'
im0_path = 'img/im4.jpg'
im1_path = 'img/im5.jpg'
headings = ["", ""]
texts = [
    "Alrighty, get ready to join me, Mr. Bean, on a wild ride through the world of Formula 1 racing! Imagine this: you've got these sleek, shiny cars that look like they've just zoomed out of one of those fancy sci-fi flicks. But nope, they're the real deal, and they're tearing up the track like nobody's business! It's like watching a bunch of cheetahs on wheels, except these cheetahs are made of metal and they go faster than you can say \"rubber chicken!\"",
    "Now, let's chat about the drivers. These folks aren't your run-of-the-mill racers; oh no, they're like the superheroes of the racing world. They've got nerves of steel and reflexes quicker than me trying to dodge a bean-filled balloon! And boy, do they have to deal with some wacky stuff on the track – hairpin turns that'll make your stomach flip-flop and other drivers sneaking past them like they're late for a delivery of their favorite bean pizza! It's a high-octane mix of speed and strategy, folks, and let me tell you, it's more thrilling than trying to catch your hat in a gust of wind! So, next time you catch those F1 cars zooming by, remember, it's not just a race – it's a bean-tastic symphony of horsepower and adrenaline!"
]
positions = [(149, 600, 950, 950), (1394, 2126, 950, 950)]
font_path = ["franklin.otf", "franklinh.otf"]
font_size = [50, 50]
font_color = "#48716E"

final_image = generate_final_image(full_page_image_path, im0_path, im1_path, headings, texts, positions, font_path, font_size, font_color)

fim = Image.fromarray(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
fim.show()
cv2.imwrite("final_image.jpg", final_image)
