# CareerNav AI (Team Helios) 🚀

**CareerNav AI** is an advanced career guidance platform designed to empower students and professionals with AI-driven insights. By analyzing resumes, GitHub repositories, and LeetCode profiles, the platform provides personalized roadmaps, job market analysis, and skill verification to bridge the gap between education and industry requirements.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-green)
![Firebase](https://img.shields.io/badge/firebase-firestore-orange)

## 🌟 Key Features

### 🧠 AI-Powered Analysis
- **Resume & Certificate Parsing**: upload your resume or certificates to automatically extract skills and verify achievements using **EasyOCR** and **LLaMA** models.
- **Smart Career Roadmap**: Generates a step-by-step learning path tailored to your current skills and target role.
- **Market Insights**: Provides real-time analysis of job market trends, salary estimates, and booming roles based on your profile.

### 💻 Developer Profile Integration
- **GitHub Analysis**: Connects to your GitHub to analyze repositories, classify projects (Web, ML, IoT, etc.), and determine career readiness.
- **LeetCode Strategy**: Fetches your LeetCode problem stats to create a focused study plan and identify weak areas in data structures & algorithms.

### 🎓 Higher Education & Internships
- **University Recommender**: Suggests top global and domestic universities based on your profile and exam scores (GRE, IELTS, etc.), complete with admission probabilities.
- **Internship Portal**: Access a curated list of internships and job openings relevant to your tech stack.

### 🎮 Gamification & Engagement
- **Daily Bounties**: Solve daily technical challenges to earn XP and track your progress.
- **Skill Verification Quizzes**: Take AI-generated quizzes to validate your expertise in specific roles.
- **EduBot**: An interactive AI mentor that answers your career queries with context from your profile.

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Database**: Google Firebase (Firestore)
- **AI & LLM**: Meta LLaMA 3 (via OpenRouter API), Google Gemini (integrated libraries)
- **OCR**: EasyOCR (for text extraction from images/PDFs)
- **Frontend**: HTML5, CSS3, JavaScript (Jinja2 Templates)
- **Tools**: Git

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- A Firebase Service Account Key (`serviceAccountKey.json`)
- An OpenRouter API Key for AI features

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Yuvaneshv2007/Team-Helios.git
   cd Team-Helios
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Ensure you have `torch` installed if required by EasyOCR.*

3. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your keys:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   # Add other necessary keys like Firebase config if not using json file directly
   ```

4. **Firebase Setup**
   - Place your `serviceAccountKey.json` in the `app/` directory or update the initialization path in `models.py`.

5. **Run the Application**
   ```bash
   python app/app.py
   ```
   The application will start at `http://localhost:5000`.

## 📂 Project Structure

```
Team-Helios/
├── app/
│   ├── app.py             # Main Flask Application
│   ├── models.py          # Database Models (Firebase)
│   └── ...
├── templates/             # HTML Templates for frontend
│   ├── dashboard.html
│   ├── index.html
│   └── ...
├── static/                # CSS, JS, and Images
├── requirements.txt       # Python Dependencies
├── README.md              # Project Documentation
└── .env                   # Environment Variables
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Built with ❤️ by Team Helios*
