from functools import wraps
from inspect import signature

def Not_none(func):
    @wraps(func)
    def None_Val(*args, **kwargs):
        try:
            InspectVar = signature(func)
            BoundArgs = InspectVar.bind(*args,**kwargs)
            BoundArgs.apply_defaults()

            for var_name, value in BoundArgs.arguments.items():
                if not value or value is None:
                    # print(f"[-]ERROR: Variable: {var_name} is `{value}` is empty from the function: ``{func.__name__}``");raise ValueError(f"[-]Variable: {var_name} is `{value}` Empty value  from the function ``{func.__name__}``");raise;
                    return{'response':" I didn't receive any spoken words from you. Please provide the text you'd like me to prephrase.",'resposne_time':'0.0'}
            return func(*args, **kwargs)
        except Exception as E:
            print(f"[-]Error From Not_None Decorator: {str(E)}")
            raise
    return None_Val





