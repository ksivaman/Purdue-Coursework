#! /usr/local/bin/python3.4
#
# $Author: ee364c10 $:
# $Date: 2015-03-01 18:10:31 -0500 (Sun, 01 Mar 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab07/MorePoints.py $:

import os
import math
import sys
import re

class Point3D:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
        
    def __str__(self):
        return "(" + "%.2f" %self.x + ", " +  "%.2f" %self.y + ", " + "%.2f" %self.z + ")"
        #return
    
    def distFrom(self, other):
        x_d = (self.x - other.x) * (self.x - other.x)
        #print x_d
        y_d = (self.y - other.y) * (self.y - other.y)
        #print y_d
        z_d = (self.z - other.z) * (self.z - other.z)
        #print z_d
        return math.sqrt(x_d + y_d + z_d)
    
    def nearestPoint(self, points):
        count = 0
        #point = Point3D()
        for element in points:
            if  count == 0:
                min_d = self.distFrom(element)
                point = element
                count = count + 1
                #print element
                #print min_d
            else:
                d = self.distFrom(element)
                #print element
                #print d
                if d <= min_d:
                    point = element
                    min_d = d
                    #print('Yes, smaller!!')
                    #print(point)
                    #print(min_d)
        #print('Nearest distance :', min_d)
        #print('Nearest point :', point)
        return point
            
    def clone(self):
        self_clone = Point3D(self.x, self.y, self.z)
        return self_clone

    def __add__(self, other):
        #print type(other)
        if isinstance(other, Point3D):
            p_add = Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
             p_add = Point3D(self.x + other, self.y + other, self.z + other)
        return p_add

    #def __add__(self, a):
    #    p_add = Point3D(self.x + a, self.y + a, self.z + a)
    #    return p_add

    def __radd__(self, a):
        p_add = Point3D(self.x + a, self.y + a, self.z + a)
        return p_add
    
    def __sub__(self, other):
        if isinstance(other, Point3D):
            p_add = Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
             p_add = Point3D(self.x - other, self.y - other, self.z - other)
        return p_add

    def __rsub__(self, a):
        p_sub = Point3D(self.x - a, self.y - a, self.z - a)
        return p_sub
    
    def __neg__(self):
        p_neg = Point3D(-self.x, -self.y, -self.z)
        return p_neg

    def __div__(self, other):
        if isinstance(other, Point3D):
            #print('jsjsjs')
            p_div = Point3D(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            #print('jjjj')
            p_div = Point3D(self.x / other, self.y / other, self.z / other)
        return p_div

    def __mul__(self, other):
        if isinstance(other, Point3D):
            #print('jsjsjs')
            p_mul = Point3D(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            #print('jjjj')
            p_mul = Point3D(self.x * other, self.y * other, self.z * other)
        return p_mul

    def __rmul__(self, a):
        p_mul = Point3D(self.x * a, self.y * a, self.z * a)
        return p_mul

    def __lt__(self, other):
        origin = Point3D()
        dist_o_1 = self.distFrom(origin)
        dist_o_2 = other.distFrom(origin)
        if dist_o_1 < dist_o_2:
            return True
        else:
            return False

    def __le__(self, other):
        origin = Point3D()
        dist_o_1 = self.distFrom(origin)
        dist_o_2 = other.distFrom(origin)
        if dist_o_1 <= dist_o_2:
            return True
        else:
            return False

    def __gt__(self, other):
        origin = Point3D()
        dist_o_1 = self.distFrom(origin)
        dist_o_2 = other.distFrom(origin)
        if dist_o_1 > dist_o_2:
            return True
        else:
            return False

    def __ge__(self, other):
        origin = Point3D()
        dist_o_1 = self.distFrom(origin)
        dist_o_2 = other.distFrom(origin)
        if dist_o_1 >= dist_o_2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    
class PointSet(Point3D):
    def __init__(self, points = set()):
        self.points = points
        #print len(self.points)
        #print self.points
    def addPoint(self, p):
        self.points.add(p)
        #print len(self.points)
    def count(self):
        #print(self.points[0])
        #print(self.points[1])
        #print(self.points)
        return len(self.points)
    def computeBoundingBox(self):
        x_min = 0.0
        x_max = 0.0
        y_min = 0.0
        y_max = 0.0
        z_min = 0.0
        z_max = 0.0
        count = 0
        for pt in self.points:
            if pt.x >= x_max:
                x_max = pt.x
            if pt.y >= y_max:
                y_max = pt.y
            if pt.z >= z_max:
                z_max = pt.z
            if count == 0:
                x_min = pt.x
                y_min = pt.y
                z_min = pt.z
                count = count + 1
                continue
            else:
                if pt.x <= x_min:
                    x_min = pt.x
                if pt.y <= y_min:
                    y_min = pt.y
                if pt.z <= z_min:
                    z_min = pt.z
        #print(x_min)
        #print(y_min)
        #print(z_min)
        p_min = Point3D(x_min, y_min, z_min)
        #print(p_min)
        p_max = Point3D(x_max, y_max, z_max)
        #print p_max
        #lst = []
        #lst.append(p_max)
        #lst.append(p_min)
        #print lst
        #t = tuple(lst)
        #t = (p_max)
        #t = (Point3D(p_max), Point3D(p_min))
        t = (p_max, p_min)
        #print len(t)
        #t.add(p_min)
        return t
    def computeNearestNeighbors(self, other):
        lst = []
        #print(self.count())
        for pt in self.points:
            t = ()
            #print(type(other))
            #print pt
            point_nearest = pt.nearestPoint(other)
            t = (pt, point_nearest)
            #print t
            #print t[0]
            #print t[1]
            lst.append(t)
            #print lst
        return lst
    
    def __add__(self, other):
        s2 = set()
        for element in self.points:
            s2.add(element)
        if isinstance(other, PointSet):
            for element2 in other.points:
                s2.add(element2)
            pointSet_add = PointSet(s2)
        else:
            s2.add(other)
            pointSet_add = PointSet(s2)   
        return pointSet_add
    
    def __sub__(self, other):
        s2 = set()
        for element in self.points:
            s2.add(element)
        if isinstance(other, PointSet):
            for element2 in other.points:
                if element2 in self.points:
                    s2.remove(element2)
            pointSet_add = PointSet(s2)
        else:
            if other in self.points:
                s2.remove(other)
            pointSet_add = PointSet(s2)   
        return pointSet_add

    def __gt__(self, other):
        if self.count() > other.count():
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.count() >= other.count():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.count() < other.count():
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.count() <= other.count():
            return True
        else:
            return False
        
'''
p1 = Point3D(4.5, 3.2, 1.78)
points = set()
#print points
points.add(p1)
ps = PointSet(points)
p2 = Point3D(4.6, 3.1, 1.88)
ps.addPoint(p2)
#print(ps.count())
p3 = Point3D(4.3, 3.4, 1.74)
ps.addPoint(p3)
#print(ps.count())
#print p3 in ps.points
t = ps.computeBoundingBox()
#print t[0]
#print t[1]
#pc1 = Point3D(2.3,0.22,-1.78)
#pc2 = Point3D(9.33, 3.2, 1.88)
#print pc1 in t
#print pc2 in t
#print p2 in t
#print t[0]
#print t[1]
other = set()
p4 = Point3D(9.34, 3.4, 7.9)
p5 = Point3D(4.51, 3.2, 1.78)
p6 = Point3D(9.88, 3.23, 7.33)
p7 = Point3D(4.6, 3.11, 1.88)
other.add(p4)
#other.add(p5)
#other.add(p6)
other.add(p7)
#lst = ps.computeNearestNeighbors(other)
#print(lst[2][1])
ps_2 = PointSet(other)
#ps2 = ps + ps_2
#for e in ps2.points:
#    print e
#p8 = Point3D(4.5, 3.2, 1.78)
#ps2 = ps - ps_2
#for e in ps2.points:
#    print e
print ps >= ps_2
'''

'''
p = Point3D(22.1, 4.3, 7.9)
#print type(p)
#str(p)
#print p
other = Point3D(23.3, 42.5, 8.9)
#print other
#print p.distFrom(other)
points = set()
points.add(other)
other2 = Point3D(3.3, 4.5, 6.7)
points.add(other2)
other3 = Point3D(4.5, 3.3, 2.10)
points.add(other3)
print p.nearestPoint(points)
#print other3.clone()
#other4 = other + other3
#print(other3 - other)
#a = float(6.9)
#b = 8.9
#print b - other2
#print a - other3
#print other2 - b
#print other3 - a
#print -other2
#print a * other
#p2 = Point3D(2.3, 4.5, 4.6)
#p3 = Point3D(24.3, 4.5, 4.6)
#print p3 > p2
'''