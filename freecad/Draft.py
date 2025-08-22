# Minimal Draft stub for tests
class _Draft:
    @staticmethod
    def Vec(a,b,c=None):
        if c is None:
            return (float(a), float(b))
        return (float(a), float(b), float(c))

    @staticmethod
    def Point(x,y,z=0):
        return (float(x), float(y), float(z))

__all__ = ['Vec', 'Point']
