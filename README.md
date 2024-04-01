<!--
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/WhatsApp%20Image%202024-03-26%20at%2021.01.47_a572f875.jpg?raw=true" alt="Logo">
</p> -->

<img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/main/images/comicify_logo_sk.jpg" alt="cropped_logo">

# Transforming Words to Worlds
<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamlyYWRhZnJucGF4ejM1Y2Z4Mmg2NmtvZTBmaWRiZGg2Y25rcW13NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F2gwWo2vLgRMhjLFs0/giphy.gif" alt="W2W">
</p>

# HOLA! WE ARE COMIC-IFY
<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG9ycXE2M3JuZW1jZ2FteDJldHc2MWtwaDloYWU2b2M3Z3BhZGt6dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MlxI9wxBir2kVzvkIQ/giphy.gif" alt="Hello">
</p>

## What is Comic-ify?
Comic-ify is not just another tool. It's a revolution in how we consume information. Imagine this: you have a stack of boring PDFs, full of dense text that drains your energy just thinking about it. We've all been there. But fear not! Comic-ify is here to transform your reading experience.

## The Problem
Let's face it, deciphering pages of dull, overwhelming text is like trying to climb a mountain without a rope. It's tough, it's exhausting, and frankly, it's no fun at all. We've experienced this struggle since our early days, constantly grappling with the challenge of making tedious content engaging.

## Our Solution
Enter Comic-ify. Powered by state-of-the-art LLM-based models, our application works like magic. Simply upload your PDF filled with mind-numbing text, and watch as it morphs into a vibrant, visually appealing comic-style content. Say goodbye to the days of drowning in endless paragraphs and hello to a world where information leaps off the page and takes you where you belong!!

## Why Comic-ify?
Comic-ify isn't just about making content pretty; it's about making it accessible. We believe that knowledge should be a joy to consume, not a burden to bear. With Comic-ify, you'll not only understand the content better, but you'll actually enjoy the process. It's a win-win situation.

## Features
Lexicon, our fine-tuned model is employed to generate imaginative text and produce images inspired by the text. captivating readers as they explore the content

- **Input as prompt or PDF**
Displays modified text/images for prompts, generates a downloadable PDF for PDF input.

- **Theme-based generation**
Users can choose predefined themes. For example, in the 'Indian Mythology' theme, Lord Vishnu could provide insights into the mysteries of black holes in the universe.

- **Highlight User’s Prefered topics**
Example: If the emphasis is on Operating Systems, users can prompt for a detailed explanation of how system calls work, directing the explanation accordingly.

## HOW OUR WORK FLOWS:
<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3V6YXNiZTVwYTNqN3ZnanNjOXRoM2l6ZDVtdGZ5Z2R0bG1nNHNrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26xBKuuVuNxp8seTS/giphy.gif" alt="workflow_gif">
</p>

<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/Comicify-PPT.png?raw=true" alt="workflow">
</p>


 ## **Check Out Our Demo and Model**

**Explore our demo video on YouTube and our Hugging Face model below:**

<div align="center">
  <p align="center"><strong>YouTube Demo</strong></p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=1xngEIozVgw">
      <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzNzYW9ic21ybW0yeXJka2xvdjVkNGt1czc5aHBsMWE2b2UzYWxvdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13Nc3xlO1kGg3S/giphy.gif" alt="YouTube GIF" width="150">
    </a>
    <br>
    <a href="https://www.youtube.com/watch?v=1xngEIozVgw">Click Here!</a>
  </p>
</div>

<div align="center">
  <p align="center"><strong>Hugging Face Model</strong></p>
  <p align="center">
    <a href="https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/models#latent-consistency-models">
      <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTNlcW96bHVocmd5dmU2dnNnOWxkMTQ1MWdveDd0dG82ZjVhdWNiYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zYoSeYMRUEHQwD4Mh7/giphy.gif" alt="Hugging Face GIF" width="150">
    </a>
    <br>
    <a href="https://huggingface.co/docs/optimum/main/en/onnxruntime/usage_guides/models#latent-consistency-models">Click Here!</a>
  </p>
</div>




## RUNNING FAST API

To run the FastAPI app locally

Step1: install the fastapi directory from the repo, and navigate the termial to it



step2: pip install requirements.txt file
```bash
pip install -r requirements.txt
```

step3: run the uvicorn ASGI server to get the endpoints functional
```bash
uvicorn main:app --reload
```

step4: Test the APIs on Swagger-UI
<img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/main/images/FASTAPI-SWAGGER-UI-SS.png" alt="swagger_ui_ss">

## Intel Tool-Kits Used
| **Sno** | **Intel Product Used** | **Description** | 
|---|---|---|
| 1 | Intel® Distribution for Python® | We are using this toolkit as it provides optimized Python libraries for numerical computing and data manipulation | 
| 2 | Intel® OpenVINO™ | We are making the process of implementing Q-LoRA faster using OpenVINO | 
| 3 | Intel® DevCloud | DevCloud offers a valuable environment for our project |


## Dataset
We have uploaded the dataset used to train our model at: https://drive.google.com/drive/folders/1u6DDqnxUgWTlgHAeIW7bdt0CnYkCX6fT


## Outputs

### UI Design
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/UI.png" alt="UI">
</p>

### Interstellar Themed
<p align="center">
  <img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/f28b019e26e516377e438076a4150ffe45f2f7c7/images/2480%20x%203508%20(4).png" alt="Interstellar">
</p>

### Avengers Themed
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/aven2.png" alt="Avengers">
</p>

### Pokemon Themed
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/poki%20poki.jpg" alt="Pokemon">
</p>

### Ramayana Themed
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/ram.jpg" alt="Ramayana">
</p>

### Harry Potter Themed
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/HP.jpg " alt="Harry Potter">
</p>


## Tech Stack

*Languages and Frameworks*

| ![Python](https://img.shields.io/badge/Python-3.12-blue) | ![FASTAPI](https://img.shields.io/badge/FastAPI-0.83.2-brightgreen) | ![Streamlit](https://img.shields.io/badge/Streamlit-1.17.1-brightgreen) |
|:---:|:---:|:---:|

---

*Libraries and Tools*

| ![Hugging Face](https://img.shields.io/badge/Hugging_Face-v0.6.13-blue) | ![git](https://img.shields.io/badge/git-2.44.0-orange) | ![GitHub](https://img.shields.io/badge/github-latest-gray) |
|:---:|:---:|:---:|

---

*Functionalities*

| ![Image Manipulation](https://img.shields.io/badge/Image_Manipulation-experimental-orange) | ![Langchain](https://img.shields.io/badge/Langchain-experimental-orange) | |
|:---:|:---:|:---:|

















