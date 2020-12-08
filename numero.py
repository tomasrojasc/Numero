import math

class Numero:
    def __init__(self, val, err):
        self.val = val
        self.err = err
        self.decimals = None
        
    def __mul__(self, other):
        if isinstance(other, Numero):
            final_val = self.val * other.val
            final_err = self.val * other.val * \
                        math.sqrt((self.err / self.val) ** 2 + (other.err / other.val) ** 2)
            return Numero(final_val, final_err)
        
        if isinstance(other, (int, float)):
            return self.__mul__(Numero(other, 0))

    def __add__(self, other):
        if isinstance(other, Numero):
            final_val = self.val + other.val 
            final_err = math.sqrt(self.err ** 2 + other.err ** 2)
            return Numero(final_val, final_err)
        
        if isinstance(other, (int, float)):
            return self.__add__(Numero(other, 0))
    
    def __sub__(self, other):
        if isinstance(other, Numero):
            other = Numero(-1, 0) * other
            return self.__add__(other)
        
        if isinstance(other, (int, float)):
            return self.__sub__(Numero(other, 0))
    
    def __truediv__(self, other):
        if isinstance(other, Numero):
            final_val = self.val / other.val
            final_err = (self.val / other.val) * math.sqrt((self.err / self.val) ** 2 + (other.err / other.val) ** 2)
            return Numero(final_val, final_err)
        
        if isinstance(other, (int, float)):
            return self.__truediv__(Numero(other, 0))
        
        
    def __rtruediv__(self, other):
        if isinstance(other, Numero):
            final_val = other.val / self.val
            final_err = (other.val / self.val) * math.sqrt((self.err / self.val) ** 2 + (other.err / other.val) ** 2)
            return Numero(final_val, final_err)
        
        if isinstance(other, (int, float)):
            return self.__rtruediv__(Numero(other, 0))
            
    
    def __repr__(self):
        if isinstance(self.decimals, type(None)):
            return '{} ± {}'.format(self.val, self.err)
        else:
            assert isinstance(self.decimals, int)
            text = '{:.' + str(self.decimals) + '} ± {:.' + str(self.decimals) + '}'
            return text
