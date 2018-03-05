import numpy as np
import copy

def vec(l):
    return np.array( [ float(l[0]), float(l[1]), float(l[2])] )

def test(v1, v2, err=0.001):
    return np.linalg.norm(vec(v1) - vec(v2) ) < err

def test_n(n1, n2, err=0.001):
    return abs( n1 - n2 ) < err
def v2s(v):
    """
        Return a string representation of a vector
        Example:
        >>> v = vec([1,2,3])
        >>> v2s( v )
        '[1.0, 2.0, 3.0]'
    """
    return "[%.1f, %.1f, %.1f]"%(v[0], v[1], v[2])

def normalize( v ):
    """
        Return the normalized vector
    
        Example:
        >>> normalize( vec([0.0, 0.0, 0.0]) )
        >>> normalize( vec([15.0, 20.0, 0.0]) )
        array([ 0.6,  0.8,  0. ])
        >>> normalize( vec([1.0, 0.0, 0.0]) )
        array([ 1.,  0.,  0.])
        >>> normalize( vec([0.0, 1.0, 0.0]) )
        array([ 0.,  1.,  0.])
        >>> normalize( vec([0.0, 0.0, 1.0]) )
        array([ 0.,  0.,  1.])
    """
    n = np.linalg.norm(v)
    if n==0:
        return None
    else:
        return v / np.linalg.norm(v)

def angle(vi, vi1, ai1):
    vi = normalize(vi)
    vi1 = normalize(vi1)
    if np.dot(np.cross(vi, vi1), ai1) >= 0:
        signe = 1
    else:
        signe = -1
    return signe * np.arccos( np.dot( vi, vi1) )

def gen():
    for i in [-1,1]:
        for j in [-1,1]:
            for k in [-1,1]:
                yield (i,j,k)

def norm_sup(l1 ,l2):
    assert( len(l1) == len(l2) )
    res = 0
    for i in range(len(l2)):
        if abs( l1[i] - l2[i] ) > res:
            res = abs( l1[i] - l2[i] )
    return res

