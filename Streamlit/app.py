import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
from api_request_wrapper import request_wrapper, chunk_gen, img_gen
from image_gen_helper import decode_and_save_image
from generate import generate_main

def read_n_return_pages(pdf_path):
  reader = PdfReader(pdf_path) 
  return [page.extract_text().replace('\n',' ') for page in reader.pages]

def process_file(file, theme):

    #Extracting the content from the pdf
    extracted_text = read_n_return_pages(file)

    text = []       #Output text from the model is collected in this
    img_paths = []  #Output paths of the image are collected in this
    file_name = 0

    for chunk in extracted_text:

        #Inputs are fed to the model

        #fantasized txt
        try:
            text.append( request_wrapper(chunk_gen, {"theme": theme, "word_limit": "80", "chunk_content": chunk} ) ['generated-chunk'])

        #inferenced img
            img_paths.append( decode_and_save_image(json_content = request_wrapper(img_gen, {"theme": theme} )['json-b64-format-of-image-generated'], output_filename='img'+str(file_name)))
        except:
            pass

        file_name += 1

    
    final_outputs = [Image.open('./Templates/coverpage.png')]
    final_outputs[0] = final_outputs[0].convert('RGB')

    #this for testing
    # final_outputs = [Image.open('./Templates/comicify_logo.jpg'),Image.open('./Templates/hyper_Avengers2.png'),Image.open('./Templates/hyper_spiderman0.png'),Image.open('./Templates/hyper_spiderman1.png')]

    for i in range(0, len(text), 2):

        #Images and texts are combined a put together in a template using Image Processing techniques
        #Per page, 2 images and 2 text paragraphs corresponding to that image
        final_outputs.append( Image.fromarray( generate_main(im_path = img_paths[i:i+2], texts = text[i:i+2]) ) )

                
    st.write(f'Boom💥💥💥', unsafe_allow_html=True)
    st.write(f'Happy Learning...', unsafe_allow_html=True)


    #Each page is displayed here
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

    st.image(r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\comiclogo.png", use_column_width=True)
    st.markdown('<p style="text-align:center;font-family: cursive, sans-serif;font-size: 20px">Lets make Learning<span style="color:blue;"> Fun, Forever!</span></p>', unsafe_allow_html=True)
    st.title('Select your favourite theme')
    
    theme = st.selectbox('' ,['Avengers','Spiderman','Superman','Doraemon','Pokemon','Ramayana', 'Mahabharatha', 'Harry Potter','WildLife', 'Mr Bean'])
    color = '#23CE6B'
    st.write(f'You selected <span style="color:{color}">{theme}</span>', unsafe_allow_html=True)

    st.title('Upload your boring pdf and watch the magic happen!')
    check = None
    
    with st.form(key='my_form'):
        uploaded_file = st.file_uploader('',type='pdf')   

        if st.form_submit_button(label='Process it'):

            if uploaded_file is not None:
                st.write(f'<span style="color:{color}">Processing...</span>', unsafe_allow_html=True)
                check = process_file(uploaded_file, theme)
            
            else:
                st.write(f'<span style="color:red">File not Found</span>', unsafe_allow_html=True)

    if check or st.session_state.data: 
        
        for i in range(len(st.session_state.prev)):
            st.image(st.session_state.prev[i], caption=f'Page {i+1}', use_column_width=True)

        st.write('Here is ur PDF')
        st.download_button(label="Download⬇️ and have fun🎉", data=st.session_state.data, file_name=st.session_state.output_pdf_path, mime="application/pdf")

def About_us():
    st.title('About Us')
    st.markdown('<p style=text-align:left;font-family: cursive, sans-serif;font-size: 20px">Four dudes from Amrita University who are super eager to win this hackathon...</p>', unsafe_allow_html=True)
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
    st.image(r"C:\Users\Krish\OneDrive - Amrita Vishwa Vidyapeetham\Comic-ify\comiclogo.png", use_column_width=True)
    st.markdown('<p style="text-align:center;font-family: cursive, sans-serif;font-size: 20px">Lets make Learning<span style="color:blue;"> Fun, Forever!</span></p>', unsafe_allow_html=True)
    
    st.title('What is Comic-ify')
    st.markdown("""<p style="text-align:left;font-family: cursive, sans-serif;font-size: 13px">
                Comic-ify, an AI powered Web-Application that transforms textbooks into fun comics and stories using LLMs fine-tuned on our fantasy-specific data and 
                Image Diffusion Models. Users can download the resulting fun-2-read content, improving comprehension and enjoyment of learning.<br><br>
                Lexicon, our fine-tuned model is employed to generate imaginative text and produce images 
                inspired by the text. captivating readers as they explore the content</p><br>""", unsafe_allow_html=True)
    
    st.markdown("""<p style="text-align:left;font-family: Bahnschrift, sans-serif;font-size: 20px"><strong>Input as prompt or PDF :</strong> </p>
                <p style="text-align:left;font-family: cursive, sans-serif;font-size: 13px">Displays modified text/images for prompts, generates a downloadable PDF for PDF input.</p><br>
                <p style="text-align:left;font-family: Bahnschrift, sans-serif;font-size: 20px"><strong>Theme-based generation :</strong> </p>
                <p style="text-align:left;font-family: cursive, sans-serif;font-size: 13px">Users can choose predefined themes. For example, in the 'Indian Mythology' theme, Lord Vishnu could provide insights into the mysteries of black holes in the universe.</p><br>
                <p style="text-align:left;font-family: Bahnschrift, sans-serif;font-size: 20px"><strong>Highlight User's Prefered topics :</strong> </p>
                <p style="text-align:left;font-family: cursive, sans-serif;font-size: 13px">Example: If the emphasis is on Operating Systems, users can prompt for a detailed explanation of how system calls work, directing the explanation accordingly.</p><br>
                """, unsafe_allow_html=True)
    
def main():
    pages = {
        "Home":homepage,
        "About Us": About_us,
        "About Comicify": About_comicify
    }

    selected_page = st.sidebar.radio("Where do u want to go nxt?", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()
