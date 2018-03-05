$fn=100;

module aimant(a, b, c, d, e) {
    difference(){
        cylinder( h=b, r=a, center=True );
        off=2;
        translate([0,0,-off]){
            cylinder( h=d+2*off, r=c, center=True );
        }
        
    }
};

dec = .4;
 module percage_vis(profondeur, epaisseur){
        epaisseur_vis = 1+dec;
        rayon_vis = 1+dec/2.0;
        rayon_tete_vis = 3.5/2 + dec/2.0;
        taille_ecrou_min = 4.5 + dec;
        taille_ecrou_max = 3.9;
        translate([0, 0,-2]){
            cylinder(h=profondeur+epaisseur+2, r=rayon_vis);
        }
        translate([-taille_ecrou_max/2, -taille_ecrou_min/2,-2]){
        cube([ taille_ecrou_max, taille_ecrou_min, epaisseur_vis+2]);
        }
        translate([0, 0,profondeur+epaisseur-epaisseur_vis]){
         cylinder(h=epaisseur_vis+2, r=rayon_tete_vis);
        }
        translate([0, 0,-2]){
            //cylinder(h=profondeur+epaisseur+2, r=rayon_vis);
            //cylinder(h=epaisseur_vis+2, r=rayon_tete_vis);
        }
 }
        
module socle(profondeur, epaisseur){
    ly = 32;
    lxp = 11.5;
    lxn = 6.5 + 8/2;
    lx = lxp + lxn;
    rayon = 5.5 + dec/2.0;
    vis_centre = 3.8/2.0 + dec/2;
    difference(){
        translate([-lxn, -ly/2, 0]){
            cube([lx, ly, profondeur+epaisseur]);  
        }
        translate([0,0,-1]){
        cylinder(h=profondeur+1, r=rayon);
        }
        cylinder(h=profondeur+epaisseur+2, r=vis_centre);
        
        translate([-6.5, -27/2,0]){
            percage_vis(profondeur, epaisseur);
        }
        translate([6.5, -27/2,0]){
            percage_vis(profondeur, epaisseur);
        }
        translate([-6.5, 27/2,0]){
            percage_vis(profondeur, epaisseur);
        }
       translate([6.5, 27/2,0]){
            percage_vis(profondeur, epaisseur);
        }
    }
}
socle(profondeur=(3.8+1.7+2*dec),epaisseur = 2);
lz = 40 - 32 - 5 + dec;
translate([0,0,-(lz+2)]){
    //socle(profondeur = lz, epaisseur=2 );
 
}
//support();
//aimant( a=20, b=25, c=4, d=14, e=200 );