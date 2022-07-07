
# Example
# print(1 +2j)
# print((1+4j)*(5+3j))

class Complex():

    def __init__(self, real_part, imagenative_part):
        self._real = real_part
        self._im = imagenative_part

    def get_im(self):
        return(self._im)

    def get_re(self):
        return(self._real)

    def complex_mode(self):
        if self.get_im() > 0:
           return f'{self.get_re()}+{self.get_im()}j'
        return f'{self.get_re()}{self.get_im()}j'

    def __call__(self,*args,**kwargs):
        return self.complex_mode()

    def __add__(self, other):
        if type(self) == Complex and type(other) is Complex:
            return Complex(self.get_re()+other.get_re(),self.get_im() + other.get_im())
        else:
            raise ValueError('You try to summarize non-complex numbers')

    def __sub__(self, other):
        if type(self) == Complex and type(other) is Complex:
            return Complex(self.get_re()-other.get_re(),self.get_im() - other.get_im())
        else:
            raise ValueError('You try to substract non-complex numbers')

    def __mul__(self, other):
        if isinstance(self,Complex) and isinstance(other, int):
            return Complex(self.get_re()*other, self.get_im()*other)

        elif isinstance(self, Complex) and isinstance(other, Complex):

            im1 = self.get_im()
            im2 = other.get_im()
            re1 = self.get_re()
            re2 = other.get_re()
            # print(re1*re2 -im1*im2, re1*im2+re2*im1)
            return Complex(re1*re2 -im1*im2, re1*im2+re2*im1)
        else:
            raise ValueError


    def __rmul__(self, other):

        if isinstance(self,int) and isinstance(other, Complex):
            return Complex(self.get_re()*other, self.get_im()*other)

        elif isinstance(self, Complex) and isinstance(other, Complex):

            im1 = self.get_im()
            im2 = other.get_im()
            re1 = self.get_re()
            re2 = other.get_re()
            # print(re1*re2 -im1*im2, re1*im2+re2*im1)
            return Complex(re1*re2 -im1*im2, re1*im2+re2*im1)
        else:
            raise ValueError

if __name__ == '__main__':
    # c1 = Complex(1,5)
    # c2 = Complex(5.67,2)
    # print(c1(), c2())
    #
    # c3 = c1 + c2
    # c4 = c3 - c2
    # print(c3(),c4(),c1())

    # c5 = c2*5
    # print(c5())
    #
    # c6 = c1*c2
    # print(c6())

    print((1 + 4j) * (5 + 3j))
    c7 = Complex(1, 4)
    c8 = Complex(5, 3)
    print((c7*c8)())
    print(c7.__dict__)