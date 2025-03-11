#from llm_setup import llm
from prompt_engineering import resume_prompt
from evaluation import evaluate_resume


# Define sample data for skills, experience, and achievements
skills = "Python, Machine Learning, Data Analysis"
experience = "Data Scientist at XYZ Corp (2020-2023)"
achievements = "Won Hackathon 2022, Published Research Paper in 2021"

# Step 1: Generate the resume
resume_text = resume_prompt.format(skills=skills, experience=experience, achievements=achievements)
print("Generated Resume:\n")
print(resume_text)

# Step 2: Evaluate the resume
score = evaluate_resume(resume_text)
print("\nResume Evaluation Score:")
print(score)

from llm_setup import initialize_llm
from prompt_engineering import skills_prompt, experience_prompt, achievements_prompt
from evaluation import ResumeEvaluator
from resume_helper import invoke_llm
from skills_achievements import construct_prompt_skills_achievements

def main():
    # Initialize LLM
    llm = initialize_llm()
    evaluator = ResumeEvaluator(llm)

    # Sample data
    skills_achievements_data = {
        "Name": "John Doe",
        "Skills": "Python, Machine Learning, SQL, Data Analysis",
        "Experience": [
            {
                "Role": "Data Scientist",
                "Company": "XYZ Corp",
                "Description": "Worked on machine learning models for predictive analytics.",
                "Period": "Jan 2020 - Present"
            },
            {
                "Role": "Research Assistant",
                "Company": "University of ABC",
                "Description": "Published research paper on data analysis techniques.",
                "Period": "Aug 2018 - Dec 2019"
            }
        ],
        "Achievements": [
            "Won Hackathon 2022",
            "Presented at IEEE Conference 2021"
        ]
    }

    try:
        # Process skills section
        skills_text = skills_prompt.format(skills=skills_achievements_data["Skills"])
        skills_response = invoke_llm(llm, skills_text)

        # Process experience section
        experience_sections = []
        for exp in skills_achievements_data["Experience"]:
            exp_text = experience_prompt.format(
                role=exp["Role"],
                company=exp["Company"],
                description=exp["Description"],
                period=exp["Period"]
            )
            experience_sections.append(invoke_llm(llm, exp_text))

        # Process achievements section
        achievements_text = achievements_prompt.format(
            achievements=", ".join(skills_achievements_data["Achievements"])
        )
        achievements_response = invoke_llm(llm, achievements_text)

        # Combine all sections
        complete_resume = f"""
{skills_response}

PROFESSIONAL EXPERIENCE
{"\n".join(experience_sections)}

{achievements_response}
"""

        # Evaluate the complete resume
        evaluation = evaluator.evaluate_resume(complete_resume)

        # Print results
        print("\nOptimized Resume:")
        print(complete_resume)
        print("\nEvaluation:")
        print(evaluation)

    except Exception as e:
        print(f"Error processing resume: {str(e)}")

if __name__ == "__main__":
    main()
           
     
