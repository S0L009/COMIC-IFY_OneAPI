import pandas as pd
import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
from api_request_wrapper import request_wrapper, chunk_gen, img_gen, head_gen, detailed_info_gen
from image_gen_helper import decode_and_save_image
from generate1 import generate_main
from streamlit_option_menu import option_menu
import base64
import re
def read_n_return_pages(pdf_path):
  reader = PdfReader(pdf_path) 
  return [page.extract_text().replace('\n',' ') for page in reader.pages]

def process_file(file, theme, template):

    #Extracting the content from the pdf
    extracted_text = read_n_return_pages(file)



    df = pd.read_csv('Templates/config.txt')
    num_img = df[df['file_path']==template]['numim'].iloc[0]
    num_txt = df[df['file_path']==template]['numbox'].iloc[0]
    template_name = re.search(r'/(ss|dd|fw)',template)[0][1:]


    text = []       #Output text from the model is collected in this
    imgs = []       #Output paths of the image are collected in this
    heading = [] 
    detailed_info = []      #detailed_info   -> 

    for chunk in extracted_text:

        try:

            if template_name == "ss" :  num_images = num_img
            else:  num_images = 1

            text.append( request_wrapper(chunk_gen, {"theme": theme, "word_limit": "80", "chunk_content": chunk} ) ['generated-chunk'])
            heading.append( request_wrapper(head_gen, {'chunk':text[-1]})['generated-heading'] )

            if template_name == 'dd' or template_name == 'ss': 
                    text.append( request_wrapper(detailed_info_gen, {"word_limit": "300", 'chunk':chunk} )['extracted-detailed-info'] )
                    # Have to replace ** with '' and - with \n
                    text[-1] = ((text[-1].replace("**","")).replace("#","")).replace("-",'\\n')
                    heading.append("")

            if template_name == "ss": text[-2] = ""
            

            for _ in range(num_images): 
                imgs.append(decode_and_save_image(json_content = request_wrapper(img_gen, {"theme": theme} )['json-b64-format-of-image-generated']))

        except:
            pass

    final_outputs = [Image.open('./Templates/coverpage.png')]
    final_outputs[0] = final_outputs[0].convert('RGB')

    #in ttt.ipynb

    idx = 0
    if template_name == "ss":   #appending detailed info into text, detailed info starts from index 1
        num_txt += 1
        
    for i,j in zip(range(0, len(imgs), num_img), range(idx, len(text), num_txt)):

        #template text

        if template_name == 'ss': 
            temp_head = heading[j:j+num_txt]
            temp_text = text[j:j+num_txt][::-1]
        else: 
            temp_head = heading[j:j+num_txt]
            temp_text = text[j:j+num_txt]
        

        final_outputs.append( generate_main(template_name = template_name, template_path = template, images = imgs[i:i+num_img], texts = temp_text, headings = temp_head) )

                
    st.write(f'Boom💥💥💥', unsafe_allow_html=True)
    st.write(f'Happy Learning...', unsafe_allow_html=True)


    #Each page is stored here
    st.session_state.prev = final_outputs[:]
        
    # Images to PDF
    output_pdf_path = "🔥.pdf"

    from io import BytesIO

    pdf_bts = BytesIO()
    final_outputs[0].save(pdf_bts, "PDF" ,resolution=100.0, save_all=True, append_images=final_outputs[1:])  
    pdf_bts.seek(0)
    st.session_state.data, st.session_state.output_pdf_path = pdf_bts, output_pdf_path
    
    return True

