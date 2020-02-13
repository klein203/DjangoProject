from collections import defaultdict
from casbin_sqlalchemy_adapter import Adapter
import casbin


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


class A(object):
    name = 'def_name'

    def __init__(self, *args, **kwargs):
        print('class [%s] instance [%s] call __init__' % (self.__class__.__name__, self))

    def set_name(self, name):
        self.name = name

    def normal_method(self, msg):
        print('class [%s] instance [%s] call class_method(cls, msg): %s' % (self.__class__.__name__, self, msg))

    @staticmethod
    def static_method(msg):
        print('class A call static_method(msg): %s' % msg)

    @classmethod
    def class_method(cls, msg):
        print('class [%s][%s] call class_method(cls, msg): %s' % (cls.__name__, cls.name, msg))

    def __call__(self, msg):
        print('class [%s] instance [%s] call __call__' % (self.__class__.__name__, self))
        self.static_method(msg)
        self.class_method(msg)
        print('class [%s] instance [%s] call __call__ end' % (self.__class__.__name__, self))

    def __repr__(self):
        return self.name


def testClass():
    a1 = A('a1')
    a1.set_name('a1')
    a1.normal_method('a1 111')
    a1.class_method('a1 222')
    a1.static_method('a1 333')
    a1('a1 444')
    print('------------------')

    a2 = A('a2')
    # a2.name = A.name
    a2.normal_method('a2 111')
    a2.class_method('a2 222')
    a2.static_method('a2 333')
    a2('a2 444')
    print('------------------')

    A.class_method('A 222')
    A.static_method('A 333')
    print('------------------')

    print([(type(getattr(a1, attr)), attr) for attr in dir(a1) if not attr.startswith('__')])
    print('------------------')
    print('A.__dict__', A.__dict__)
    print('a1.__dict__', a1.__dict__)
    print('a2.__dict__', a2.__dict__)


def testDynamicImport():
    cmd = 'test:testClazz'
    module, app = cmd.split(':')
    module = __import__(module)
    app = getattr(module, app)
    print('load module [%s], then invoke function [%s]' % (module.__name__, app.__name__))
    app()


def testDynamicImport2():
    cmd = 'test:Wolf:run'
    module, clazz, func = cmd.split(':')
    module = __import__(module)
    clazz = getattr(module, clazz)
    func = getattr(clazz('UNKNOWN'), func)
    print('load module [%s], class [%s], then invoke function [%s]' % (module.__name__, clazz.__name__, func.__name__))
    func()


class Ancestor:
    def pub_method(self):
        print('call class %s public method' % self)

    def _pri_method(self):
        print('call class %s call private method' % self)

    def __repr__(self):
        return self.__class__.__name__


class Descendant(Ancestor):
    pass


def testAccessRestriction():
    inst = Descendant()
    inst.pub_method()
    # runnable, with warning
    inst._pri_method()


def testCasbin():
    sqlite3_adapter = Adapter('sqlite:///db.sqlite3')
    enforcer = casbin.Enforcer("casbin_middleware/authz_model.conf", sqlite3_adapter)

    enforcer.enable_auto_save(False)
    # enforcer.load_model()
    # enforcer.load_policy()
    enforcer.add_policy()
    enforcer.save_policy()



if __name__ == '__main__':
    # testAnimal()
    # testCommunication()
    # testClass()
    # testDynamicImport()
    # testDynamicImport2()
    # testAccessRestriction()
    testCasbin()
