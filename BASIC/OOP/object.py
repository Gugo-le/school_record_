'''
OOP를 사용하면 코드를 더 나은 방법으로 이해하기 쉽고, 보다 전문적으로 개발할 수 있다는 큰 장점을 얻을 수 있습니다.

객체지향프로그래밍의 신비한 점은 데이터를 기반으로 동작하는 함수로 데이터를 캡슐화할 수 있다는 것입니다.

객체 지향 프로그래밍을 사용하면 다른 종류의 데이터와 함수들을 모두 하나의 파일에 가지고 있는 것보다 데이터를 더 구체적으로 구성할 수 있습니다. 이를 Box, Object, Bubble 등으로 부를 수 있습니다.

OOP는 코드를 보다 확장 가능하게 만들어주며 필요한 구조와 정신적인 규칙 및 모델을 제공합니다.

OOP는 데이터를 어떻게 구조화할지를 알려주고, 데이터를 수정하기 위한 함수를 어디에 넣어야 하는지에 대한 안내 역할을 합니다.

그렇게 되면 같은 수준에서 수많은 딕셔너리로 모두 다른 일을 하는 함수를 갖고 있을 필요가 없어집니다.
'''

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def sleep(self):
        print("zzzz....")
    
class GuardDog(Dog):
    
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        
    def rrrr(self):
        print("stay away")    


class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)

    def __str__(self):        
        return f"Puppy named {self.name}, breed: {self.breed}"
    
    def woof_woof(self):
        print("Woof woof")
        

ruffus = Puppy(
    name="Ruffus",
    breed = "Beagle"
)
bibi = GuardDog(
    name="Bibi",
    breed = "Dalmatian"
)

ruffus.woof_woof()
bibi.rrrr()