# prompt_engineering.py
from langchain.prompts import PromptTemplate

skills_prompt = PromptTemplate(
    input_variables=["skills"],
    template="""Transform and optimize the following skills for ATS compatibility:

Skills: {skills}

Requirements:
1. Categorize skills logically (e.g., Programming Languages, Frameworks, Tools)
2. Include industry-standard variations of each skill
3. Order by relevance and expertise
4. Remove outdated skills

Output Format:
TECHNICAL SKILLS
[Category 1]
• Primary Skill 1 (+ variations)
• Primary Skill 2 (+ variations)

[Category 2]
• Primary Skill 3 (+ variations)
• Primary Skill 4 (+ variations)
"""
)

experience_prompt = PromptTemplate(
    input_variables=["role", "company", "description", "period"],
    template="""Optimize the following professional experience for ATS compatibility:

Role: {role}
Company: {company}
Description: {description}
Period: {period}

Requirements:
1. Start with strong action verbs
2. Include metrics and quantifiable results
3. Highlight technical skills used
4. Focus on achievements over responsibilities

Output Format:
[Company Name] | [Role] | [Period]
• [Action Verb] + [Project/Task] + [Technology] + [Quantifiable Result]
• [Action Verb] + [Achievement] + [Skills Used] + [Impact]
(3-5 bullets maximum)
"""
)

achievements_prompt = PromptTemplate(
    input_variables=["achievements"],
    template="""Enhance the following achievements for maximum impact:

Achievements: {achievements}

Requirements:
1. Use Challenge-Action-Result format
2. Quantify results where possible
3. Highlight leadership and initiative
4. Include technical context

Output Format:
KEY ACHIEVEMENTS
• [Achievement 1]: [Challenge] → [Action] → [Quantified Result]
• [Achievement 2]: [Challenge] → [Action] → [Quantified Result]
(2-4 achievements total)
"""
)


from langchain.prompts import PromptTemplate

# Define prompts for different sections
resume_prompt = PromptTemplate(
    input_variables=["skills", "experience", "achievements"],
    template="""Generate an ATS-compatible resume section.

Skills: {skills}
Experience: {experience}
Achievements: {achievements}

Formatted Resume Output:
"""
)

#Few Shot Prompting
resume_prompt = PromptTemplate(
    input_variables=["skills", "experience", "achievements"],
    template="""Generate an ATS-compatible resume section tailored for a software engineering role.

Example:
Skills: Python, Java, SQL
Experience: Developed a scalable backend system for a fintech startup.
Achievements: Reduced server costs by 20% through optimized database queries.

Formatted Resume Output:
- Proficient in Python, Java, and SQL.
- Developed a scalable backend system for a fintech startup, handling over 1M daily transactions.
- Reduced server costs by 20% by optimizing database queries.

Now generate a resume section for:
Skills: {skills}
Experience: {experience}
Achievements: {achievements}

Formatted Resume Output:
"""
)

#Role Assignment 
resume_prompt = PromptTemplate(
    input_variables=["skills", "experience", "achievements"],
    template="""You are a professional resume writer specializing in ATS-compatible resumes for software engineers. Generate a resume section based on the following details:

Skills: {skills}
Experience: {experience}
Achievements: {achievements}

Formatted Resume Output:
"""
)

#Constraints and Formatting
resume_prompt = PromptTemplate(
    input_variables=["skills", "experience", "achievements"],
    template="""Generate an ATS-compatible resume section tailored for a software engineering role.

Constraints:
- Use no more than 50 words.
- Format the output in bullet points.
- Start each bullet point with an action verb.

Skills: {skills}
Experience: {experience}
Achievements: {achievements}

Formatted Resume Output:
"""
)

#Iterative Refinement 
#Initial Prompt
resume_prompt = PromptTemplate(
    input_variables=["skills", "experience", "achievements"],
    template="""Generate a resume section.

Skills: {skills}
Experience: {experience}
Achievements: {achievements}

Formatted Resume Output:
"""
)

# Refined Prompt
resume_prompt = PromptTemplate(
    input_variables=["skills", "experience", "achievements"],
    template="""Generate an ATS-compatible resume section tailored for a software engineering role.

Skills: {skills}
Experience: {experience}
Achievements: {achievements}

Format the output in bullet points, starting with action verbs and quantifying achievements where possible.

Formatted Resume Output:
"""
)