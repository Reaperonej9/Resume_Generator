# resume_helper.py
def invoke_llm(llm, prompt_text):
    """
    Invokes the LLM with error handling
    """
    try:
        response = llm.invoke(prompt_text)
        return response if isinstance(response, str) else response.content
    except Exception as e:
        return f"Error: {str(e)}"
