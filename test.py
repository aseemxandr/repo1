class main:
    x = 'aseem'

    def func1(self):
        self.x += 'something'
        print('x=', self.x)


if __name__ == '__main__':
    main().func1()
