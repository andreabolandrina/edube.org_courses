#!/usr/bin/env python3

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# Try to:
#     1) minimize the number of print() function invocations by inserting the \n sequence into the strings
#     2) make the arrow twice as large (but keep the proportions)
#     3) duplicate the arrow, placing both arrows side by side

x = 2 # multiplies every character (used for problem #2)
c = "*" # character for the arrow
s = " " # left and right spacing
si = " " # internal (to the arrow) spacing
cnt = 3 # number arrows (used for problem #3)
sep = " " # character separating the arrows

r1 = [s*4*x,c*x,s*4*x,sep]
r2 = [s*3*x,c*x,si*x,c*x,s*3*x,sep]
r3 = [s*2*x,c*x,si*3*x,c*x,s*2*x,sep]
r4 = [s*x,c*x,si*5*x,c*x,s*x,sep]
r5 = [c*3*x,si*3*x,c*3*x,sep]
r6 = [s*2*x,c*x,si*3*x,c*x,s*2*x,sep]
r7 = [s*2*x,c*x,si*3*x,c*x,s*2*x,sep]
r8 = [s*2*x,c*5*x,s*2*x,sep]

a = [*r1*cnt,"\n",*r2*cnt,"\n",*r3*cnt,"\n",*r4*cnt,"\n",*r5*cnt,"\n",*r6*cnt,"\n",*r7*cnt,"\n",*r8*cnt]

print(*a, sep="")
