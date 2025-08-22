# Minimal DraftVecUtils stub used by tests

def vec2d(x, y):
    return (float(x), float(y))

# Provide placeholders for functions the code may call
def length(vec):
    x, y = vec
    return (x**2 + y**2)**0.5

def rotate(vec, angle):
    import math
    x, y = vec
    ca = math.cos(angle)
    sa = math.sin(angle)
    return (x*ca - y*sa, x*sa + y*ca)

__all__ = ['vec2d', 'length', 'rotate']
