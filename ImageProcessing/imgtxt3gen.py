from PIL import Image, ImageDraw, ImageFont
import numpy as np

def draw_text_on_image(input_image_array, content, font_path, font_size, font_color, frame_coords):
    # Convert the OpenCV image array to PIL Image
    heading = content[0]
    text = content[1]
    
    text_size = font_size[0]
    heading_size = font_size[1]
    
    print(content, font_path, font_size, font_color, frame_coords)

    
    font = ImageFont.truetype(font_path[0], text_size)
    fonth = ImageFont.truetype(font_path[1], heading_size)
    
    font_color = font_color
    
    image = Image.fromarray(input_image_array)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    

    # Function to draw text within a frame
    def draw_text_within_frame(draw, text):
        # Load font




        #HEading First
        frame_x, frame_y, frame_width, frame_height = frame_coords        
        max_text_width = frame_width

        #initial offsets from frame

        text_width, text_height = draw.textsize(heading, font=fonth)
        #frame_x+=50
        #frame_width-=50
        #frame_y+=60
        draw.text((frame_x, frame_y), heading, fill=font_color, font=fonth)
        frame_y+=text_height+50
        #print(text_height)

        # Split the text into lines that fit within the frame width
        lines = []
        line = ""
        words = text.split()
        
        

        
        for word in words:
            test_line = line + word + " "
            text_width, _ = draw.textsize(test_line, font=font)
            if text_width <= max_text_width:
                line = test_line
            else:
                if len(word) > max_text_width // text_size:
                    # Handle big words that need to continue on the next line
                    word_lines = [word[i:i+max_text_width // text_size] for i in range(0, len(word), max_text_width // text_size)]
                    for word_line in word_lines:
                        lines.append(line)
                        line = word_line + " "
                else:
                    lines.append(line)
                    line = word + " "
        lines.append(line)
        
        # Draw the text on the image within the frame
        text_height = 0
        for line in lines:
            text_width, text_height = draw.textsize(line, font=font)
            if frame_y + text_height <= frame_coords[1] + frame_coords[3]:
                draw.text((frame_x, frame_y), line, fill=font_color, font=font)
                frame_y += text_height+20  # Move to the next line
            else:
                # No more space in the frame, break the loop
                break
        
        # Return the total height of the drawn text
        return text_height * len(lines)
    
    # Draw text within the frame
    total_text_height = draw_text_within_frame(draw, text)
    
    # Return the modified image as a numpy array
    return np.array(image)
