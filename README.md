# 📚 StudyBBuddy AI – Smart Study Assistant

An AI-powered multi-domain assistant built with **Python, Streamlit, and Google's Gemini API**. StudyBBuddy AI helps users get information and assistance across three major domains: Education, Health Information, and Sustainability.

The project combines keyword-based domain classification with a Gemini-powered AI agent to provide relevant responses based on the user's questions.

## ✨ Features

- **Multi-Domain Assistance:** Supports Education, Health Information, and Sustainability.
- **Smart Domain Classification:** Automatically identifies the topic of a user's question using keyword-based classification.
- **Google Gemini Integration:** Uses Google's Gemini API to generate AI-powered responses.
- **Conversational Context:** Maintains chat history during the active application session.
- **Interactive Chat Interface:** Provides a simple and user-friendly interface using Streamlit.
- **Modular Architecture:** Separates domain classification, AI processing, and application logic into different Python modules.
- **Health Information Safety:** Provides general health information without making medical diagnoses.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini API | AI response generation |
| Google GenAI SDK | Gemini API integration |
| Streamlit | Interactive web interface |
| Python-dotenv | Environment variable management |

## 🏗️ Project Structure

```text
studyBBuddy-/
│
├── agent.py           # Gemini AI agent and prompt handling
├── app.py             # Streamlit application and chat interface
├── classifier.py      # Domain classification logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Git ignored files
├── LICENSE            # MIT License
└── README.md          # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Mousam-gift/studyBBuddy-.git
```

### 2. Navigate to the Project Directory

```bash
cd studyBBuddy-
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project root directory:

```env
Gemini_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual API key.

**Important:** Never upload your `.env` file or expose your API key on GitHub.

## 🚀 Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your default browser.

## 💡 How It Works

1. **User Input:** The user enters a question through the Streamlit interface.
2. **Domain Classification:** The classifier analyzes keywords in the question and identifies its domain.
3. **Smart Routing:** The classified domain is added to the user's message.
4. **AI Processing:** The Gemini-powered agent processes the question along with the available conversation history.
5. **Response Generation:** Gemini generates a relevant response and displays it in the chat interface.

## 📌 Supported Domains

| Domain | Example Questions |
|---|---|
| Education | Explain Python programming, help me prepare for exams. |
| Health Information | How can I improve my sleep schedule? |
| Sustainability | What are the benefits of recycling? |
| Mixed | Questions that do not match the predefined categories. |

## 🔮 Future Improvements

- Implement an ML-based domain classification model.
- Add document and PDF-based question answering.
- Introduce voice-based interaction.
- Improve conversation memory and context management.
- Add user authentication and personalized learning.
- Integrate additional AI models.
- Deploy the application to a cloud platform.

## ⚠️ Disclaimer

StudyBBuddy AI is an educational and informational assistant. It does not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical concerns.

## 👨‍💻 Developer

**Mousam Das**

B.Tech – Computer Science and Engineering (AI & ML)

- GitHub: [@Mousam-gift](https://github.com/Mousam-gift)
- Project Repository: [StudyBBuddy AI](https://github.com/Mousam-gift/studyBBuddy-)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

⭐ If you find this project useful, consider giving it a star on GitHub!
