from langchain.schema import HumanMessage, SystemMessage

def construct_prompt(education_data):
    """
    Constructs a prompt for the LLM to refine education data.
    
    Parameters:
        education_data (pd.DataFrame): The education data read from a CSV file.

    Returns:
        List[BaseMessage]: A list of messages formatted for the LLM.
    """
    # Convert the DataFrame to a string
    education_text = education_data.to_string(index=False)

    # Define system and human messages
    system_message = SystemMessage(
        content="You are an assistant that checks a candidate's resume education information. "
                "Your task is to check for errors in spelling, and conflicts in the educational timeline. "
                "For University field, check if the university exists. "
                "For Major field, check the spellings. Also, if the candidate has already gained the Bachelor degree, then later period shouldn't appear any Bachelor degree. "
                "For Period field, the time shouldn't overlap."
                "For the combination of Period and Degree field, the bachelor degree should be pursued before master degree. And it's common to have more than 1 master degree or more than 1 bachelor degree. "
                "For Honor field, it is ok that the honor part or the course part is empty. But if the line has honor or course field, do not change it. "
                "For Course field, check if they are related to that line's major. "
                "As long as the name fields are same, this means these lines of education all belongs to one person. "
                "When you print the correct output, put 'NaN' into the block if it's empty. "
                "Here is an example of Corrected DataFrame you need to follow: "
                "| number | Name                       | University                       | Major           | Degree   | GPA   | Period               | Course       |Honor                                                                            |"
                "|--------|----------------------------|----------------------------------|-----------------|----------|-------|----------------------|--------------|--------------------------------------------------------------------|"
                "| 1      | Muqi Zhang                 | Beijing University of Technology | Applied Physics | Bachelor | 3.89  | Sep 2014 - July 2018 |              | Scholarship for Outstanding Academic Performance (2014/2015, 2015/2016, 2016/2017)|"
    )
    human_message = HumanMessage(
        content=f"Here is the raw data:\n{education_text}\n\nPlease review it and point out any errors or inconsistencies. And generate the correct sentences. "
    )

    return [system_message, human_message]


def invoke_llm(llm, messages):
    """
    Sends messages to the LLM and retrieves its response.

    Parameters:
        llm (ChatOpenAI): The initialized LLM instance.
        messages (List[BaseMessage]): The messages to send to the LLM.

    Returns:
        str: The content of the LLM's response.
    """
    response = llm.invoke(messages)
    return response.content


