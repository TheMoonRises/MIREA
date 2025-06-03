class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'
    def forge(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'E':
            self.state = 'B'
            return 7
        if self.state == 'D':
            self.state = 'E'
            return 3
        raise MealyError('forge')
    def mass(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'D':
            self.state = 'G'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'F':
            return 9
        raise MealyError('mass')
    def wreck(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'E':
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 8
        raise MealyError('wreck')

def main():
    return StateMachine()

def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) == error
    assert output is None

def test():
    o = main()
    assert o.forge() == 0
    assert o.mass() == 1
    assert o.wreck() == 2
    assert o.mass() == 4
    o = main()
    assert o.forge() == 0
    assert o.mass() == 1
    assert o.wreck() == 2
    assert o.forge() == 3
    assert o.forge() == 7
    o = main()
    assert o.forge() == 0
    assert o.mass() == 1
    assert o.wreck() == 2
    assert o.forge() == 3
    assert o.wreck() == 6
    assert o.mass() == 5
    assert o.mass() == 9
    assert o.wreck() == 8
    raises(lambda: o.forge(), MealyError)
    raises(lambda: o.wreck(), MealyError)
    raises(lambda: o.mass(), MealyError)