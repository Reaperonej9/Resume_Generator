# skills_achievements.py
from langchain.schema import HumanMessage, SystemMessage

def construct_prompt_skills_achievements(data):
    """
    Constructs a prompt for skills and achievements optimization
    """
    # Convert data to structured string
    data_text = f"""
Name: {data.get('Name', 'NaN')}
Skills: {data.get('Skills', 'NaN')}

Experience:
{format_experience(data.get('Experience', []))}

Achievements:
{format_achievements(data.get('Achievements', []))}
"""

    system_message = SystemMessage(
        content="""You are an expert resume assistant. Optimize the provided information for:
1. ATS compatibility
2. Clear and impactful presentation
3. Quantifiable achievements
4. Technical accuracy
5. Professional formatting"""
    )

    human_message = HumanMessage(
        content=f"Please optimize this resume information:\n{data_text}"
    )

    return [system_message, human_message]

def format_experience(experience_list):
    return "\n".join([
        f"- Role: {exp.get('Role', 'NaN')}, "
        f"Company: {exp.get('Company', 'NaN')}, "
        f"Description: {exp.get('Description', 'NaN')}, "
        f"Period: {exp.get('Period', 'NaN')}"
        for exp in experience_list
    ])

def format_achievements(achievements_list):
    return "\n".join([f"- {achievement}" for achievement in achievements_list])