#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import nhood_objects as nho


list = [
'nho.Abell.exterior.xy',
'nho.Allendale.exterior.xy',
'nho.Arcadia.exterior.xy',
'nho.Arlington.exterior.xy',
'nho.Armistead_Gardens.exterior.xy',
'nho.Ashburton.exterior.xy',
'nho.Baltimore_Highlands.exterior.xy',
'nho.Barclay.exterior.xy',
'nho.Barre_Circle.exterior.xy',
'nho.Bayview.exterior.xy',
'nho.Beechfield.exterior.xy',
'nho.Belair_Edison.exterior.xy',
'nho.Belair_Parkside.exterior.xy',
'nho.Bellona_Gittings.exterior.xy',
'nho.Belvedere.exterior.xy',
'nho.Berea.exterior.xy',
'nho.Better_Waverly.exterior.xy',
'nho.Beverly_Hills.exterior.xy',
'nho.Biddle_Street.exterior.xy',
'nho.Blythewood.exterior.xy',
'nho.Bolton_Hill.exterior.xy',
'nho.Boyd_Booth.exterior.xy',
'nho.Brewers_Hill.exterior.xy',
'nho.Bridgeview_Greenlawn.exterior.xy',
'nho.Broadway_East.exterior.xy',
'nho.Broening_Manor.exterior.xy',
'nho.Brooklyn.exterior.xy',
'nho.Burleith_Leighton.exterior.xy',
'nho.ButcherS_Hill.exterior.xy',
'nho.Callaway_Garrison.exterior.xy',
'nho.Cameron_Village.exterior.xy',
'nho.Canton.exterior.xy',
'nho.Canton_Industrial_Area.exterior.xy',
'nho.Care.exterior.xy',
'nho.Carroll_Park.exterior.xy',
'nho.Carroll_South_Hilton.exterior.xy',
'nho.Carroll___Camden_Industrial_Area.exterior.xy',
'nho.Carrollton_Ridge.exterior.xy',
'nho.Cedarcroft.exterior.xy',
'nho.Cedmont.exterior.xy',
'nho.Cedonia.exterior.xy',
'nho.Central_Forest_Park.exterior.xy',
'nho.Central_Park_Heights.exterior.xy',
'nho.Charles_North.exterior.xy',
'nho.Charles_Village.exterior.xy',
'nho.Cherry_Hill.exterior.xy',
'nho.Cheswolde.exterior.xy',
'nho.Chinquapin_Park.exterior.xy',
'nho.Clifton_Park.exterior.xy',
'nho.Coldspring.exterior.xy',
'nho.Coldstream_Homestead_Montebello.exterior.xy',
'nho.Concerned_Citizens_Of_Forest_Park.exterior.xy',
'nho.Coppin_HeightsAsh_Co_East.exterior.xy',
'nho.Cross_Country.exterior.xy',
'nho.Cross_Keys.exterior.xy',
'nho.Curtis_Bay.exterior.xy',
'nho.Curtis_Bay_Industrial_Area.exterior.xy',
'nho.Cylburn.exterior.xy',
'nho.Darley_Park.exterior.xy',
'nho.Dickeyville.exterior.xy',
'nho.Dolfield.exterior.xy',
'nho.Dorchester.exterior.xy',
'nho.Downtown.exterior.xy',
'nho.Downtown_West.exterior.xy',
'nho.Druid_Heights.exterior.xy',
'nho.Druid_Hill_Park.exterior.xy',
'nho.Dunbar_Broadway.exterior.xy',
'nho.Dundalk_Marine_Terminal.exterior.xy',
'nho.East_Arlington.exterior.xy',
'nho.East_Baltimore_Midway.exterior.xy',
'nho.Easterwood.exterior.xy',
'nho.Eastwood.exterior.xy',
'nho.Edgewood.exterior.xy',
'nho.Edmondson_Village.exterior.xy',
'nho.Ednor_Gardens_Lakeside.exterior.xy',
'nho.Ellwood_Park_Monument.exterior.xy',
'nho.Evergreen.exterior.xy',
'nho.Evergreen_Lawn.exterior.xy',
'nho.Evesham_Park.exterior.xy',
'nho.Fairfield_Area.exterior.xy',
'nho.Fairmont.exterior.xy',
'nho.Fallstaff.exterior.xy',
'nho.Federal_Hill.exterior.xy',
'nho.Fells_Point.exterior.xy',
'nho.Forest_Park.exterior.xy',
'nho.Forest_Park_Golf_Course.exterior.xy',
'nho.Four_By_Four.exterior.xy',
'nho.Frankford.exterior.xy',
'nho.Franklin_Square.exterior.xy',
'nho.Franklintown.exterior.xy',
'nho.Franklintown_Road.exterior.xy',
'nho.Garwyn_Oaks.exterior.xy',
'nho.Gay_Street.exterior.xy',
'nho.Glen.exterior.xy',
'nho.Glen_Oaks.exterior.xy',
'nho.Glenham_Belhar.exterior.xy',
'nho.Graceland_Park.exterior.xy',
'nho.Greektown.exterior.xy',
'nho.Greenmount_Cemetery.exterior.xy',
'nho.Greenmount_West.exterior.xy',
'nho.Greenspring.exterior.xy',
'nho.Grove_Park.exterior.xy',
'nho.Guilford.exterior.xy',
'nho.Gwynns_Falls.exterior.xy',
'nho.Gwynns_Falls_Leakin_Park.exterior.xy',
'nho.Hamilton_Hills.exterior.xy',
'nho.Hampden.exterior.xy',
'nho.Hanlon_Longwood.exterior.xy',
'nho.Harlem_Park.exterior.xy',
'nho.Harwood.exterior.xy',
'nho.Hawkins_Point.exterior.xy',
'nho.Heritage_Crossing.exterior.xy',
'nho.Herring_Run_Park.exterior.xy',
'nho.Highlandtown.exterior.xy',
'nho.Hillen.exterior.xy',
'nho.Hoes_Heights.exterior.xy',
'nho.Holabird_Industrial_Park.exterior.xy',
'nho.Hollins_Market.exterior.xy',
'nho.Homeland.exterior.xy',
'nho.Hopkins_Bayview.exterior.xy',
'nho.Howard_Park.exterior.xy',
'nho.Hunting_Ridge.exterior.xy',
'nho.Idlewood.exterior.xy',
'nho.Inner_Harbor.exterior.xy',
'nho.Irvington.exterior.xy',
'nho.Johns_Hopkins_Homewood.exterior.xy',
'nho.Johnston_Square.exterior.xy',
'nho.Jones_Falls_Area.exterior.xy',
'nho.Jonestown.exterior.xy',
'nho.Kenilworth_Park.exterior.xy',
'nho.Kernewood.exterior.xy',
'nho.Keswick.exterior.xy',
'nho.Kresson.exterior.xy',
'nho.Lake_Evesham.exterior.xy',
'nho.Lake_Walker.exterior.xy',
'nho.Lakeland.exterior.xy',
'nho.Langston_Hughes.exterior.xy',
'nho.Lauraville.exterior.xy',
'nho.Levindale.exterior.xy',
'nho.Liberty_Square.exterior.xy',
'nho.Little_Italy.exterior.xy',
'nho.Loch_Raven.exterior.xy',
'nho.Locust_Point.exterior.xy',
'nho.Locust_Point_Industrial_Area.exterior.xy',
'nho.Lower_Edmondson_Village.exterior.xy',
'nho.Lower_Herring_Run_Park.exterior.xy',
'nho.Loyola_Notre_Dame.exterior.xy',
'nho.Lucille_Park.exterior.xy',
'nho.Madison_Eastend.exterior.xy',
'nho.Madison_Park.exterior.xy',
'nho.Mayfield.exterior.xy',
'nho.Mcelderry_Park.exterior.xy',
'nho.Medfield.exterior.xy',
'nho.Medford.exterior.xy',
'nho.Mid_Govans.exterior.xy',
'nho.Mid_Town_Belvedere.exterior.xy',
'nho.Middle_Branch_Reedbird_Parks.exterior.xy',
'nho.Middle_East.exterior.xy',
'nho.Midtown_Edmondson.exterior.xy',
'nho.Millhill.exterior.xy',
'nho.Milton_Montford.exterior.xy',
'nho.Mondawmin.exterior.xy',
'nho.Montebello.exterior.xy',
'nho.Moravia_Walther.exterior.xy',
'nho.Morgan_Park.exterior.xy',
'nho.Morgan_State_University.exterior.xy',
'nho.Morrell_Park.exterior.xy',
'nho.Mosher.exterior.xy',
'nho.Mount_Holly.exterior.xy',
'nho.Mount_Vernon.exterior.xy',
'nho.Mount_Washington.exterior.xy',
'nho.Mount_Winans.exterior.xy',
'nho.Mt_Pleasant_Park.exterior.xy',
'nho.New_Northwood.exterior.xy',
'nho.New_Southwest_Mount_Clare.exterior.xy',
'nho.North_Harford_Road.exterior.xy',
'nho.North_Roland_Park_Poplar_Hill.exterior.xy',
'nho.Northwest_Community_Action.exterior.xy',
'nho.ODonnell_Heights.exterior.xy',
'nho.Oakenshawe.exterior.xy',
'nho.Oaklee.exterior.xy',
'nho.Old_Goucher.exterior.xy',
'nho.Oldtown.exterior.xy',
'nho.Oliver.exterior.xy',
'nho.Orangeville.exterior.xy',
'nho.Orangeville_Industrial_Area.exterior.xy',
'nho.Orchard_Ridge.exterior.xy',
'nho.Original_Northwood.exterior.xy',
'nho.Otterbein.exterior.xy',
'nho.Overlea.exterior.xy',
'nho.Panway_Braddish_Avenue.exterior.xy',
'nho.Park_Circle.exterior.xy',
'nho.Parklane.exterior.xy',
'nho.Parkside.exterior.xy',
'nho.Parkview_Woodbrook.exterior.xy',
'nho.Patterson_Park.exterior.xy',
'nho.Patterson_Park_Neighborhood.exterior.xy',
'nho.Patterson_Place.exterior.xy',
'nho.Pen_Lucy.exterior.xy',
'nho.Penn_Fallsway.exterior.xy',
'nho.Penn_North.exterior.xy',
'nho.Penrose_Fayette_Street_Outreach.exterior.xy',
'nho.Perkins_Homes.exterior.xy',
'nho.Perring_Loch.exterior.xy',
'nho.Pimlico_Good_Neighbors.exterior.xy',
'nho.Pleasant_View_Gardens.exterior.xy',
'nho.Poppleton.exterior.xy',
'nho.Port_Covington.exterior.xy',
'nho.Pulaski_Industrial_Area.exterior.xy',
'nho.Purnell.exterior.xy',
'nho.Radnor_Winston.exterior.xy',
'nho.Ramblewood.exterior.xy',
'nho.Reisterstown_Station.exterior.xy',
'nho.Remington.exterior.xy',
'nho.Reservoir_Hill.exterior.xy',
'nho.Richnor_Springs.exterior.xy',
'nho.RidgelyS_Delight.exterior.xy',
'nho.Riverside.exterior.xy',
'nho.Rognel_Heights.exterior.xy',
'nho.Roland_Park.exterior.xy',
'nho.Rosebank.exterior.xy',
'nho.Rosemont.exterior.xy',
'nho.Rosemont_East.exterior.xy',
'nho.Rosemont_Homeowners_Tenants.exterior.xy',
'nho.Sabina_Mattfeldt.exterior.xy',
'nho.Saint_Agnes.exterior.xy',
'nho.Saint_Helena.exterior.xy',
'nho.Saint_Josephs.exterior.xy',
'nho.Saint_Paul.exterior.xy',
'nho.Sandtown_Winchester.exterior.xy',
'nho.Seton_Business_Park.exterior.xy',
'nho.Seton_Hill.exterior.xy',
'nho.Sharp_Leadenhall.exterior.xy',
'nho.Shipley_Hill.exterior.xy',
'nho.South_Baltimore.exterior.xy',
'nho.South_Clifton_Park.exterior.xy',
'nho.Spring_Garden_Industrial_Area.exterior.xy',
'nho.Stadium_Area.exterior.xy',
'nho.Stonewood_Pentwood_Winston.exterior.xy',
'nho.Taylor_Heights.exterior.xy',
'nho.Ten_Hills.exterior.xy',
'nho.The_Orchards.exterior.xy',
'nho.Towanda_Grantley.exterior.xy',
'nho.Tremont.exterior.xy',
'nho.Tuscany_Canterbury.exterior.xy',
'nho.Union_Square.exterior.xy',
'nho.University_Of_Maryland.exterior.xy',
'nho.Uplands.exterior.xy',
'nho.Upper_Fells_Point.exterior.xy',
'nho.Upton.exterior.xy',
'nho.Villages_Of_Homeland.exterior.xy',
'nho.Violetville.exterior.xy',
'nho.Wakefield.exterior.xy',
'nho.Walbrook.exterior.xy',
'nho.Waltherson.exterior.xy',
'nho.Washington_Hill.exterior.xy',
'nho.Washington_Village_Pigtown.exterior.xy',
'nho.Waverly.exterior.xy',
'nho.West_Arlington.exterior.xy',
'nho.West_Forest_Park.exterior.xy',
'nho.West_Hills.exterior.xy',
'nho.Westfield.exterior.xy',
'nho.Westgate.exterior.xy',
'nho.Westport.exterior.xy',
'nho.Wilhelm_Park.exterior.xy',
'nho.Wilson_Park.exterior.xy',
'nho.Winchester.exterior.xy',
'nho.Windsor_Hills.exterior.xy',
'nho.Winston_Govans.exterior.xy',
'nho.Woodberry.exterior.xy',
'nho.Woodbourne_Heights.exterior.xy',
'nho.Woodbourne_Mccabe.exterior.xy',
'nho.Woodmere.exterior.xy',
'nho.Wrenlane.exterior.xy',
'nho.Wyman_Park.exterior.xy',
'nho.Wyndhurst.exterior.xy',
'nho.Yale_Heights.exterior.xy',
'nho.York_Homeland.exterior.xy',
]
k=1
#for line in list:
#    print('x'+str(k)+',y'+str(k)+' = '+line)
#    k = k + 1

    
#for j in range(1,279):
#    print('plt.plot(x'+str(j)+',y'+str(j)+')')

