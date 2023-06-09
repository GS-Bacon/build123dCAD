from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
from math import *
set_port(3939)

#プリント品基準の壁厚
WALL_THIN=4
#プリント品の色
PRINT_COLLAR=(200,200,200)
#ミスミ40x40 5シリーズ
ALUMI_FRAME=40
#プリント品のクリアランス
CLEARANCE=0.1

def pole():
    pole_lengh=120/2 #ハンドルポール長さ
    pole_OR=34/2 #hハンドルポール外径
    flange_OR=40/2
    flange_thin=1
    bearing_Cangle=36
    bearing_OR=47/2
    bearing_thin=7.5
    out_pole_lengh=(pole_lengh+flange_thin+(bearing_OR-flange_OR)*tan(radians(bearing_Cangle))+bearing_thin)

    #ヘッドセットOrbitMX No.20に合せて回転形状を生成
    #line(X,Y,Z)
    flange=[
        (0,0,0),
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

    #out_pole_OR=bearing_OR+wall_thin*2 #25.5
    out_pole_OR=30+WALL_THIN

    out_pole=Cylinder(out_pole_OR,out_pole_lengh)
    ex2=Pos(0,0,out_pole_lengh/2)*out_pole

    ex2 -= revolve(face, Axis.Z)

    show(ex2)
    #show(ex2)

    pole_base=[
        (-20,0,0),
        (20,0,0),
        (20,0,out_pole_lengh),
        (-20,0,out_pole_lengh),
        (-20,0,0),
        ]

    l2=Pos(0,out_pole_OR+0.1,0)*Polygon(*pole_base)
    ex2+=extrude(l2,until=Until.NEXT,target=ex2)

    ex2=fillet(ex2.edges().group_by(Axis.Y)[-1].filter_by(Axis.Z),1)
    ex2=fillet(ex2.edges().group_by(Axis.Z)[-1],1)
    ex2+=mirror(ex2,Plane.XZ)
    ex2+=mirror(ex2,Plane.XY)
    return ex2

frame_length=60
frame_stay_wall=Rectangle(ALUMI_FRAME+WALL_THIN,ALUMI_FRAME+WALL_THIN)
frame_stay_wall-=offset(
    frame_stay_wall,
    -WALL_THIN-CLEARANCE,
    kind=Kind.INTERSECTION,
    )
ex2=extrude(frame_stay_wall,frame_length)
hole_loc=Location(0,-(ALUMI_FRAME+WALL_THIN+CLEARANCE)/2,30)
ex2-=hole_loc*Hole(10,10)
show_object(ex2)
#show_object(pole(),name="pole",options={"color": PRINT_COLLAR})