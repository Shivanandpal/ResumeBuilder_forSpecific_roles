import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load data
data = pd.read_csv("dataset.csv")

# Combine company + role
data["input"] = data["job_title"] + " " + data["category"]

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["input"])

# Train model
model = NearestNeighbors(n_neighbors=1)
model.fit(X)

def predict_skills(job_role, company):
    query = job_role + " " + company
    vec = vectorizer.transform([query])
    _, idx = model.kneighbors(vec)
    skills = data.iloc[idx[0][0]]["job_skill_set"]
    return skills.split(",")

# PROJECT PREDICTION FUNCTION

def predict_projects(role, company):
    query = role + " " + company
    vec = vectorizer.transform([query])
    _, idx = model.kneighbors(vec)

    projects = []

    # Generate dummy projects based on role
    for i in idx[0]:
        job = data.iloc[i]["job_title"]

        projects.append({
            "title": f"{job} Project",
            "desc": f"Developed a {job.lower()} related solution using relevant tools and technologies."
        })

    return projects