from math import *


def to_hyp_from_adj(adj, angle):
    hyp = adj / cos(radians(angle))
    return hyp


def to_adj_from_hyp(hyp, angle):
    adj = hyp * cos(radians(angle))
    return adj


def to_angle_from_hyp_adj(hyp, adj):
    angle = degrees(acos(adj / hyp))
    return angle

def to_opp_from_hyp(hyp, angle):
    opp = hyp * sin(radians(angle))
    return opp

def to_angle_from_adj_opp(adj, opp):
    angle = degrees(atan(opp / adj))
    return angle


adj_a = 8
angle_a = 28
hyp_a = to_hyp_from_adj(adj_a, angle_a)
print("Hyp A: " + str(hyp_a))

hyp_b = (hyp_a - 2.5) + 3.6
angle_b = 11
adj_b = to_adj_from_hyp(hyp_a, angle_b)
print("Adj B: " + str(hyp_b))

hyp_c = (adj_b - 2) + 2.9
adj_c = 3.8
angle_c = to_angle_from_hyp_adj(hyp_c, adj_c)
opp_c = to_opp_from_hyp(hyp_c, angle_c)
print("Opp C: " + str(opp_c))

hyp_d = (opp_c - 1) + 3.2
angle_d = 43
adj_d = to_adj_from_hyp(hyp_d, angle_d)
print("Adj D: " + str(adj_d))

adj_e = (adj_d - 1) + 1
angle_e = 30
hyp_e = to_hyp_from_adj(adj_e, angle_e)
print("Hyp E: " + str(hyp_e))

hyp_f = hyp_e + 3.2 + 1.9
angle_f = 19
adj_f = to_adj_from_hyp(hyp_f, angle_f)
print("Hyp F: " + str(hyp_f))

adj_g = (hyp_f - 4.8 - 1.1)
angle_g = 46
hyp_g = to_hyp_from_adj(adj_g, angle_g)
print("Hyp G: " + str(hyp_g))

adj_h = (hyp_g - 1.7)
opp_h = 3.2
angle_h = to_angle_from_adj_opp(adj_h, opp_h)
hyp_h = to_hyp_from_adj(adj_h, angle_h)
print("Hyp H: " + str(hyp_h))

hyp_i = (hyp_h - 2.73)
angle_i = 22
adj_i = to_adj_from_hyp(hyp_i, angle_i)
print("Adj I: " + str(adj_i))

adj_j = (adj_i - 2.24) + 6.9
angle_j = 4
hyp_j = to_hyp_from_adj(adj_j, angle_j)
print("Hyp J: " + str(hyp_j))
