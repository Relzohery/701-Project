
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:07:22 2016

@author: rabab
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import os
import nice_plots

nice_plots.init_nice_plots()


 
""" This part extracts the compositions of different isotopes from serpent output files and 
arrange them into arrays  for each istope which their width is the  number irradiation steps and their height
is the number of decay steps
"""

f=[]



U_234=np.zeros([28,22])
U_235=np.zeros([28,22])
U_236=np.zeros([28,22])
U_238=np.zeros([28,22])
Np_237=np.zeros([28,22])
Pu_238=np.zeros([28,22])
Pu_239=np.zeros([28,22])
Pu_240=np.zeros([28,22])
Pu_241=np.zeros([28,22])
Pu_242=np.zeros([28,22])
Am_241=np.zeros([28,22])
Am_243=np.zeros([28,22])
Tc_99=np.zeros ([28,22])
Cs_133=np.zeros([28,22])
Cs_135=np.zeros([28,22])
Nd_143=np.zeros([28,22])
Nd_145=np.zeros([28,22])
Sm_147=np.zeros([28,22])
Sm_149=np.zeros([28,22])
Sm_150=np.zeros([28,22])
Sm_151=np.zeros([28,22])
Sm_152=np.zeros([28,22])
Eu_153=np.zeros([28,22])
Gd_155=np.zeros([28,22])
Mo_95=np.zeros ([28,22])
Ru_103=np.zeros([28,22])
Xe_135=np.zeros([28,22])
Pm_147=np.zeros([28,22])
Rh_103=np.zeros([28,22])
Xe_131=np.zeros([28,22])
Cs_137=np.zeros([28,22])
Cs_134=np.zeros([28,22])
Eu_154=np.zeros([28,22])
Ru_106=np.zeros([28,22])
Ce_144=np.zeros([28,22])
Nb_95=np.zeros([28,22])
        
isotopes=[U_234,U_235,U_236,U_238,Np_237,Pu_238,Pu_239,Pu_240,Pu_241,Pu_242,Am_241,Am_243,
         Tc_99,Cs_133,Cs_135,Nd_143,Nd_145,Sm_147,Sm_149,Sm_150,Sm_151,Sm_152,Eu_153,Gd_155,
         Mo_95,Ru_103,Xe_135,Pm_147,Rh_103,Xe_131,Cs_137,Cs_134,Eu_154,Ru_106,Ce_144,Nb_95]
         
rootdir='/home/rabab/701/project/compositions'
filelist=os.walk(rootdir)
dirpath, dirs,files = filelist.next()

names = ['composition{}_dep.m'.format(i) for i in range(1,22)]
for k in names:
   f.append(open(dirpath+'/'+k,'r').readlines()[127:163])
  
f=np.array(f)
for j in range(len(isotopes)):
        isotopes[j][:,0]=np.array(float((f[:,j][0].split( )[0])))   # zero irradiation time column  
for j in range(len(isotopes)):
    for i in range (1,22):
        isotopes[j][:,i]=(np.array(map(float,(f[:,j][i-1].split( )[1:-2]))))

decay_days= open("composition1_dep.m","r").readlines()[706: ]
for lines in decay_days:
     Decay_days=np.array(map(float,lines.split( )[4:-1]))-(365)    # Subtracting the irradiation time 


