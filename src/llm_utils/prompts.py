from langchain_core.prompts import ChatPromptTemplate


class Instruction:
    """
    @property: 
        Purpose:
            - It will return only the property of the class 
            - Cannot change are modify the property funciton. @func_name.setter to modify the attribute of the function 
        Technical:
            - Encapsulation
            - makes a method act like an attribute.
    """

    def __init__(self):
        self.prephaseInstruct =  ChatPromptTemplate.from_messages([("system","""you can prephrase it by converting the user spoken words into correct written English. For example, if the user says'I lik du rangutang,' you can prephrase it as 'I like orangutans.' As an assistan should focus on accurately prephrasing it. avoide any answer to the user quesiotn just prephase it
        Generate prephased context into JSON with this structure:
            {{
                "prephase_context":"I like orangutans."
            }}"""),
        ("user","{user_input}")])

    @property
    def prephase_prompt_instruciton(self):
        '''
        single-Short Prompting...
        '''
        return self.prephaseInstruct

    @property
    def grammer_prompt_instruction(self):
        return "Should check the grammatical mistake and poitout the the mistakes in the given sentence."
