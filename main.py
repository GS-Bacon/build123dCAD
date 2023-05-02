from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
from math import *
set_port(3939)

pole_lengh=120/2
pole_OR=34/2
flange_OR=40/2
flange_thin=1
bearing_Cangle=36
bearing_OR=47/2
bearing_thin=7.5
outpole_lengh=(pole_lengh+flange_thin+(bearing_OR-flange_OR)*tan(radians(bearing_Cangle))+bearing_thin)
warll_thin=4

#ヘッドセットOrbitMX No.20に合せて
flange=[(0,-0,0),
       (0,pole_OR,0),
       (0,pole_OR,pole_lengh),
       (0,flange_OR,pole_lengh),
       (0,flange_OR,pole_lengh+flange_thin),
       (0,bearing_OR,pole_lengh+flange_thin+(bearing_OR-flange_OR)*tan(radians(bearing_Cangle))),
       (0,bearing_OR,pole_lengh+flange_thin+(bearing_OR-flange_OR)*tan(radians(bearing_Cangle))+bearing_thin),
       (0,0,pole_lengh+flange_thin+(bearing_OR-flange_OR)*tan(radians(bearing_Cangle))+bearing_thin),
        ]

l1=Polyline(*flange)
line =Line(l1@1,l1@0)

face = make_face(l1, line)
ex23=Pos(0,0,outpole_lengh/2)*Cylinder(bearing_OR+warll_thin*2,outpole_lengh)


ex23 -= revolve(face, Axis.Z)

show(ex23)