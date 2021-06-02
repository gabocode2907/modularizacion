local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
    
print(__name__)
if __name__ == "__main__":
    print("El archivo esta siendo ejecutado directamente")
else:
    print(". El archivo se llama: ", __name__)