// Biupiu Blade / Micro-Turbine engineering blockout
// Concept geometry only — not a manufacturing or flight-certified design.
module blade(length=220, chord=42, thickness=6, twist=18) {
  linear_extrude(height=thickness, twist=twist, slices=24)
    polygon([[0,0],[length,0],[length,chord],[0,chord]]);
}
module hub(radius=55, height=35) { cylinder(r=radius, h=height, center=true, $fn=96); }
module rotor(blades=8) { hub(); for (i=[0:blades-1]) rotate([0,0,i*360/blades]) translate([55,-21,0]) blade(); }
rotor();