from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from llm_setup import initialize_llm  # Import the LLM initialization function

# Define the evaluation prompt globally
evaluation_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""Evaluate the following resume sections for ATS compatibility and effectiveness:

Resume Text: {resume_text}

Provide ratings and feedback in the following areas:
1. ATS Optimization (1-10):
   - Keyword usage and placement
   - Industry-standard terminology
   - Formatting compatibility

2. Content Impact (1-10):
   - Quantifiable achievements
   - Action verbs
   - Technical detail accuracy

3. Structure & Clarity (1-10):
   - Section organization
   - Bullet point effectiveness
   - Information hierarchy

Overall Score:
Improvement Suggestions:
"""
)

class ResumeEvaluator:
    def __init__(self, llm=None):
        """Initialize ResumeEvaluator with an LLM instance. If none is provided, initialize one."""
        self.llm = llm if llm else initialize_llm()
        self.evaluator_chain = LLMChain(llm=self.llm, prompt=evaluation_prompt)

    def evaluate_resume(self, resume_text):
        """Evaluates a resume using the LLM."""
        return self.evaluator_chain.run(resume_text=resume_text)

# Function to allow direct evaluation without instantiating ResumeEvaluator
def evaluate_resume(resume_text):
    """Creates a temporary ResumeEvaluator instance and evaluates the resume."""
    evaluator = ResumeEvaluator()
    return evaluator.evaluate_resume(resume_text)




