# StoryCraft : AI Story Teller (V2)

An AI-powered story generator that brings your imagination to life. Create unique stories by combining genres and get suggested age ratings based on international certification boards.

![StoryCraft Screenshot](./screenshot.png)
*(Suggestion: Add a screenshot of your running application and name it `screenshot.png`)*

---

### ✨ Features

- **AI Story Generation:** Uses Google's Gemini API to write unique stories based on your topic.
- **Multi-Genre Blending:** Select multiple genres (e.g., Sci-Fi + Horror) to create interesting narrative mashups.
- **International Age Ratings:** Get suggested age ratings for your story based on MPA (USA), CBFC (India), and BBFC (UK) guidelines.
- **Dynamic UI:** A clean, modern, and responsive interface built with HTML, CSS, and vanilla JavaScript.
- **Live Re-certification:** Instantly get a new rating by switching certification boards without regenerating the story.

### 💻 Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python with Flask
- **AI Model:** Google Gemini API
- **Deployment:** Gunicorn, Render

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### Installation & Local Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/StoryCraft.git](https://github.com/your-username/StoryCraft.git)
    cd StoryCraft
    ```
    *(Remember to replace `your-username` with your actual GitHub username!)*

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

## 🌐 Deployment

This project is configured for easy deployment on a service like Render.

1.  Push your project to a GitHub repository (ensure your `.env` file is listed in `.gitignore` and is not uploaded).
2.  On Render, create a new "Web Service" and connect it to your repository.
3.  Use the following settings:
    - **Runtime:** `Python 3`
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `gunicorn app:app`
4.  Add your `GEMINI_API_KEY` as an Environment Variable in the Render dashboard.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
