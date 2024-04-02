<!--
<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/WhatsApp%20Image%202024-03-26%20at%2021.01.47_a572f875.jpg?raw=true" alt="Logo">
</p> -->

<div align="center">
  <a href="https://github.com/OpenDevin/OpenDevin/graphs/contributors"><img src="https://img.shields.io/badge/CONTRIBUTORS-4-6cf542" alt="Contributors"></a>
  <a href="https://github.com/OpenDevin/OpenDevin/network/members"><img src="https://img.shields.io/badge/COMMITS-100+-blue" alt="Forks"></a>
  <a href="https://github.com/OpenDevin/OpenDevin/stargazers"><img src="https://img.shields.io/badge/STARS-3-blue" alt="Stargazers"></a>
  <a href="https://github.com/OpenDevin/OpenDevin/issues"><img src="https://img.shields.io/badge/CLONED-54+ TIMES-efca08" alt="Issues"></a>
  <a href="https://github.com/OpenDevin/OpenDevin/blob/main/LICENSE"><img src="https://img.shields.io/badge/LICENSE-MIT-6cf542" alt="MIT License"></a>
</div>


<!-- PROJECT LOGO -->
<div align="center">
  <img src="./images/logo.png" alt="Logo" width="200" height="200">
  <h1 align="center">Comic-ify: Making Learning Fun, Forever</h1>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>🗂️ Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">🐚 About Comic-ify</a>
      <ul>
        <li><a href="#features">⭐️ Features</a></li>
        <li><a href="#vision">🔮 Vision</a></li>
      </ul>
    </li>
    <li>
      <a href="#workflow">🌈 Workflow Diagram</a>
    </li>
    <li>
      <a href="#get-started">🚀 Get Started</a>
      <ul>
        <li><a href="#1-build-and-setup">1. Build and Setup</a></li>
        <li><a href="#2-run-the-application">2. Running FastAPI</a></li>
      </ul>
    </li>
    <li>
      <a href="#intel">⚡ Intel OneAPI Tools</a>
    </li>
    <li><a href="#outputs">🛸 Outputs</a></li>
    <li><a href="#project-status">🚧 Project Status</a></li>
    <li><a href="#community">🤖 Meet us!</a></li>
    
    <li><a href="#research-strategy">⭐️ Research Strategy</a></li>
    <li><a href="#how-to-contribute">🤝 How to Contribute</a></li>
    <li><a href="#built-with">🛠️ Built With</a></li>

    <li><a href="#license">📜 License</a></li>
  </ol>
</details>



## 🎯 Mission