def homepage():

    if 'prev' not in st.session_state:
        st.session_state.prev = False

    if 'data' not in st.session_state:
        st.session_state.data = False

    if 'output_pdf_path' not in st.session_state:
        st.session_state.output_pdf_path = False

    with open('Templates/bgg1.jpg', "rb") as img_file:
        img_data = img_file.read()

    img_base64 = base64.b64encode(img_data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('data:image/{"png"};base64,{img_base64}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    #LOGO
    st.image(r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\comiclogo.png", use_column_width=True)
    st.markdown('<p style="text-align:center; font-family: cursive, sans-serif; font-size: 30px; ">Lets make Learning<strong><span style="color:yellow;text-shadow: 1px 1px 15px rgba(255, 255, 0, 0.6);"> Fun, Forever!</span></strong></p>', unsafe_allow_html=True)


    #THEME
    st.title('Select your favourite theme')
    theme = st.selectbox('' ,['Avengers','Spiderman','Superman','Doraemon','Pokemon','Ramayana', 'Mahabharatha', 'Harry Potter','WildLife', 'Mr Bean'])
    color = 'yellow'
    st.write(f'<p style =" font-size: 20px">You selected <strong style="color:{color};">{theme}</strong></p>', unsafe_allow_html=True)



    #TEMPLATE
    st.title('Choose a template (Selection controls content gen method)')
    template = st.selectbox('' ,['Get your feet wet - 1','Get your feet wet - 2','Get your feet wet - 3', 'Dive Deep - 1', 'Dive Deep - 2', 'Dive Deep - 3', 'Splash and Submerge - 1', 'Splash and Submerge - 2', 'Splash and Submerge - 3'])


    l, m = st.columns(2)
    with l:
        st.write(f'<p style =" font-size: 20px">You selected <strong style="color:{color};">{template}</strong></p>', unsafe_allow_html=True)

    template_file = {'Get your feet wet - 1':"Templates/fw01.png", 'Get your feet wet - 2':"Templates/fw02.png", 'Get your feet wet - 3':"Templates/fw03.png",
                    'Dive Deep - 1':"Templates/dd01.png", 'Dive Deep - 2':"Templates/dd02.png", 'Dive Deep - 3':"Templates/dd03.png",
                    'Splash and Submerge - 1':"Templates/ss01.png", 'Splash and Submerge - 2':"Templates/ss02.png", 'Splash and Submerge - 3':"Templates/ss03.png"}
                    
    template = template_file[template]
    with m:
        st.image(template,width=250)

    st.title('Upload your boring pdf and watch the magic happen!')
    check = None
    
    with st.form(key='my_form'):
        uploaded_file = st.file_uploader('',type='pdf')   

        if st.form_submit_button(label='Process it'):

            if uploaded_file is not None:
                st.write(f'<span style="color:{color}">Processing...</span>', unsafe_allow_html=True)
                check = process_file(uploaded_file, theme, template)
            
            else:
                st.write(f'<span style="color:red">File not Found</span>', unsafe_allow_html=True)

    if check or st.session_state.data: 
        
        for i in range(len(st.session_state.prev)):
            st.image(st.session_state.prev[i], caption=f'Page {i+1}', use_column_width=True)

        st.write('Here is ur PDF')
        st.download_button(label="Download⬇️ and have fun🎉", data=st.session_state.data, file_name=st.session_state.output_pdf_path, mime="application/pdf")

def About_us():

    with open('Templates/bg_a1.jpg', "rb") as img_file:
        img_data = img_file.read()

    img_base64 = base64.b64encode(img_data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('data:image/{"png"};base64,{img_base64}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('About Us')
    st.markdown('<p style="text-align:left;font-family: sans-serif;font-size: 19px">Four dudes from Amrita University who are intensely keen to win this hackathon...</p>', unsafe_allow_html=True)
    images_with_captions = [
        (r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\amrith.jpg", "Amrith"),
        (r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\surya.jpg", "Surya"),
        (r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\srikar.jpg", "Srikar"),
        (r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\me.jpg", "Navneet")
    ]

    col0, col1, col2, col3 = st.columns(4)

    with col0:
        st.markdown(f'<h1 style="text-align: center;font-family:Consolas;font-size:25px">{images_with_captions[0][1]}</h1>',unsafe_allow_html=True)
        st.image(images_with_captions[0][0])
    with col1:
        st.markdown(f'<h1 style="text-align: center;font-family:Consolas;font-size:25px">{images_with_captions[1][1]}</h1>',unsafe_allow_html=True)
        st.image(images_with_captions[1][0])
    with col2:
        st.markdown(f'<h1 style="text-align: center;font-family:Consolas;font-size:25px">{images_with_captions[2][1]}</h1>',unsafe_allow_html=True)
        st.image(images_with_captions[2][0])
    with col3:
        st.markdown(f'<h1 style="text-align: center;font-family:Consolas;font-size:25px">{images_with_captions[3][1]}</h1>',unsafe_allow_html=True)
        st.image(images_with_captions[3][0])

def About_comicify():
    with open('Templates/bg_c1.jpg', "rb") as img_file:
        img_data = img_file.read()

    img_base64 = base64.b64encode(img_data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('data:image/{"png"};base64,{img_base64}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image(r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\comiclogo.png", use_column_width=True)
    st.markdown('<p style="text-align:center;font-family: cursive, sans-serif;font-size: 20px">Lets make Learning<span style="color:blue;"> Fun, Forever!</span></p>', unsafe_allow_html=True)
    
    st.title('What is Comic-ify')
    st.markdown("""<p style="text-align:left;font-family: cursive, sans-serif;font-size: 20px">
                Comic-ify, an AI powered Web-Application that transforms textbooks into fun comics and stories using LLMs fine-tuned on our fantasy-specific data and 
                Image Diffusion Models. Users can download the resulting fun-2-read content, improving comprehension and enjoyment of learning.<br><br>
                Lexicon, our fine-tuned model is employed to generate imaginative text and produce images 
                inspired by the text. captivating readers as they explore the content</p><br>""", unsafe_allow_html=True)
    
    st.markdown("""<p style="text-align:left;font-family: Bahnschrift, sans-serif;font-size: 30px"><strong>Input as prompt or PDF :</strong> </p>
                <p style="text-align:left;font-family: cursive, sans-serif;font-size: 20px">Displays modified text/images for prompts, generates a downloadable PDF for PDF input.</p><br>
                <p style="text-align:left;font-family: Bahnschrift, sans-serif;font-size: 30px"><strong>Theme-based generation :</strong> </p>
                <p style="text-align:left;font-family: cursive, sans-serif;font-size: 20px">Users can choose predefined themes. For example, in the 'Indian Mythology' theme, Lord Vishnu could provide insights into the mysteries of black holes in the universe.</p><br>
                <p style="text-align:left;font-family: Bahnschrift, sans-serif;font-size: 30px"><strong>Highlight User's Prefered topics :</strong> </p>
                <p style="text-align:left;font-family: cursive, sans-serif;font-size: 20px">Example: If the emphasis is on Operating Systems, users can prompt for a detailed explanation of how system calls work, directing the explanation accordingly.</p><br>
                """, unsafe_allow_html=True)
    
def main():

    pages_dict = {
        "Home":homepage,
        "About Us": About_us,
        "About Comicify": About_comicify
    }

    with open('Templates/sidebar1.jpg', "rb") as img_file:
        img_data = img_file.read()

    img_base64 = base64.b64encode(img_data).decode()

    st.markdown(
        f"""
        <style>
        [data-testid=stSidebar] {{
            background-color: dark-grey;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        selected_page = option_menu(
            menu_title=None,
            options=["Home", "About Us", "About Comicify"],
            icons=['house-door-fill','info-square-fill','emoji-heart-eyes-fill'],
            menu_icon='cast',
            styles={
            "container": {"padding": "0!important","background-color": "black"},
            "icon": {"font-size": "20px"}, 
            "nav-link": {"color": "white","font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#6B23CE"},
            "nav-link-selected": {"color": "black", "background-color": "white"},
            'icon-selected':{'color':'white'},
            }
        )
    pages_dict[selected_page]()

if __name__ == "__main__":
    main()
