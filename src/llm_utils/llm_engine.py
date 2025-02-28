import os
from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from dataclasses import field, dataclass
from src.llm_utils.Exception.validator import Not_none
from typing import Annotated
from src.llm_utils.prompts import Instruction
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import functools
load_dotenv()

#Load Environment Variable.
llm_model = os.getenv("LLM_MODEL",None)
embedding_model = os.getenv("embedding_model",None)
Groq_API_Key=os.environ.get("GROQ_API_KEY","")

#validaiton:
if not Groq_API_Key:
    raise ValueError("Invalid API Key: 'GROQ_API_KEY' is missing in environment variables.")#Done

#
@functools.lru_cache(maxsize=1)
def Cache_prephase_Instruction():
    """
    Cache instruction prompt to avoide realoading on each call.
    """
    return Instruction().prephase_prompt_instruciton



@functools.lru_cache(maxsize=1)
def cahce_Json_Parser():
    return JsonOutputParser(pydantic_object={
                "type":"object",
                "properties":{
                    "prephase":{"type": "string"}
                }
            })


class SingletoneMeta(type):
    """
    type is an  Parent Classs
    if create a obj of class(ModelInstance), python internally call the singletonemeta.__call__(cls, args, kwargs)
    here,
        cls ----->  refers to ModelInstance (the class being instaniated)
        cls is not a instance, it's the class itself

    *args and **kwargs are wrapping the class along with the positional argument in the class constructot
        - declaring args and kwargs for the purpose of Avoid,
            ERROR: *missing positional argument Error.*
    incase,
        if the new instance with the new value means, singleton will returning existing instance new value will not affect the singletone instance creation 
        
    Note: Singletone will create a class instance only once for the whole program!    
    """

    _instances = {}

    def __call__(cls, *args, **kwds):
        #checking if the instance is created or Not!
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]
    

class embedding_engine:
    def __init__(self, Model:str =embedding_model):
        self.engine = HuggingFaceEmbeddings(Model)



class ModelInstance(metaclass=SingletoneMeta):
    '''
    metaclass is a class that defines the behavior and structure of other classes    
    '''
    @staticmethod
    @functools.lru_cache(maxsize=1) #For single llm instance is efficiency
    def llm_instance(llm_Model:str = llm_model):
        '''
        Model instaniation method.
        '''
        try:
            return ChatGroq(model=llm_Model,api_key=Groq_API_Key,temperature=0.5,max_retries=3)
        except Exception as E:
            print(f"\nERROR: {str(E)} | from llm_Bot.py/model_instaniation");return {'messages':'Sorry something Went wrong!'}




@dataclass
class Bot_Assistant(ModelInstance): 
    """This class fetches raw model output without any post-processing.    
        - Uses a default LLM model if none is provided.
        - Implements `staticmethod` for standalone function behavior.
        - Dataclass ensures better field management.
    run_in_executer:
        - Run blocking operation in anathor event loop means free for other tasks.
        - lambda: wraps blocking function inside a lambda  
    """

    @staticmethod
    @Not_none  
    @functools.lru_cache(maxsize=128)#Unique input
    def prephase_Bot(UserInput:Annotated[str, 'User input here....']) -> dict:
        try:
            #ChainExecution
            chain = (Cache_prephase_Instruction() |  ModelInstance.llm_instance() | cahce_Json_Parser()).invoke({'user_input':UserInput})
            return{'model_raw_output':chain['prephase_context']}
        
        except Exception as E:
            print(f"\nERROR: {str(E)} | from llm_Bot.py/rawbotresponse/GroqLLM")
            return {'model_raw_output':'Sorry something Went wrong!'}














