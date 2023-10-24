# example created by Bright Photonics

import numpy as np
import nazca as nd
import nazca.demofab as demo

# print(nd.__version__)

# create functions x, y, w for the viper-based mask_element:
def x(t, radius, angle, **kwargs):
    """X as function of t and free parameters."""
    return radius * np.cos(t * angle * np.pi / 180)
def y(t, radius, angle, **kwargs):
    """Y as function of t and free parameters."""
    return radius * np.sin(t * angle * np.pi / 180)
def w(t, width1=None, width2=None, **kwargs):
    """Width as function of t, width1 and width2 and free parameters."""
    return width1 + (width2 - width1) * t

# create the new parametric function using the template Tp_viper():
params = {'radius': 100, 'angle':90} # include defaults for *all* free parameters used in the functions x, y and w.
tapered_bend = nd.Tp_viper(x, y, w, xs='Deep', **params)

# put waveguides:
tapered_bend().put(0)
demo.deep.strt(length=100).put()
tapered_bend(angle=90, width2=20, N=1000).put()
tapered_bend(angle=-300, radius=60, width1=20, width2=0.5, N=2000).put()
nd.export_gds()
