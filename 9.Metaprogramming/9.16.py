from inspect import Signature,Parameter

parms = [Parameter('x',Parameter.POSITIONAL_OR_KEYWORD),
        Parameter('y',Parameter.POSITIONAL_OR_KEYWORD,default=42),
        Parameter('z',Parameter.POSITIONAL_OR_KEYWORD,default=None)
]
sig = Signature(parms)
print(sig)

def func(*args,**kwargs):
    bound_values = sig.bind(*args,**kwargs)
    for name,value in bound_values.arguments.items():
        print(name,value)
func(1,5,z=30)