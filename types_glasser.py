class err:
    def __init__(self,id):
        self.id = id

class general:
    def __init__(self,inputs):
        self.inputs = inputs

class Type:
    def __init__(self,name):
        self.name = name
        self.methods = {}
    def add_method(self,method_name):
        self.methods[method_name] = None
    def set_method(self,code,method):
        self.methods[method] = code

class var:
    def __init__(self,name : str,lifetime : int | None,type : Type):
        self.name = name
        self.type = type
        self.lifetime = lifetime
    def use_var(self) -> None | err :
        if self.lifetime == None:
            return None
        if self.lifetime > 0:
            self.lifetime -= 1
            return None
        return err(1)
class func:
    def __init__(self,name):
        self.name = name
        self.code = None
    def set_code(self,code):
        self.code = code