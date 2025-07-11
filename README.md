# StoryCraft : AI Story Teller

An AI-powered story generator that brings your imagination to life. Create unique stories by combining genres and get suggested age ratings based on international certification boards.

<img src="./assets/logo.png" alt="StoryCraft Logo" width="200"/>

---

### ✨ Features

- **AI Story Generation:** Uses Google's Gemini API to write unique stories based on your topic.
- **Multi-Genre Blending:** Select multiple genres (e.g., Sci-Fi + Horror) to create interesting narrative mashups.
- **International Age Ratings:** Get suggested age ratings for your story based on MPA (USA), CBFC (India), and BBFC (UK) guidelines.
- **Dynamic UI:** A clean, modern, and responsive interface built with HTML, CSS, and vanilla JavaScript.
- **Live Re-certification:** Instantly get a new rating by switching certification boards without regenerating the story.

### 💻 Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python (Flask)
- **AI Model:** Google Gemini API

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### Installation & Local Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/BurraRohan/StoryCraft_The_AI_Story_Generator_V2.git](https://github.com/BurraRohan/StoryCraft_The_AI_Story_Generator_V2.git)
    cd StoryCraft
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create an environment file:**
    Create a file named `.env` in the main project folder.

4.  **Add your API Key:**
    Inside the `.env` file, add your Gemini API key like this:
    ```
    GEMINI_API_KEY="YOUR_OWN_API_KEY_HERE"
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```
    Your server will start on `http://127.0.0.1:5000`.

6.  **View the app:**
    Open the `index.html` file directly in your web browser.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📸 **Demo Images**

### 1️⃣ **Interface After Code Execution**
![Interface After Code Execution](assets/landing_page.png)  
_The interface displayed after executing the AI Story Generator._

### 2️⃣ **Adding the prompt**
![Adding the Prompt](assets/prompt_entered.png)  
_The user interface showing the input field where the prompt is added._

### 3️⃣ **Adding the genre**
![Adding the Genre(s)](assets/genres_entered.png)  
_The user interface showing the input field where the genre(s) is added._

### 4️⃣ **During the Generation Phase**
![During the Generation Phase](assets/during_generation.png)  
_Screenshot showing the application during the text generation phase._

### 5️⃣ **After the Output is Generated**
![After the Output is Generated](assets/output_generated.png)  
_The output displayed after the AI generates the story from the prompt._

### 6️⃣ **After the reset button is hit**
![After the Output is Generated](assets/interface_after_execution.png)  
_The interface is reset after the reset button is hit._




