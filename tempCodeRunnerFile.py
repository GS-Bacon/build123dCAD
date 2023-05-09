l1=Polyline(*flange)
line =Line(l1@1,l1@0)

face = make_face(l1, line)
ex23=Pos(0,0,outpole_lengh/2)*Cylinder(bearing_OR+warll_thin*2,outpole_lengh)


ex23 -= revolve(face, Axis.Z)

show(ex23)
