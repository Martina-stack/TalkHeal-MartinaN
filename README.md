<div align="center"><img src="/static_files/TalkHealLogo.png" style="width: 220px; height: 220px;" /></div>

# <div align="center">TALKHEAL</div>

## 🧠 Your AI-Powered Mental Health Companion

**TalkHeal** is an empathetic, intelligent, and interactive mental health support assistant built using **Python** and **Streamlit**. Designed with compassion and care at its core, it offers 24/7 support, emotional journaling, resource guidance, and AI-powered conversations powered by Google’s Gemini.

---

## ✨ Features

### 🗣️ Conversational AI Support

* Gemini-powered chatbot for mental health companionship
* Empathetic and encouraging tone—never clinical or diagnostic
* Smart conversation history with multi-threaded support
* **Chatbot personality tone selector**:  
  *Compassionate Listener*, *Motivating Coach*, *Wise Friend*, *Neutral Therapist*, *Mindfulness Guide*

### 📘 Resource & Crisis Help

* Emergency Help Button — instantly access local support via Google Maps
* International helpline directory and global mental health resources
* Mental health resource library with live search

### 🧪 Science-Backed Assessments

* Integrated **PsyToolkit**-verified mental health quizzes for self-evaluation

### 💖 Mood Tracking, Journaling & Insights

* Mood slider with five emotional states, detailed entries with notes and activities
* AI-assisted coping tips and micro-journaling with guided reflection prompts
* Interactive dashboard with mood history, trend analysis, and personalized insights based on emotional patterns

###🧘 Focus Sessions

* Customizable focus timers (5 min to custom durations) with calming audio (piano, nature, or silence)
* Includes visual breathing animation, motivational quotes, and session controls (pause/resume/end)

### 📌 Smart Prompts

* Instant-start suggestions like “Feeling overwhelmed” or “How to manage stress?”
* Direct conversion of journal thoughts into chatbot prompts

### 🎨 Themes & UI

* Multiple soothing themes: **Light**, **Calm Blue**, **Mint**, **Lavender**, **Pink**, and **Dark**
* 3D-inspired soft pink and magenta UI for a mentally soothing experience
* Smooth transitions and responsive design for mobile and desktop

---

## 🚀 Live Demo

