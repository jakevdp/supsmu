from . import _supsmu
import numpy as np


def supsmu(x, y, w=1, periodic=False, span=0.0, alpha=-1.0):
    """Interface to Friedman's supsmu Fortran routine

    Parameters
    ----------
    x, y : array_like
        1D arrays giving the x and y coordinates of the data
    w : float or array_like (optional)
        weights for each point. If not given, equal weights are used.
    periodic : boolean
        if True, then use a periodic smooth with period 1
        (in this case, x is assumed to fall in the range 0...1).
    span : float (optional)
        The fractional data span to use (0 <= span < 1).
        If specified, then use the given fixed span.
        If set to zero (default) then use a variable span.
    alpha : float (optional)
        Degree of bass enhancement, 0 <= alpha <= 10. If alpha < 0, then
        no bass enhancement will be used.

    Returns
    -------
    y_smooth : ndarray
        smoothed y values corresponding to x
    """
    x, y, w = np.broadcast_arrays(x, y, w)
    x = np.asarray(x, dtype=np.float32, order='F')
    y = np.asarray(y, dtype=np.float32, order='F')
    w = np.asarray(w, dtype=np.float32, order='F')
    N = len(x)
    assert(x.ndim == 1)
    assert 0 <= span < 1
    assert alpha <= 10
    sc = np.zeros((N, 7), dtype=np.float32, order='F')
    y_smooth = _supsmu.supsmu(x, y, w, periodic, span, alpha, sc)
    return y_smooth