class arm:
    def solve_min(self, thetas=None):
        """
            Return True if a solution had been founded and False in the other
            case.
            Example:

            >>> a = arm(
            ...     end_position = [0.01, 0.06, 0.3] , 
            ...     end_normal = [0.0, -0.6, -1.0], 
            ...     end_direction = [1.0,0.0,0.0],
            ...     arm_size = [0.078, 0.067, 0.067, 0.067, 0.064]
            ... )
            >>> a.solve_min()
            True
            >>> a = arm(
            ...     end_position = [0.0, 0.0, 0.343] , 
            ...     end_normal = [0.0, 0.0, -1.0], 
            ...     end_direction = [1.0,0.0,0.0],
            ...     arm_size = [0.078, 0.067, 0.067, 0.067, 0.064]
            ... )
            >>> a.solve_min()
            True
            >>> test(a.thetas, [1.57079, 0.0, 0.0, 0.0, 0.0, 0.0])
            True
        """
        if thetas is None:
            if self.thetas is None:
                thetas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            else:
                thetas = copy.deepcopy( self.thetas )
        min_signes = None
        min_chgt = None
        for (i,j,k) in gen():
            if self.solve(signes=[i,j,k]):
                chgt = norm_sup(self.thetas, thetas)
                if min_chgt is None or min_chgt > chgt:
                    min_chgt = chgt
                    min_signes = [i, j, k]
        if min_chgt is None:
            return False
        self.solve(signes=min_signes)
        return True
    def solve(self, signes=[1,1,1]):
        """
            >>> a = arm( 
            ...     end_position = vec([10,11,12]),
            ...     end_normal = vec([13,14,15]),
            ...     end_direction = vec([16,17,18]),
            ...     arm_size = [2, 3, 4, 5, 6],
            ... )
            >>> a.solve()
            False
            >>> a = arm( 
            ...     end_position = vec([2.0,0.0,0.0]),
            ...     end_normal = vec([0,0,-1]),
            ...     end_direction = vec([1,0,0]),
            ...     arm_size = [2.0, 2.0, 2.0, 2.0, 2.0],
            ... )
            >>> a.solve()
            True
            >>> test( a.o0, [0,0,0] )
            True
            >>> test( a.x0, [1.0,0,0] )
            True
            >>> test( a.n0, [0.0,0.0,1.0] )
            True
            >>> test( a.o5, [2.0,0.0,0.0] )
            True
            >>> test( a.x5, [1.0,0.0,0.0] )
            True
            >>> test( a.n5, [0.0,0.0,-1.0] )
            True
            >>> test( a.v0, [0.0,0.0,2.0] )
            True
            >>> test( a.o1, [0.0,0.0,2.0] )
            True
            >>> test( a.v4, [0.0,0.0,2.0] )
            True
            >>> test( a.o4, [2.0,0.0,-2.0] )
            True
            >>> test( a.a2, [0.0,-1.0,0.0] )
            True
            >>> test_n( a.c0, -1.0 )
            True
            >>> test_n( a.s0, 0.0 )
            True
            >>> test( a.a1, [-1.0, 0.0, 0.0] )
            True
            >>> test_n( a.g, -1.0 )
            True
            >>> test_n( a.c1, -1.0 )
            True
            >>> test_n( a.s1, 0.0 )
            True
            >>> test( a.v1, [0.0, 0.0, -2.0] )
            True
            >>> test( a.o2, [0.0, 0.0, 0.0] )
            True
            >>> test( a.o2, [0.0, 0.0, 0.0] )
            True
            >>> test( a.u, [0.70710, 0.0, -0.70710678])
            True
            >>> test( a.w, [0.0, -1.0, 0.0])
            True
            >>> test( a.v, [0.70710, 0.0, 0.70710678])
            True
            >>> test_n( a.alpha, 1.41421)
            True
            >>> test_n( a.beta, 1.41421)
            True
            >>> test(a.o3_r, [1.41421, 1.41421, 0.0])
            True
            >>> test(a.o3, [2.0, 0.0, 0.0])
            True
        """
        [l0, l1, l2, l3, l4] = self.size
        self.signes = signes
        [s_t0, s_t1, s_b] = signes

        self.v0 = self.n0 * l0
        self.o1 = self.o0 + self.v0

        self.v4 = - self.n5 * l4
        self.o4 = self.o5 - self.v4

        o1o5 = self.o5 - self.o1
        if np.linalg.norm(o1o5)==0:
            return False

        self.a2 = normalize( np.cross(o1o5 , self.v4) )

        if self.a2 is None:
            if o1o5[0] == 0.0 and o1o5[1] == 0.0:
                self.a2 = vec([1.0,0.0,0.0])
            else :
                self.a2 = normalize( vec([o1o5[1],-o1o5[0],0.0]) )

        self.c0 = s_t0 * self.a2[1] / np.sqrt( self.a2[0]**2 +  self.a2[1]**2 )
        self.s0 = - s_t0 * self.a2[0] / np.sqrt( self.a2[0]**2 +  self.a2[1]**2 )

        self.a1 = vec( [self.c0, self.s0, 0.0] )

        self.g = self.a2[0] * self.s0 - self.a2[1] * self.c0
        if self.g**2 + self.a2[2]**2 > 0.0:
            self.c1 = s_t1 * self.g / np.sqrt( self.g**2 + self.a2[2]**2 )
            self.s1 = - s_t1 * self.a2[2] / np.sqrt( self.g**2 + self.a2[2]**2 )
        else:
            self.c1 = s_t1
            self.s1 = 0.0
        self.v1 = vec( [ self.s1*self.s0, -self.s1*self.c0, self.c1 ] ) * l2
        self.o2 = self.o0 + self.v0 + self.v1

        o2o4 = self.o4 - self.o2

        no2o4 = np.linalg.norm(o2o4)
        if no2o4 == 0:
            return False
        if no2o4 > l2 + l3 :
            return False

        self.u = normalize( o2o4 )
        self.w = self.a2
        self.v = np.cross( self.w, self.u )

        self.M = np.matrix([self.u, self.v, self.w]) #.getT()

        self.alpha = ( l3**2 - l2**2 + no2o4**2 )/( 2*no2o4 )

        if l2**2 - self.alpha**2 < 0 :
            return False

        self.beta = s_b * np.sqrt( l2**2 - self.alpha**2 )

        self.o3_r = vec([self.alpha, self.beta, 0])
        self.o3 = (self.o3_r * self.M).A1 + self.o2

        self.v2 = self.o3 - self.o2
        self.v3 = self.o4 - self.o3

        self.theta0 = angle( self.x0, self.a1, vec([0,0,1.0]) )
        self.theta1 = angle( self.v0, self.v1, self.a1 )
        self.theta2 = angle( self.v1, self.v2, self.a2 )
        self.theta3 = angle( self.v2, self.v3, self.a2 )
        self.theta4 = angle( self.v3, self.v4, self.a2 )
        self.theta5 = angle( self.x5, self.a2, self.n5 )
        self.thetas = [
            self.theta0, self.theta1, 
            self.theta2, self.theta3, 
            self.theta4, self.theta5 
        ]
        return True

    def __init__(
        self,
        end_position, end_normal, end_direction,
        arm_size
    ):
        """
            Define the kinematic of an arm

            Example:
            >>> a = arm( 
            ...     end_position = vec([10,11,12]),
            ...     end_normal = vec([13,14,15]),
            ...     end_direction = vec([16,17,18]),
            ...     arm_size = [2, 3, 4, 5, 6],
            ... )
            >>> a.size
            [2.0, 3.0, 4.0, 5.0, 6.0]
            >>> test( a.o0, [0,0,0] )
            True
            >>> test( a.n0, (0.0, 0.0, 1.0) )
            True
            >>> test( a.x0, (1.0, 0.0, 0.0) )
            True
            >>> test(a.o5, [10,11,12])
            True
            >>> test(a.n5, (0.53520, 0.57637, 0.61754))
            True
            >>> test(a.x5, (0.54276, 0.57668, 0.61060))
            True
            >>> test(a.x5, (0.54276, 0.57668, 0.61060))
            True
        """
        self.o0 = vec([0.0, 0.0, 0.0])
        self.x0 = vec([1.0, 0.0, 0.0])
        self.n0 = vec([0.0, 0.0, 1.0])
        self.o5 = vec(end_position)
        self.n5 = normalize( vec(end_normal) )
        self.x5 = normalize( vec(end_direction) )
        self.size = list(map(float, arm_size))
        self.thetas = None

    def __repr__(self):
        return (
            "<p1 : %s, n1: %s, d1, %s | "%(
                str(v2s(self.o0)), 
                str(v2s(self.n0)),
                str(v2s(self.x0))
            ) +
            "p2 : %s, n2: %s, d2 %s"%(
                str(v2s(self.o5)), 
                str(v2s(self.n5)),
                str(v2s(self.x5))
            ) + 
            " | size : [%.1f, %.1f, %.1f, %.1f, %.1f]>"%(
                self.size[0],
                self.size[1],
                self.size[2],
                self.size[3],
                self.size[4],
            )
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()

