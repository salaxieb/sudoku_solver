
def transform_white_on_black( x):
        """ Inverses [0, 255] scale to [-0.5, 0.5]. """
        return 0.5 - (x / 255)

 
def transform_black_on_white(x):
    """ Inverses [255, 0] scale to [-0.5, 0.5]. """
    return x / 255 - 0.5