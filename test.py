class Animal(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class FlyableMixin(object):
    def fly(self):
        print("[%s] %s is flying..." % (self.__class__.__name__, self))


class RunnableMixin(object):
    def run(self):
        print("[%s] %s is running..." % (self.__class__.__name__, self))


class CarnivorousMixIn(object):
    def kill(self, animal=None):
        if animal == None:
            print("[%s] %s is killing something..." % (self.__class__.__name__, self))
        else:
            print("[%s] %s is killing [%s] %s..." % (self.__class__.__name__, self, animal.__class__.__name__, animal))


class HerbivoresMixIn(object):
    def graze(self):
        print("[%s] %s is grazing..." % (self.__class__.__name__, self))


class Wolf(Mammal, RunnableMixin, CarnivorousMixIn):
    pass


class Sheep(Mammal, RunnableMixin, HerbivoresMixIn):
    pass


class Crow(Mammal, FlyableMixin, CarnivorousMixIn):
    pass


def testAnimal():
    sheep = Sheep('Shawn')
    sheep.run()
    sheep.graze()

    crow = Crow('Klins')
    crow.kill()
    crow.fly()

    wolf = Wolf('Adolfo')
    wolf.run()
    wolf.kill(sheep)


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CommunicationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('process request:', request)
        return request

    def process_response(self, request, response):
        print('process response:', response)
        return response


def testCommunication():
    cmw = CommunicationMiddleware('console')
    cmw('http request')


if __name__ == '__main__':
    # testAnimal()
    testCommunication()