class isotopes(object):
    """ This class encapsulates all the istopic compositions, each istopic composition is an attribute of the class;
    it also contains the methods Gen_Compositions with different forms to calculate the istopc compositions 
    at any intermediate point between the the existing ones """
    
    def __init__(self):
        self.U_234=U_234
        self.U_235=U_235
        self.U_236=U_236
        self.U_238=U_238
        self.Np_237=Np_237
        self.Pu_238=Pu_238
        self.Pu_239=Pu_239
        self.Pu_240=Pu_240
        self.Pu_241=Pu_241
        self.Pu_242=Pu_242
        self.Am_241=Am_241
        self.Am_243=Am_243
        self.Tc_99=Tc_99
        self.Cs_133=Cs_133
        self.Cs_135=Cs_135
        self.Nd_143=Nd_143
        self.Nd_145=Nd_145
        self.Sm_147=Sm_147
        self.Sm_149=Sm_149
        self.Sm_150=Sm_150
        self.Sm_151=Sm_151
        self.Sm_152=Sm_152
        self.Eu_153=Eu_153
        self.Gd_155=Gd_155
        self.Mo_95=Mo_95
        self.Ru_103=Ru_103
        self.Xe_135=Xe_135
        self.Pm_147=Pm_147
        self.Rh_103=Rh_103
        self.Xe_131=Xe_131
        self.Cs_137=Cs_137
        self.Cs_134=Cs_134
        self.Eu_154=Eu_154
        self.Ru_106=Ru_106
        self.Ce_144=Ce_144
        self.Nb_95=Nb_95
        self.isotopes=[U_234,U_235,U_236,U_238,Np_237,Pu_238,Pu_239,Pu_240,Pu_241,Pu_242,Am_241,Am_243,
                 Tc_99,Cs_133,Cs_135,Nd_143,Nd_145,Sm_147,Sm_149,Sm_150,Sm_151,Sm_152,Eu_153,Gd_155,
                 Mo_95,Ru_103,Xe_135,Pm_147,Rh_103,Xe_131,Cs_137,Cs_134,Eu_154,Ru_106,Ce_144,Nb_95]
                 
        self.names=["U-234","U-235","U-236","U-238","Np-237","Pu-238","Pu-239","Pu-240","Pu-241","Pu-242","Am-241","Am-243",
                 "Tc-99","Cs-133","Cs-135","Nd-143","Nd-145","Sm-147","Sm-149","Sm-150","Sm-151","Sm-152","Eu-153","Gd-155",
        "M0-95","Ru-103","Xe-135","Pm-147","Rh-103","Xe-131","Cs-137","Cs-134","Eu-154","Ru-106","Ce-144","Nb-95"]
        
        self.Irradiation_days=np.array([0,3.65000E+02,7.30000E+02,1.09500E+03,1.46000E+03,1.82500E+03,2.19000E+03 ,
                                   2.55500E+03,2.92000E+03,3.28500E+03,3.65000E+03,4.38000E+03,5.11000E+03,5.84000E+03,
                                   6.57000E+03,7.30000E+03,8.03000E+03,9.49000E+03,1.09500E+04,1.24100E+04,1.38700E+04,
                                   1.53300E+04 ]) 
        self.Irradiation_years=self.Irradiation_days/365
        self.Decay_days=Decay_days
        self.Decay_years=Decay_days/365
        
    def Gen_compositions(self,r,d): 
        """ in the interpolation function "Z" should have the shape(x.size,y.size), because the istopes arrays have
        the shape (decay time steps, irradiation time steps), the decay_days is the first argument in the interpolation
        class, but the arguments order is flipped in the outer function (Gen_compositions) for more convenience """
        
        compositions =[ ]
        
        for i in range(36):
                    Interp=interpolate.RectBivariateSpline(self.Decay_days,self.Irradiation_days,self.isotopes[i],kx=1,ky=1)
                    compositions.append(Interp(d,r)[0][0])
        return compositions
        
    def Gen_compositions_years(self,r,d):
       
       
        compositions =[ ]
        
        for i in range(36):
                    Interp=interpolate.RectBivariateSpline(self.Decay_years,self.Irradiation_years,self.isotopes[i],kx=1,ky=1)
                    compositions.append(Interp(d,r)[0][0])
        return compositions
        
    def Gen_compositions_years_days(self,r,d): 
        compositions =[ ]
        for i in range(36):
                    Interp=interpolate.RectBivariateSpline(self.Decay_days,self.Irradiation_years,self.isotopes[i],kx=1,ky=1)
                    compositions.append(Interp(d,r)[0][0])
        return compositions
        
    def Gen_compositions_days_years(self,r,d): 
        compositions =[ ]
        for i in range(36):
                    Interp=interpolate.RectBivariateSpline(self.Decay_years,self.Irradiation_days,self.isotopes[i],kx=1,ky=1)
                    compositions.append(Interp(d,r)[0][0])
        return compositions


        
        
if __name__=="__main__":
    isotope=isotopes( )
    
    
    II=np.arange(0,1.53300E+04,10)  # more points within the range of the actual Irradiation times
    dd=np.arange(0,14965,10)        # more points within the range of the actual Decay times.
    Interp=interpolate.RectBivariateSpline(isotope.Decay_days,isotope.Irradiation_days,isotope.Cs_134,kx=3,ky=3)
    
    Interpolated=Interp(dd,II)
    labels=("1 ","5 ", "10", "15" ,"20","25","30","35","40")
    values=(365, 1825 ,3650, 5475,7300,9125,10950,12775,14600)
    plt.figure(1)
    plt.plot(isotope.Decay_days,isotope.Cs_134[:,1],"ro",label="Serpent Data")
    plt.plot(dd,Interpolated[:,36],label="Interpolation Curve")   # Interpolated[:,36] is approximately the composition at 360 days.
    plt.title("$^{134}$Cs  concentration Vs Decay time")
    plt.legend()
    plt.xticks(values,labels)
    plt.xlabel("Decay Time in years")
    plt.ylabel("Atomic Concentration")
    plt.savefig("Cs134,decay")
    
    
    
    plt.figure(2)
    plt.plot(isotope.Irradiation_days,Cs_134[0,:],"ro",label="Serpent Data")
    plt.plot(II,Interpolated[0,:],label="Interpolation Curve")
    plt.title("$^{134}$Cs concentration Vs Irradiation time")
    plt.legend()
    plt.xlabel("Irradiation Time in years")
    plt.ylabel("Atomic Concentration")
    plt.xticks(values,labels)
    plt.savefig("Cs134,irradiaton")

