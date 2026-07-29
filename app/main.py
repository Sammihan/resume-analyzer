from services.analyzer_service import analyze_resume_against_jd

resume_pdf = "resume/sample_resume.pdf"
jd_pdf = "resume/sample_job_description.pdf"

result = analyze_resume_against_jd(resume_pdf, jd_pdf)

print(f"Semantic Match: {result['semantic_match']:.2f}%")

print("\nMissing Skills")
print("----------------")
for skill in result["missing_skills"]:
    print(f"- {skill}")

print("\nAI Suggestions")
print("----------------")
print(result["suggestions"])

from report.pdf_generator import generate_pdf_report

pdf_path = generate_pdf_report(result)

print(f"\nPDF Generated Successfully: {pdf_path}")
