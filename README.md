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

### 4️⃣ **Selecting the Certification Board**
![Certification_board](assets/certification_board_entered.png)  
_Selected the Certification board as CBFC (India)._

### 5️⃣ **Generating the story**
![Generating Story](assets/generating_story.png)  
_Story is getting Generated._

### 6️⃣ **Story generated**
![After the Output is Generated](assets/story_generated.png)  
_The story is generated._

### 7️⃣ **Suggested CBFC rating**
![Suggested_CBFC](assets/suggested_rating_CBFC.png)  
_CBFC (India) age rating also specified._

### 8️⃣ **Shifted to BBFC rating**
![Changed_BBFC](assets/changed_to_BBFC_board.png)  
_Now changed it to BBFC (UK) board._

### 9️⃣ **Suggested BBFC rating**
![Suggested_BBFC](assets/suggested_rating_BBFC.png)  
_BBFC (UK) age rating also specified without changing the story._

### 🔟 **Story Regenerate Button entered**
![regenerate](assets/regenerate_entered.png)  
_story is now regenerating._

### 1️⃣1️⃣ **Story Regenerated**
![regenerate](assets/story_regenerated.png)  
_story is regenerated._

### 1️⃣2️⃣ **Reset Button entered**
![clear_button](assets/clear_button_entered.png)  
_The prompt, genre, story and suggested rating are now cleared._


