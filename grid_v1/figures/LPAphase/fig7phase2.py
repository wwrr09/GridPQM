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
#V2=np.loadtxt('T50mu237.2/V_u237.1.dat')
#V3=np.loadtxt('T50mu237.2/V_u237.2.dat')
#V4=np.loadtxt('T50mu237.2/V_u237.3.dat')
#V5=np.loadtxt('T50mu237.2/V_u237.4.dat')
#V6=np.loadtxt('T50mu237.2/V_u237.5.dat')

#print(mu120[:,2])
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(mu[0:49],T[0:49],':b',linewidth=2,markersize=4,label=r'2nd order phase transform')
ax1.plot(mu[48:64],T[48:64],'-r',linewidth=1,markersize=4,label=r'1st order phase transform')
ax1.plot(mu[64:69],T[64:69],':b',linewidth=2,markersize=4)
ax1.plot(mu[69:80],T[69:80],'-r',linewidth=1,markersize=4)
ax1.plot(mu[64],T[64],'xg',linewidth=2,markersize=4)
ax1.plot(mu[48],T[48],'xg',linewidth=2,markersize=4,label=r'Critical endpoint')
print(T[48])
#ax1.plot(mu[26:28],T[26:28],'-r',linewidth=2,markersize=4)
#ax1.plot(phi,V2,'-',linewidth=1,markersize=2,label=r'$\mu=237.1 [\mathrm{MeV}]$')
#ax1.plot(phi,V3,'-',linewidth=1,markersize=2,label=r'$\mu=237.2 [\mathrm{MeV}]$')
#ax1.plot(phi,V4,'-',linewidth=1,markersize=2,label=r'$\mu=237.3 [\mathrm{MeV}]$')
#ax1.plot(phi,V5,'-',linewidth=1,markersize=2,label=r'$\mu=237.4 [\mathrm{MeV}]$')
#ax1.plot(phi,V6,'-',linewidth=1,markersize=2,label=r'$\mu=237.5 [\mathrm{MeV}]$')
ax1.axis([0,300,0,150])
#ax1.ticklabel_format(style='scientific', axis='y',scilimits=(-1,0))
#ax1.set_xscale('log')
ax1.set_xlabel('$\mu \,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$T \,[\mathrm{MeV}]$', fontsize=14, color='black')
#plt.text(25,0.8e6,r'$T=50 \mathrm{MeV}$',fontsize=10)
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
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.15, right=0.95, hspace=0.35,
                    wspace=0.35)


fig.savefig("fig7(2).pdf")