### 🎯 **Experience TalkHeal live now!**  
🔗 [https://TalkHeal.streamlit.app](https://TalkHeal.streamlit.app)

---

## 📊 Project Stats

<div align="center">
<p>

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat)
![Visitors](https://api.visitorbadge.io/api/Visitors?path=eccentriccoder01%2FTalkHeal%20&countColor=%23263759&style=flat)
![GitHub Forks](https://img.shields.io/github/forks/eccentriccoder01/TalkHeal)
![GitHub Repo Stars](https://img.shields.io/github/stars/eccentriccoder01/TalkHeal)
![GitHub Contributors](https://img.shields.io/github/contributors/eccentriccoder01/TalkHeal)
![GitHub Last Commit](https://img.shields.io/github/last-commit/eccentriccoder01/TalkHeal)
![GitHub Repo Size](https://img.shields.io/github/repo-size/eccentriccoder01/TalkHeal)
![GitHub Total Lines](https://sloc.xyz/github/eccentriccoder01/TalkHeal)
![Github](https://img.shields.io/github/license/eccentriccoder01/TalkHeal)
![GitHub Issues](https://img.shields.io/github/issues/eccentriccoder01/TalkHeal)
![GitHub Closed Issues](https://img.shields.io/github/issues-closed-raw/eccentriccoder01/TalkHeal)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/eccentriccoder01/TalkHeal)
![GitHub Closed Pull Requests](https://img.shields.io/github/issues-pr-closed/eccentriccoder01/TalkHeal)

</p>
</div>

---

> 💡 **PRs Welcome!** We love contributions. Check out the [Contribution Guidelines](CONTRIBUTING.md) to get started.

## 📸 Screenshots

<div align="center">
  <img src="static_files/light_ss.jpg" alt="Main Screenshot" width="600"/>
  <br>
  <img src="static_files/dark_ss.jpg" width="200"/></a>
  <img src="static_files/blue_ss.jpg" width="200"/></a>
  <img src="static_files/lav_ss.jpg" width="200"/></a>
</div>

## 📺 Video Explanation

For a detailed walkthrough of TalkHeal's features and how to use them, check out this video:

**[Insert YouTube Video Link Here]**

---

## 📁 Project Structure

```bash
TalkHeal/
├── .devcontainer/               # Dev container configuration (for VS Code)
├── .github/                     # GitHub workflows and issue templates
├── .streamlit/
│   └── secrets.toml             # Streamlit secrets (API keys, credentials)
├── assets/
│   ├── pink.png
│   └── yoga_animation.json
├── audio/
├── audio_files/
├── auth/
│   ├── auth_utils.py            # Authentication functions (login, register)
│   └── users.yaml               # User credentials and roles (YAML format)
├── components/
│   ├── Breathing_Exercise.py
│   ├── __init__.py
│   ├── chat_interface.py
│   ├── emergency_page.py
│   ├── focus_session.py
│   ├── header.py
│   ├── login_page.py
│   ├── mood_dashboard.py
│   ├── profile.py
│   ├── sidebar.py
│   └── theme_toggle.py
├── core/
│   ├── __init__.py
│   ├── config.py                # Central app configuration
│   ├── theme.py
│   └── utils.py                 # Common helper functions
├── css/
│   └── styles.py
├── data/
│   └── Yoga.json                # Yoga session data (poses, flows)
├── favicon/
│   ├── apple-touch-icon.png
│   ├── favicon-96x96.png
│   ├── favicon.ico
│   ├── favicon.svg
│   ├── site.webmanifest
│   ├── web-app-manifest-192x192.png
│   └── web-app-manifest-512x512.png
├── pages/
│   ├── About.py
│   ├── Journaling.py           # Journaling UI page
│   ├── Yoga.py                 # Yoga activity page
│   └── selfHelpTools.py        # Tools/resources for self-help
├── .gitignore                   # Files/folders ignored by Git
├── Background.jpg
├── Background_Dark.jpg
├── CODE_OF_CONDUCT.md          # Contribution behavior guidelines
├── CONTRIBUTING.md             # Instructions for contributing
├── LICENSE                     # License for the project (e.g., MIT)
├── MOOD_TRACKING_README.md     # Info about the mood tracking feature
├── README.md                   # Main project documentation
├── TalkHeal.pptx               # Presentation for TalkHeal
├── TalkHeal.py                 # 🔷 Main app entry point (Streamlit)
├── TalkHealLogo.png
├── blue.png
├── blue_ss.jpg
├── dark.png
├── dark_ss.jpg
├── generate_audio.py           # Script to convert text to speech/audio
├── journals.db                 # Database of user journal entries
├── lav_ss.jpg
├── lavender.png
├── light_ss.jpg
├── mint.png
├── requirements.txt            # Python package dependencies
├── streamlit.toml              # Streamlit configuration
├── test_mood_dashboard.py      # Test cases for mood dashboard
└── users.db                    # Database for user authentication

```
---


## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=61DAFB)
![CSS](https://img.shields.io/badge/CSS-38B2AC?style=for-the-badge&logo=css&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-4EA94B?style=for-the-badge&logo=sqlite&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-3448C5?style=for-the-badge&logo=google&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-0099FF?style=for-the-badge&logo=streamlit&logoColor=white)

---

## ⚙️ Installation and Setup

> Clone and run locally using Python and Streamlit.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/eccentriccoder01/TalkHeal.git
   cd TalkHeal
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API key:**
   Go to your Streamlit [Secrets Settings](https://streamlit.io/cloud) and add:

   ```toml
   [gemini]
   api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
   ```

4. **Run the app:**

   ```bash
   streamlit run TalkHeal.py
   ```

---

## Issue Creation ✴
Report bugs and  issues or propose improvements through our GitHub repository.

## Contribution Guidelines 📑

- Firstly Star(⭐) the Repository
- Fork the Repository and create a new branch for any updates/changes/issue you are working on.
- Start Coding and do changes.
- Commit your changes
- Create a Pull Request which will be reviewed and suggestions would be added to improve it.
- Add Screenshots and updated website links to help us understand what changes is all about.

- Check the [CONTRIBUTING.md](CONTRIBUTING.md) for detailed steps...
    
## Contributing is fun🧡

We welcome all contributions and suggestions!
Whether it's a new feature, design improvement, or a bug fix — your voice matters 💜

Your insights are invaluable to us. Reach out to us team for any inquiries, feedback, or concerns.

## 👥 Contributors

Thanks to these wonderful people for contributing 💖

[![Contributors](https://contrib.rocks/image?repo=eccentriccoder01/TalkHeal)](https://github.com/eccentriccoder01/TalkHeal/graphs/contributors)

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 📞 Contact

Developed by [Eccentric Explorer](https://eccentriccoder01.github.io/Me)

Feel free to reach out with any questions or feedback\!
