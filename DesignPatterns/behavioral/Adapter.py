# -*- coding:utf-8 -*-

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return self.name + 'executes a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return self.name + 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return self.name + 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    objects = [Computer('Computer')]
    synth = Synthesizer('Synthesizer')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Human')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))
        print('type is {}'.format(type(i)))
        print("*" * 20)

    """
    the Computer computer Computerexecutes a program
    type is <class '__main__.Computer'>
    
    the Synthesizer synthesizer Synthesizeris playing an electronic song
    type is <class '__main__.Adapter'>
    
    Human the human Humansays hello
    type is <class '__main__.Adapter'>
    """
    for i in objects:
        print(i.obj.name)  # i.name
