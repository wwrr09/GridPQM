#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl

mpl.style.use('classic')


# Data for plotting
#phi=np.loadtxt('T100mu/phi.dat')
V1=np.loadtxt('muLPA.dat')
V2=np.loadtxt('muBLPA.dat')
V3=np.loadtxt('muTcLPA.dat')
V4=np.loadtxt('muTc_eta.dat')
V5=np.loadtxt('AA.dat')
V6=np.loadtxt('AA1.dat')
#V5=np.loadtxt('T20mu247/V_u247.1.dat')
#V6=np.loadtxt('T20mu247/V_u247.2.dat')

#print(mu120[:,2])
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(V1,V3,':r',linewidth=1,markersize=2,label=r'LPA')
ax1.plot(V2,V4,':b',linewidth=1,markersize=2,label=r'beyond LPA')
ax1.plot(V6[:,0],V6[:,1],'-',linewidth=1,markersize=2)
ax1.plot(V5[:,0],V5[:,1],'-',linewidth=1,markersize=2)
#ax1.plot(phi,V4/1E6,'-',linewidth=1,markersize=2,label=r'$\mu=205.0 \mathrm{MeV}$')
#ax1.plot(phi,V5,'-',linewidth=1,markersize=2,label=r'$k_{IR}=50 [\mathrm{MeV}]$')
#ax1.plot(phi,V6/1E6,'-',linewidth=1,markersize=2,label=r'$\mu=247.2 [\mathrm{MeV}]$')
ax1.axis([0,1000,0,150])
#ax1.ticklabel_format(style='scientific', axis='y',scilimits=(-1,0))
#ax1.set_xscale('log')
ax1.set_xlabel('$\mu_B \,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$T\ \,[\mathrm{MeV}]$', fontsize=14, color='black')
plt.text(265,80,r'$\frac{\mu_B}{T}=3$',fontsize=10)
plt.text(50,80,r'$\frac{\mu_B}{T}=2$',fontsize=10)
ax1.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

#for ax in fig.axes:
#    ax.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.17, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("fig16curvature.pdf")
