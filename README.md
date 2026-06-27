# AI Recruiter Copilot

An AI-powered hiring assistant that helps recruiters and hiring managers evaluate multiple resumes against a job description, rank candidates, identify strengths and weaknesses, and generate interview questions automatically.

## ✨ Features

* 📄 Upload multiple resumes (PDF format)
* 🎯 Match candidates against a Job Description (JD)
* 🤖 AI-powered candidate evaluation using Mistral AI
* 📊 Automatic candidate ranking based on match score
* ✅ Strength analysis
* 🚩 Weakness and red flag detection
* 🎙️ Interview question generation
* ⚡ FastAPI backend with asynchronous processing
* 🖥️ Streamlit dashboard for recruiters

---

## 🏗️ Architecture

```text
Resume PDFs
      │
      ▼
Document Processing
      │
      ▼
Vector Database Storage
      │
      ▼
Mistral AI Evaluation Engine
      │
      ▼
Candidate Ranking & Insights
      │
      ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python
* AsyncIO
* Mistral AI API

### Frontend

* Streamlit

### Data Processing

* PDF Text Extraction
* Vector Database Storage
* Resume Parsing

---

## 📂 Project Structure

```text
AI recruiter/
│
├── backend/
│   ├── ai_agent.py
│   ├── document_processor.py
│   ├── vector_stores.py
│   ├── main.py
│   └── __init__.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── .env
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-recruiter-copilot.git
cd ai-recruiter-copilot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## 🚀 Running the Application

### Start Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

### Start Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

## 📖 How It Works

1. Upload one or more resumes.
2. Paste the target Job Description.
3. Click **Generate Hiring Report**.
4. AI evaluates each candidate.
5. Candidates are ranked based on job fit.
6. Detailed reports are generated including:

   * Match Score
   * Strengths
   * Weaknesses
   * Hiring Recommendation
   * Interview Questions

---

## 📸 Example Output

### Candidate Ranking

| Candidate  | Match Score | Recommendation |
| ---------- | ----------- | -------------- |
| John Doe   | 92%         | Strong Hire    |
| Jane Smith | 85%         | Hire           |
| Alex Brown | 68%         | Consider       |

### Detailed Insights

**Strengths**

* Strong Python experience
* Relevant AI/ML projects
* Industry experience

**Weaknesses**

* Limited leadership experience
* Missing cloud certifications

**Interview Questions**

* Explain your experience with FastAPI.
* Describe a challenging ML project.
* How do you evaluate model performance?

---

## 🎯 Use Cases

* Recruitment Agencies
* HR Teams
* Startup Hiring
* Technical Screening
* Campus Recruitment
* Talent Acquisition Teams

---

## 🔮 Future Improvements

* Resume-to-resume comparison
* ATS compatibility scoring
* Skill gap analysis
* Candidate chat interface
* Recruiter feedback loop
* Multi-agent evaluation workflow
* Export reports to PDF
* Job recommendation engine

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Aman Kumar**

If you found this project useful, consider giving it a ⭐ on GitHub.
