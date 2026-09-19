// Biupiu marine propulsor blockout — concept/research geometry only.
module hub(r=38,h=70){ cylinder(r=r,h=h,center=true,$fn=96); }
module blade(len=260,width=70,thick=10){ linear_extrude(height=thick,center=true) polygon([[0,0],[len*0.82,width*0.20],[len,width],[len*0.92,0]]); }
module propulsor(n=5){ hub(); for(i=[0:n-1]) rotate([0,0,i*360/n]) translate([35,-15,0]) rotate([0,8,0]) blade(); }
propulsor();