[Project Demo Video](https://github.com/S0L009/COMIC-IFY_OneAPI/assets/121689231/530288cc-1c34-49cd-b62e-da7d25921d5f)

Welcome to Comic-ify, a revolutionary application fueled by cutting-edge LLM-based technology. Simply upload your mundane PDF, and prepare to be dazzled as it metamorphoses into a visually stunning comic-style masterpiece! Say goodbye to drowning in endless paragraphs and hello to a world where information leaps off the page, guiding you to your rightful destination in the most captivating way possible! Get ready to redefine your reading experience – Comic-ify is here to elevate it to unprecedented heights!






## 🐚 About Comic-ify
Comic-ify is not just another tool. It's a revolution in how we consume information. Imagine this: you have a stack of boring PDFs, full of dense text that drains your energy just thinking about it. We've all been there. But fear not! Comic-ify is here to transform your reading experience. Let's face it, deciphering pages of dull, overwhelming text is like trying to climb a mountain without a rope. It's tough, it's exhausting, and frankly, it's no fun at all. We've experienced this struggle since our early days, constantly grappling with the challenge of making tedious content engaging.

## ⭐️ Features
Lexicon, our fine-tuned model is employed to generate imaginative text and produce images inspired by the text. captivating readers as they explore the content

- **Input as prompt or PDF**
Displays modified text/images for prompts, generates a downloadable PDF for PDF input.

- **Theme-based generation**
Users can choose predefined themes. For example, in the 'Indian Mythology' theme, Lord Vishnu could provide insights into the mysteries of black holes in the universe.

- **Highlight User’s Prefered topics**
Example: If the emphasis is on Operating Systems, users can prompt for a detailed explanation of how system calls work, directing the explanation accordingly.



## 🔮 Vision: Transforming Content Consumption

Comic-ify is revolutionizing how we engage with information. Powered by cutting-edge LLM-based models, our tool effortlessly converts dense PDFs into visually engaging comic-style content. Say goodbye to tedious paragraphs and hello to an immersive experience where information comes to life! Why Comic-ify? Because we believe knowledge should be accessible and enjoyable. With Comic-ify, understanding content becomes effortless, and the process becomes a pleasure. It's a win-win for all.



## 🌈 Workflow Diagram

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




## 🚀 Get Started

### 1. Build and Setup
Clone the Comic-ify repository to your local machine using the following command:
```bash
git clone https://github.com/S0L009/COMIC-IFY_OneAPI.git
```
### 2. Running the Fast API
Run the FastAPI server locally to enable all endpoints

Step1: Install the FastAPI directory from the repository and navigate into it in your terminal

Step2: Install all necessary dependencies
```bash
pip install -r requirements.txt
```

Step3: Run the uvicorn ASGI server to get the endpoints functional
```bash
uvicorn main:app --reload
```
Step4: Test the APIs on Swagger-UI (your app should look like this)

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


## 🚧 Project Status
Comicify is currently under active development, but you can already experience its early capabilities by running the alpha version. Our dedicated team is diligently working on achieving the following key milestones:

- **Expanding Templates and Themes**: We're dedicated to enriching the Comicify experience by adding more templates and themes for the output. These new designs will offer users a wider range of options to customize their comic-style content, ensuring greater flexibility and creativity in transforming text-heavy materials.

- **Scaling the Product**: As Comicify gains momentum, we're focusing on scaling the product to accommodate growing demand and usage. This involves optimizing performance, enhancing scalability, and ensuring seamless user experiences even as our user base expands.

- **Innovative Feature Research**: Our team is actively researching new and innovative features that align with our mission of making content consumption enjoyable. From interactive elements to gamification features, we're exploring ways to infuse Comicify with engaging functionalities that enhance user engagement and retention.

- **Continuous Improvement**: Beyond adding new features, we're committed to continuously improving Comicify based on user feedback and emerging trends. This includes refining existing features, optimizing workflows, and addressing any issues or pain points identified by our users.

As we continue to evolve Comicify, our goal remains clear: to revolutionize the way people consume and interact with information by making content fun, engaging, and visually appealing. 



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


## 🤖 Join Our Community

<p align="center">
  <img src="https://github.com/SrikarVamsi/dump/blob/main/amrita_logo.png" alt="Amrita Vishwa Vidyapeetham Logo">
</p>

Meet the talented minds behind Comic-ify, all hailing from Amrita Vishwa Vidyapeetham's AI branch:

**<p align="center">Surya</p>**
   <p align="center">
     <img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/main/Streamlit/surya.jpg" alt="Surya's Picture" width="150">
   </p>
   <p align="center">
     <a href="https://www.linkedin.com/in/surya-santhosh-64a08b297/">
       <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
     </a>
     <a href="https://www.instagram.com/ss.surya.ss/">
       <img src="https://img.shields.io/badge/Instagram-Follow-red?style=flat-square&logo=instagram" alt="Instagram">
     </a>
   </p>

**<p align="center">Amrit</p>**
   <p align="center">
     <img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/main/Streamlit/amrith.jpg" alt="Amrit's Picture" width="150">
   </p>
   <p align="center">
     <a href="https://www.linkedin.com/in/macromrit/">
       <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
     </a>
     <a href="https://www.instagram.com/amritsubramanian.c/">
       <img src="https://img.shields.io/badge/Instagram-Follow-red?style=flat-square&logo=instagram" alt="Instagram">
     </a>
   </p>

**<p align="center">Navneet</p>**
   <p align="center">
     <img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/main/Streamlit/me.jpg" alt="Navneet's Picture" width="150">
   </p>
   <p align="center">
     <a href="https://www.linkedin.com/in/navneet-krishna-669000279/">
       <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
     </a>
     <a href="https://www.instagram.com/krri__shh/">
       <img src="https://img.shields.io/badge/Instagram-Follow-red?style=flat-square&logo=instagram" alt="Instagram">
     </a>
   </p>

**<p align="center">Srikar</p>**
   <p align="center">
     <img src="https://github.com/S0L009/COMIC-IFY_OneAPI/blob/main/Streamlit/srikar.jpg" alt="Srikar's Picture" width="150">
   </p>
   <p align="center">
     <a href="https://www.linkedin.com/in/kottakki-srikar-vamsi/">
       <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
     </a>
     <a href="https://www.instagram.com/srikarvamsi1230/">
       <img src="https://img.shields.io/badge/Instagram-Follow-red?style=flat-square&logo=instagram" alt="Instagram">
     </a>
   </p>

**<p align="center">Kavya</p>**
   <p align="center">
     <img src="https://github.com/SrikarVamsi/dump/blob/main/kav.jpg" alt="Kavya's Picture" width="150">
   </p>
   <p align="center">
     <a href="https://www.linkedin.com/in/kavya-sakthivel/">
       <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
     </a>
     <a href="https://www.instagram.com/kaavyaa04/">
       <img src="https://img.shields.io/badge/Instagram-Follow-red?style=flat-square&logo=instagram" alt="Instagram">
     </a>
   </p>
   
   **(Note: Kavya has not participated in the hackathon but has been an integral part of the project.)**

## Future Developments

We envision several exciting future features for Comic-ify, including:

- Integration with educational platforms to enhance learning experiences.
- Multilingual support for catering to a diverse audience.
- Implementation of accessibility features for users with different needs.
- Community functionalities to foster collaboration and user engagement.

## Contributing to Comic-ify

If you're passionate about improving information consumption and want to contribute to Comic-ify, here's how you can get started:

1. Fork the Comic-ify repository on GitHub.
2. Make your desired changes or enhancements.
3. Submit a pull request detailing your modifications.
4. Collaborate with our team to review and integrate your contributions.

We welcome contributions from developers, designers, and enthusiasts alike!

## Conclusion

Comic-ify represents a paradigm shift in how we interact with textual information. By transforming dense content into visually engaging comics, we aim to make learning a delightful experience for everyone. Join us in this journey of innovation and empowerment!
