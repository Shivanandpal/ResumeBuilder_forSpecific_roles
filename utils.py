import pdfkit

# ✅ KEEP THIS (for preview)
def generate_resume(data, skills, projects):
    project_section = ""
    
    for p in projects:
        project_section += f"""
- {p['title']}
  {p['desc']}
"""

    resume = f"""
{data['name'].upper()}
Email: {data['email']} | Phone: {data['phone']}

----------------------------------------

OBJECTIVE
Seeking a position as {data['role']} at {data['company']}.

----------------------------------------

EDUCATION
{data['education']}

----------------------------------------

SKILLS
{', '.join(skills)}

----------------------------------------

PROJECTS
{project_section}

----------------------------------------
"""
    return resume


def format_bullets(text):
    lines = text.split("\n")
    html = ""

    for line in lines:
        line = line.strip()
        if line:
            html += f"<li>{line}</li>"

    return f"<ul>{html}</ul>"

def generate_summary(data, skills):
    # Take top 3–5 skills
    top_skills = ", ".join(skills[:5])

    # Take first experience line
    exp_lines = data["experience"].split("\n")
    first_exp = exp_lines[0] if exp_lines else ""

    summary = f"""
    Motivated {data['role']} with strong knowledge in {top_skills}.
    {first_exp}.
    Completed {data['education'].splitlines()[0]} and eager to contribute effectively at {data['company']}.
    """

    return summary.strip()

# 🔥 REPLACE THIS FUNCTION ONLY
def create_pdf(data, skills, projects):

    # ✅ Skills (clean)
    skills_html = "".join([f"<li>{str(s).strip()}</li>" for s in skills])

    # ✅ Projects
    projects_html = ""
    for p in projects:
        projects_html += f"""
        <div class="project">
            <b>{p['title']}</b><br>
            {p['desc']}
        </div>
        """

    # ✅ Experience → bullets
    experience_html = format_bullets(data["experience"])

    # ✅ Education → bullets
    education_html = format_bullets(data["education"])

    # Load template
    with open("template.html", "r", encoding="utf-8") as f:
        html = f.read()

    summary_text = generate_summary(data, skills)
    summary_html = f"<p>{summary_text}</p>"

    # Replace placeholders
    html = html.replace("{{name}}", data["name"])
    html = html.replace("{{role}}", data["role"])
    html = html.replace("{{email}}", data["email"])
    html = html.replace("{{phone}}", data["phone"])
    html = html.replace("{{address}}", data["address"])
    html = html.replace("{{skills}}", skills_html)
    html = html.replace("{{projects}}", projects_html)
    html = html.replace("{{experience}}", experience_html)
    html = html.replace("{{education}}", education_html)
    html = html.replace("{{summary}}", summary_html)

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    )

    pdfkit.from_string(
        html,
        "resume.pdf",
        configuration=config,
        options={"enable-local-file-access": ""}
    )

    return "resume.pdf"