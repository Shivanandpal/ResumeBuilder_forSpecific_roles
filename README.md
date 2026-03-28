# 🚀 AI Resume Builder

An AI-powered resume builder that generates **ATS-friendly, professional resumes** based on job role and user input.
This project intelligently predicts relevant skills and formats resumes with a clean, modern layout.

---

## ✨ Features

* 🤖 **AI Skill Prediction** based on job role & company
* 📄 **Professional Resume Layout** (sidebar + sections)
* 🧠 **Auto Summary Generation**
* 📌 **Bullet Formatting** for Education & Experience
* 🧾 **User-Controlled Experience Input**
* 📥 **Download Resume as PDF**
* 🎯 ATS-friendly structure

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* PDFKit (wkhtmltopdf)

---

## 📁 Project Structure

```
resume_builder/
│
├── app.py                 # Streamlit UI
├── model.py               # Skill prediction model
├── utils.py               # Resume + PDF generation
├── template.html          # Resume design template
├── dataset.csv            # Job & skill dataset
├── projects_dataset.csv   # Project suggestions
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shivanandpal/ResumeBuilder_forDpecific.git
cd ResumeBuilder_forDpecific
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install wkhtmltopdf (IMPORTANT)

This project uses **wkhtmltopdf** for PDF generation.

👉 Download from:
https://wkhtmltopdf.org/downloads.html

After installation, ensure the path is set in `utils.py`:

```python
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters:

   * Personal details
   * Job role & company
   * Education & experience

2. System:

   * Predicts relevant skills using ML
   * Formats resume content
   * Generates a professional PDF

---

## 📸 Output

* Clean header with name & role
* Sidebar with details & skills
* Sections for:

  * Summary
  * Experience
  * Projects
  * Education

---

## 🚀 Future Improvements

* 🌐 Deploy online (public access)
* 📊 ATS score checker
* 🎨 Multiple resume templates
* 🖼 Profile photo support
* ⭐ Skill rating bars
* 🤖 Advanced AI summary generation

---

## 👨‍💻 Author

**Shivanand Pal**

---

## ⭐ Contribute

Feel free to fork this repo, improve features, and submit pull requests!

---

## 📌 Note

* `wkhtmltopdf` is required for PDF generation
* Make sure it is properly installed and configured

---

## 💡 Inspiration

This project was built to simplify resume creation using AI and help users generate job-ready resumes quickly.

---