x1,y1 = nho.Abell.exterior.xy
x2,y2 = nho.Allendale.exterior.xy
x3,y3 = nho.Arcadia.exterior.xy
x4,y4 = nho.Arlington.exterior.xy
x5,y5 = nho.Armistead_Gardens.exterior.xy
x6,y6 = nho.Ashburton.exterior.xy
x7,y7 = nho.Baltimore_Highlands.exterior.xy
x8,y8 = nho.Barclay.exterior.xy
x9,y9 = nho.Barre_Circle.exterior.xy
x10,y10 = nho.Bayview.exterior.xy
x11,y11 = nho.Beechfield.exterior.xy
x12,y12 = nho.Belair_Edison.exterior.xy
x13,y13 = nho.Belair_Parkside.exterior.xy
x14,y14 = nho.Bellona_Gittings.exterior.xy
x15,y15 = nho.Belvedere.exterior.xy
x16,y16 = nho.Berea.exterior.xy
x17,y17 = nho.Better_Waverly.exterior.xy
x18,y18 = nho.Beverly_Hills.exterior.xy
x19,y19 = nho.Biddle_Street.exterior.xy
x20,y20 = nho.Blythewood.exterior.xy
x21,y21 = nho.Bolton_Hill.exterior.xy
x22,y22 = nho.Boyd_Booth.exterior.xy
x23,y23 = nho.Brewers_Hill.exterior.xy
x24,y24 = nho.Bridgeview_Greenlawn.exterior.xy
x25,y25 = nho.Broadway_East.exterior.xy
x26,y26 = nho.Broening_Manor.exterior.xy
x27,y27 = nho.Brooklyn.exterior.xy
x28,y28 = nho.Burleith_Leighton.exterior.xy
x29,y29 = nho.ButcherS_Hill.exterior.xy
x30,y30 = nho.Callaway_Garrison.exterior.xy
x31,y31 = nho.Cameron_Village.exterior.xy
x32,y32 = nho.Canton.exterior.xy
x33,y33 = nho.Canton_Industrial_Area.exterior.xy
x34,y34 = nho.Care.exterior.xy
x35,y35 = nho.Carroll_Park.exterior.xy
x36,y36 = nho.Carroll_South_Hilton.exterior.xy
x37,y37 = nho.Carroll___Camden_Industrial_Area.exterior.xy
x38,y38 = nho.Carrollton_Ridge.exterior.xy
x39,y39 = nho.Cedarcroft.exterior.xy
x40,y40 = nho.Cedmont.exterior.xy
x41,y41 = nho.Cedonia.exterior.xy
x42,y42 = nho.Central_Forest_Park.exterior.xy
x43,y43 = nho.Central_Park_Heights.exterior.xy
x44,y44 = nho.Charles_North.exterior.xy
x45,y45 = nho.Charles_Village.exterior.xy
x46,y46 = nho.Cherry_Hill.exterior.xy
x47,y47 = nho.Cheswolde.exterior.xy
x48,y48 = nho.Chinquapin_Park.exterior.xy
x49,y49 = nho.Clifton_Park.exterior.xy
x50,y50 = nho.Coldspring.exterior.xy
x51,y51 = nho.Coldstream_Homestead_Montebello.exterior.xy
x52,y52 = nho.Concerned_Citizens_Of_Forest_Park.exterior.xy
x53,y53 = nho.Coppin_HeightsAsh_Co_East.exterior.xy
x54,y54 = nho.Cross_Country.exterior.xy
x55,y55 = nho.Cross_Keys.exterior.xy
x56,y56 = nho.Curtis_Bay.exterior.xy
x57,y57 = nho.Curtis_Bay_Industrial_Area.exterior.xy
x58,y58 = nho.Cylburn.exterior.xy
x59,y59 = nho.Darley_Park.exterior.xy
x60,y60 = nho.Dickeyville.exterior.xy
x61,y61 = nho.Dolfield.exterior.xy
x62,y62 = nho.Dorchester.exterior.xy
x63,y63 = nho.Downtown.exterior.xy
x64,y64 = nho.Downtown_West.exterior.xy
x65,y65 = nho.Druid_Heights.exterior.xy
x66,y66 = nho.Druid_Hill_Park.exterior.xy
x67,y67 = nho.Dunbar_Broadway.exterior.xy
x68,y68 = nho.Dundalk_Marine_Terminal.exterior.xy
x69,y69 = nho.East_Arlington.exterior.xy
x70,y70 = nho.East_Baltimore_Midway.exterior.xy
x71,y71 = nho.Easterwood.exterior.xy
x72,y72 = nho.Eastwood.exterior.xy
x73,y73 = nho.Edgewood.exterior.xy
x74,y74 = nho.Edmondson_Village.exterior.xy
x75,y75 = nho.Ednor_Gardens_Lakeside.exterior.xy
x76,y76 = nho.Ellwood_Park_Monument.exterior.xy
x77,y77 = nho.Evergreen.exterior.xy
x78,y78 = nho.Evergreen_Lawn.exterior.xy
x79,y79 = nho.Evesham_Park.exterior.xy
x80,y80 = nho.Fairfield_Area.exterior.xy
x81,y81 = nho.Fairmont.exterior.xy
x82,y82 = nho.Fallstaff.exterior.xy
x83,y83 = nho.Federal_Hill.exterior.xy
x84,y84 = nho.Fells_Point.exterior.xy
x85,y85 = nho.Forest_Park.exterior.xy
x86,y86 = nho.Forest_Park_Golf_Course.exterior.xy
x87,y87 = nho.Four_By_Four.exterior.xy
x88,y88 = nho.Frankford.exterior.xy
x89,y89 = nho.Franklin_Square.exterior.xy
x90,y90 = nho.Franklintown.exterior.xy
x91,y91 = nho.Franklintown_Road.exterior.xy
x92,y92 = nho.Garwyn_Oaks.exterior.xy
x93,y93 = nho.Gay_Street.exterior.xy
x94,y94 = nho.Glen.exterior.xy
x95,y95 = nho.Glen_Oaks.exterior.xy
x96,y96 = nho.Glenham_Belhar.exterior.xy
x97,y97 = nho.Graceland_Park.exterior.xy
x98,y98 = nho.Greektown.exterior.xy
x99,y99 = nho.Greenmount_Cemetery.exterior.xy
x100,y100 = nho.Greenmount_West.exterior.xy
x101,y101 = nho.Greenspring.exterior.xy
x102,y102 = nho.Grove_Park.exterior.xy
x103,y103 = nho.Guilford.exterior.xy
x104,y104 = nho.Gwynns_Falls.exterior.xy
x105,y105 = nho.Gwynns_Falls_Leakin_Park.exterior.xy
x106,y106 = nho.Hamilton_Hills.exterior.xy
x107,y107 = nho.Hampden.exterior.xy
x108,y108 = nho.Hanlon_Longwood.exterior.xy
x109,y109 = nho.Harlem_Park.exterior.xy
x110,y110 = nho.Harwood.exterior.xy
x111,y111 = nho.Hawkins_Point.exterior.xy
x112,y112 = nho.Heritage_Crossing.exterior.xy
x113,y113 = nho.Herring_Run_Park.exterior.xy
x114,y114 = nho.Highlandtown.exterior.xy
x115,y115 = nho.Hillen.exterior.xy
x116,y116 = nho.Hoes_Heights.exterior.xy
x117,y117 = nho.Holabird_Industrial_Park.exterior.xy
x118,y118 = nho.Hollins_Market.exterior.xy
x119,y119 = nho.Homeland.exterior.xy
x120,y120 = nho.Hopkins_Bayview.exterior.xy
x121,y121 = nho.Howard_Park.exterior.xy
x122,y122 = nho.Hunting_Ridge.exterior.xy
x123,y123 = nho.Idlewood.exterior.xy
x124,y124 = nho.Inner_Harbor.exterior.xy
x125,y125 = nho.Irvington.exterior.xy
x126,y126 = nho.Johns_Hopkins_Homewood.exterior.xy
x127,y127 = nho.Johnston_Square.exterior.xy
x128,y128 = nho.Jones_Falls_Area.exterior.xy
x129,y129 = nho.Jonestown.exterior.xy
x130,y130 = nho.Kenilworth_Park.exterior.xy
x131,y131 = nho.Kernewood.exterior.xy
x132,y132 = nho.Keswick.exterior.xy
x133,y133 = nho.Kresson.exterior.xy
x134,y134 = nho.Lake_Evesham.exterior.xy
x135,y135 = nho.Lake_Walker.exterior.xy
x136,y136 = nho.Lakeland.exterior.xy
x137,y137 = nho.Langston_Hughes.exterior.xy
x138,y138 = nho.Lauraville.exterior.xy
x139,y139 = nho.Levindale.exterior.xy
x140,y140 = nho.Liberty_Square.exterior.xy
x141,y141 = nho.Little_Italy.exterior.xy
x142,y142 = nho.Loch_Raven.exterior.xy
x143,y143 = nho.Locust_Point.exterior.xy
x144,y144 = nho.Locust_Point_Industrial_Area.exterior.xy
x145,y145 = nho.Lower_Edmondson_Village.exterior.xy
x146,y146 = nho.Lower_Herring_Run_Park.exterior.xy
x147,y147 = nho.Loyola_Notre_Dame.exterior.xy
x148,y148 = nho.Lucille_Park.exterior.xy
x149,y149 = nho.Madison_Eastend.exterior.xy
x150,y150 = nho.Madison_Park.exterior.xy
x151,y151 = nho.Mayfield.exterior.xy
x152,y152 = nho.Mcelderry_Park.exterior.xy
x153,y153 = nho.Medfield.exterior.xy
x154,y154 = nho.Medford.exterior.xy
x155,y155 = nho.Mid_Govans.exterior.xy
x156,y156 = nho.Mid_Town_Belvedere.exterior.xy
x157,y157 = nho.Middle_Branch_Reedbird_Parks.exterior.xy
x158,y158 = nho.Middle_East.exterior.xy
x159,y159 = nho.Midtown_Edmondson.exterior.xy
x160,y160 = nho.Millhill.exterior.xy
x161,y161 = nho.Milton_Montford.exterior.xy
x162,y162 = nho.Mondawmin.exterior.xy
x163,y163 = nho.Montebello.exterior.xy
x164,y164 = nho.Moravia_Walther.exterior.xy
x165,y165 = nho.Morgan_Park.exterior.xy
x166,y166 = nho.Morgan_State_University.exterior.xy
x167,y167 = nho.Morrell_Park.exterior.xy
x168,y168 = nho.Mosher.exterior.xy
x169,y169 = nho.Mount_Holly.exterior.xy
x170,y170 = nho.Mount_Vernon.exterior.xy
x171,y171 = nho.Mount_Washington.exterior.xy
x172,y172 = nho.Mount_Winans.exterior.xy
x173,y173 = nho.Mt_Pleasant_Park.exterior.xy
x174,y174 = nho.New_Northwood.exterior.xy
x175,y175 = nho.New_Southwest_Mount_Clare.exterior.xy
x176,y176 = nho.North_Harford_Road.exterior.xy
x177,y177 = nho.North_Roland_Park_Poplar_Hill.exterior.xy
x178,y178 = nho.Northwest_Community_Action.exterior.xy
x179,y179 = nho.ODonnell_Heights.exterior.xy
x180,y180 = nho.Oakenshawe.exterior.xy
x181,y181 = nho.Oaklee.exterior.xy
x182,y182 = nho.Old_Goucher.exterior.xy
x183,y183 = nho.Oldtown.exterior.xy
x184,y184 = nho.Oliver.exterior.xy
x185,y185 = nho.Orangeville.exterior.xy
x186,y186 = nho.Orangeville_Industrial_Area.exterior.xy
x187,y187 = nho.Orchard_Ridge.exterior.xy
x188,y188 = nho.Original_Northwood.exterior.xy
x189,y189 = nho.Otterbein.exterior.xy
x190,y190 = nho.Overlea.exterior.xy
x191,y191 = nho.Panway_Braddish_Avenue.exterior.xy
x192,y192 = nho.Park_Circle.exterior.xy
x193,y193 = nho.Parklane.exterior.xy
x194,y194 = nho.Parkside.exterior.xy
x195,y195 = nho.Parkview_Woodbrook.exterior.xy
x196,y196 = nho.Patterson_Park.exterior.xy
x197,y197 = nho.Patterson_Park_Neighborhood.exterior.xy
x198,y198 = nho.Patterson_Place.exterior.xy
x199,y199 = nho.Pen_Lucy.exterior.xy
x200,y200 = nho.Penn_Fallsway.exterior.xy
x201,y201 = nho.Penn_North.exterior.xy
x202,y202 = nho.Penrose_Fayette_Street_Outreach.exterior.xy
x203,y203 = nho.Perkins_Homes.exterior.xy
x204,y204 = nho.Perring_Loch.exterior.xy
x205,y205 = nho.Pimlico_Good_Neighbors.exterior.xy
x206,y206 = nho.Pleasant_View_Gardens.exterior.xy
x207,y207 = nho.Poppleton.exterior.xy
x208,y208 = nho.Port_Covington.exterior.xy
x209,y209 = nho.Pulaski_Industrial_Area.exterior.xy
x210,y210 = nho.Purnell.exterior.xy
x211,y211 = nho.Radnor_Winston.exterior.xy
x212,y212 = nho.Ramblewood.exterior.xy
x213,y213 = nho.Reisterstown_Station.exterior.xy
x214,y214 = nho.Remington.exterior.xy
x215,y215 = nho.Reservoir_Hill.exterior.xy
x216,y216 = nho.Richnor_Springs.exterior.xy
x217,y217 = nho.RidgelyS_Delight.exterior.xy
x218,y218 = nho.Riverside.exterior.xy
x219,y219 = nho.Rognel_Heights.exterior.xy
x220,y220 = nho.Roland_Park.exterior.xy
x221,y221 = nho.Rosebank.exterior.xy
x222,y222 = nho.Rosemont.exterior.xy
x223,y223 = nho.Rosemont_East.exterior.xy
x224,y224 = nho.Rosemont_Homeowners_Tenants.exterior.xy
x225,y225 = nho.Sabina_Mattfeldt.exterior.xy
x226,y226 = nho.Saint_Agnes.exterior.xy
x227,y227 = nho.Saint_Helena.exterior.xy
x228,y228 = nho.Saint_Josephs.exterior.xy
x229,y229 = nho.Saint_Paul.exterior.xy
x230,y230 = nho.Sandtown_Winchester.exterior.xy
x231,y231 = nho.Seton_Business_Park.exterior.xy
x232,y232 = nho.Seton_Hill.exterior.xy
x233,y233 = nho.Sharp_Leadenhall.exterior.xy
x234,y234 = nho.Shipley_Hill.exterior.xy
x235,y235 = nho.South_Baltimore.exterior.xy
x236,y236 = nho.South_Clifton_Park.exterior.xy
x237,y237 = nho.Spring_Garden_Industrial_Area.exterior.xy
x238,y238 = nho.Stadium_Area.exterior.xy
x239,y239 = nho.Stonewood_Pentwood_Winston.exterior.xy
x240,y240 = nho.Taylor_Heights.exterior.xy
x241,y241 = nho.Ten_Hills.exterior.xy
x242,y242 = nho.The_Orchards.exterior.xy
x243,y243 = nho.Towanda_Grantley.exterior.xy
x244,y244 = nho.Tremont.exterior.xy
x245,y245 = nho.Tuscany_Canterbury.exterior.xy
x246,y246 = nho.Union_Square.exterior.xy
x247,y247 = nho.University_Of_Maryland.exterior.xy
x248,y248 = nho.Uplands.exterior.xy
x249,y249 = nho.Upper_Fells_Point.exterior.xy
x250,y250 = nho.Upton.exterior.xy
x251,y251 = nho.Villages_Of_Homeland.exterior.xy
x252,y252 = nho.Violetville.exterior.xy
x253,y253 = nho.Wakefield.exterior.xy
x254,y254 = nho.Walbrook.exterior.xy
x255,y255 = nho.Waltherson.exterior.xy
x256,y256 = nho.Washington_Hill.exterior.xy
x257,y257 = nho.Washington_Village_Pigtown.exterior.xy
x258,y258 = nho.Waverly.exterior.xy
x259,y259 = nho.West_Arlington.exterior.xy
x260,y260 = nho.West_Forest_Park.exterior.xy
x261,y261 = nho.West_Hills.exterior.xy
x262,y262 = nho.Westfield.exterior.xy
x263,y263 = nho.Westgate.exterior.xy
x264,y264 = nho.Westport.exterior.xy
x265,y265 = nho.Wilhelm_Park.exterior.xy
x266,y266 = nho.Wilson_Park.exterior.xy
x267,y267 = nho.Winchester.exterior.xy
x268,y268 = nho.Windsor_Hills.exterior.xy
x269,y269 = nho.Winston_Govans.exterior.xy
x270,y270 = nho.Woodberry.exterior.xy
x271,y271 = nho.Woodbourne_Heights.exterior.xy
x272,y272 = nho.Woodbourne_Mccabe.exterior.xy
x273,y273 = nho.Woodmere.exterior.xy
x274,y274 = nho.Wrenlane.exterior.xy
x275,y275 = nho.Wyman_Park.exterior.xy
x276,y276 = nho.Wyndhurst.exterior.xy
x277,y277 = nho.Yale_Heights.exterior.xy
x278,y278 = nho.York_Homeland.exterior.xy 

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
plt.plot(x8,y8)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)
plt.plot(x13,y13)
plt.plot(x14,y14)
plt.plot(x15,y15)
plt.plot(x16,y16)
plt.plot(x17,y17)
plt.plot(x18,y18)
plt.plot(x19,y19)
plt.plot(x20,y20)
plt.plot(x21,y21)
plt.plot(x22,y22)
plt.plot(x23,y23)
plt.plot(x24,y24)
plt.plot(x25,y25)
plt.plot(x26,y26)
plt.plot(x27,y27)
plt.plot(x28,y28)
plt.plot(x29,y29)
plt.plot(x30,y30)
plt.plot(x31,y31)
plt.plot(x32,y32)
plt.plot(x33,y33)
plt.plot(x34,y34)
plt.plot(x35,y35)
plt.plot(x36,y36)
plt.plot(x37,y37)
plt.plot(x38,y38)
plt.plot(x39,y39)
plt.plot(x40,y40)
plt.plot(x41,y41)
plt.plot(x42,y42)
plt.plot(x43,y43)
plt.plot(x44,y44)
plt.plot(x45,y45)
plt.plot(x46,y46)
plt.plot(x47,y47)
plt.plot(x48,y48)
plt.plot(x49,y49)
plt.plot(x50,y50)
plt.plot(x51,y51)
plt.plot(x52,y52)
plt.plot(x53,y53)
plt.plot(x54,y54)
plt.plot(x55,y55)
plt.plot(x56,y56)
plt.plot(x57,y57)
plt.plot(x58,y58)
plt.plot(x59,y59)
plt.plot(x60,y60)
plt.plot(x61,y61)
plt.plot(x62,y62)
plt.plot(x63,y63)
plt.plot(x64,y64)
plt.plot(x65,y65)
plt.plot(x66,y66)
plt.plot(x67,y67)
plt.plot(x68,y68)
plt.plot(x69,y69)
plt.plot(x70,y70)
plt.plot(x71,y71)
plt.plot(x72,y72)
plt.plot(x73,y73)
plt.plot(x74,y74)
plt.plot(x75,y75)
plt.plot(x76,y76)
plt.plot(x77,y77)
plt.plot(x78,y78)
plt.plot(x79,y79)
plt.plot(x80,y80)
plt.plot(x81,y81)
plt.plot(x82,y82)
plt.plot(x83,y83)
plt.plot(x84,y84)
plt.plot(x85,y85)
plt.plot(x86,y86)
plt.plot(x87,y87)
plt.plot(x88,y88)
plt.plot(x89,y89)
plt.plot(x90,y90)
plt.plot(x91,y91)
plt.plot(x92,y92)
plt.plot(x93,y93)
plt.plot(x94,y94)
plt.plot(x95,y95)
plt.plot(x96,y96)
plt.plot(x97,y97)
plt.plot(x98,y98)
plt.plot(x99,y99)
plt.plot(x100,y100)
plt.plot(x101,y101)
plt.plot(x102,y102)
plt.plot(x103,y103)
plt.plot(x104,y104)
plt.plot(x105,y105)
plt.plot(x106,y106)
plt.plot(x107,y107)
plt.plot(x108,y108)
plt.plot(x109,y109)
plt.plot(x110,y110)
plt.plot(x111,y111)
plt.plot(x112,y112)
plt.plot(x113,y113)
plt.plot(x114,y114)
plt.plot(x115,y115)
plt.plot(x116,y116)
plt.plot(x117,y117)
plt.plot(x118,y118)
plt.plot(x119,y119)
plt.plot(x120,y120)
plt.plot(x121,y121)
plt.plot(x122,y122)
plt.plot(x123,y123)
plt.plot(x124,y124)
plt.plot(x125,y125)
plt.plot(x126,y126)
plt.plot(x127,y127)
plt.plot(x128,y128)
plt.plot(x129,y129)
plt.plot(x130,y130)
plt.plot(x131,y131)
plt.plot(x132,y132)
plt.plot(x133,y133)
plt.plot(x134,y134)
plt.plot(x135,y135)
plt.plot(x136,y136)
plt.plot(x137,y137)
plt.plot(x138,y138)
plt.plot(x139,y139)
plt.plot(x140,y140)
plt.plot(x141,y141)
plt.plot(x142,y142)
plt.plot(x143,y143)
plt.plot(x144,y144)
plt.plot(x145,y145)
plt.plot(x146,y146)
plt.plot(x147,y147)
plt.plot(x148,y148)
plt.plot(x149,y149)
plt.plot(x150,y150)
plt.plot(x151,y151)
plt.plot(x152,y152)
plt.plot(x153,y153)
plt.plot(x154,y154)
plt.plot(x155,y155)
plt.plot(x156,y156)
plt.plot(x157,y157)
plt.plot(x158,y158)
plt.plot(x159,y159)
plt.plot(x160,y160)
plt.plot(x161,y161)
plt.plot(x162,y162)
plt.plot(x163,y163)
plt.plot(x164,y164)
plt.plot(x165,y165)
plt.plot(x166,y166)
plt.plot(x167,y167)
plt.plot(x168,y168)
plt.plot(x169,y169)
plt.plot(x170,y170)
plt.plot(x171,y171)
plt.plot(x172,y172)
plt.plot(x173,y173)
plt.plot(x174,y174)
plt.plot(x175,y175)
plt.plot(x176,y176)
plt.plot(x177,y177)
plt.plot(x178,y178)
plt.plot(x179,y179)
plt.plot(x180,y180)
plt.plot(x181,y181)
plt.plot(x182,y182)
plt.plot(x183,y183)
plt.plot(x184,y184)
plt.plot(x185,y185)
plt.plot(x186,y186)
plt.plot(x187,y187)
plt.plot(x188,y188)
plt.plot(x189,y189)
plt.plot(x190,y190)
plt.plot(x191,y191)
plt.plot(x192,y192)
plt.plot(x193,y193)
plt.plot(x194,y194)
plt.plot(x195,y195)
plt.plot(x196,y196)
plt.plot(x197,y197)
plt.plot(x198,y198)
plt.plot(x199,y199)
plt.plot(x200,y200)
plt.plot(x201,y201)
plt.plot(x202,y202)
plt.plot(x203,y203)
plt.plot(x204,y204)
plt.plot(x205,y205)
plt.plot(x206,y206)
plt.plot(x207,y207)
plt.plot(x208,y208)
plt.plot(x209,y209)
plt.plot(x210,y210)
plt.plot(x211,y211)
plt.plot(x212,y212)
plt.plot(x213,y213)
plt.plot(x214,y214)
plt.plot(x215,y215)
plt.plot(x216,y216)
plt.plot(x217,y217)
plt.plot(x218,y218)
plt.plot(x219,y219)
plt.plot(x220,y220)
plt.plot(x221,y221)
plt.plot(x222,y222)
plt.plot(x223,y223, '-k')
plt.plot(x224,y224)
plt.plot(x225,y225)
plt.plot(x226,y226)
plt.plot(x227,y227)
plt.plot(x228,y228)
plt.plot(x229,y229)
plt.plot(x230,y230)
plt.plot(x231,y231)
plt.plot(x232,y232)
plt.plot(x233,y233)
plt.plot(x234,y234)
plt.plot(x235,y235)
plt.plot(x236,y236)
plt.plot(x237,y237)
plt.plot(x238,y238)
plt.plot(x239,y239)
plt.plot(x240,y240)
plt.plot(x241,y241)
plt.plot(x242,y242)
plt.plot(x243,y243)
plt.plot(x244,y244)
plt.plot(x245,y245)
plt.plot(x246,y246)
plt.plot(x247,y247)
plt.plot(x248,y248)
plt.plot(x249,y249)
plt.plot(x250,y250)
plt.plot(x251,y251)
plt.plot(x252,y252)
plt.plot(x253,y253)
plt.plot(x254,y254)
plt.plot(x255,y255)
plt.plot(x256,y256)
plt.plot(x257,y257)
plt.plot(x258,y258)
plt.plot(x259,y259)
plt.plot(x260,y260)
plt.plot(x261,y261)
plt.plot(x262,y262)
plt.plot(x263,y263)
plt.plot(x264,y264)
plt.plot(x265,y265)
plt.plot(x266,y266)
plt.plot(x267,y267)
plt.plot(x268,y268)
plt.plot(x269,y269)
plt.plot(x270,y270)
plt.plot(x271,y271)
plt.plot(x272,y272)
plt.plot(x273,y273)
plt.plot(x274,y274)
plt.plot(x275,y275)
plt.plot(x276,y276)
plt.plot(x277,y277)
plt.plot(x278,y278)

plt.show()