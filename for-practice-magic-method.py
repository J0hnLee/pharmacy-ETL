##from typing_extensions import Self


#from msilib.schema import SelfReg


class A:
    def __new__(cls):
        print("new是一個class建立object的過程")
        return super().__new__(cls)
    def __init__(self) -> None:
        print("init是有了obj後初始化object的過程.")
        pass
    
    
o=A()
#o(1)
