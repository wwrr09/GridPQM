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
mu=np.loadtxt('mu.dat')
T=np.loadtxt('T.dat')
#V2=np.loadtxt('T20mu247/V_u246.7.dat')
#V3=np.loadtxt('T20mu247/V_u246.9.dat')
#V4=np.loadtxt('T20mu247/V_u247.dat')
#V5=np.loadtxt('T20mu247/V_u247.1.dat')
#V6=np.loadtxt('T20mu247/V_u247.2.dat')

#print(mu120[:,2])
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(mu[0:30],T[0:30],':b',linewidth=2,markersize=4,label=r'2nd order phase transform')
print(T[30])
ax1.plot(mu[30:42],T[30:42],'-r',linewidth=1,markersize=4,label=r'1st order phase transform')
ax1.plot(mu[30],T[30],'xg',linewidth=2,markersize=4,label=r'Critical endpoint')
#ax1.plot(phi,V2,'-',linewidth=1,markersize=2,label=r'$k_{IR}=20 [\mathrm{MeV}]$')
#ax1.plot(phi,V3,'-',linewidth=1,markersize=2,label=r'$\mu=246.9 [\mathrm{MeV}]$')
#ax1.plot(phi,V4,'-',linewidth=1,markersize=2,label=r'$\mu=247.0 [\mathrm{MeV}]$')
#ax1.plot(phi,V5,'-',linewidth=1,markersize=2,label=r'$k_{IR}=50 [\mathrm{MeV}]$')
#ax1.plot(phi,V6,'-',linewidth=1,markersize=2,label=r'$\mu=247.2 [\mathrm{MeV}]$')
ax1.axis([0,300,0,150])
#ax1.ticklabel_format(style='scientific', axis='y',scilimits=(-1,0))
#ax1.set_xscale('log')
ax1.set_xlabel('$\mu \,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$T \,[\mathrm{MeV}]$', fontsize=14, color='black')
#plt.text(50,1.5e6,r'$T=20 \mathrm{MeV}$',fontsize=10)
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


fig.savefig("beyondLPA.pdf")
