########################################################################
# R.A.Borrelli
# @TheDoctorRAB 
# rev.15.January.2015
# v1.0
########################################################################
#
# The Weibull distribution is used for a lot of failure analysis.
# It is very flexible for a wide variety of failure scenarios. 
#
########################################################################
#
# Objective
# Test the Weibull distribution to determine if it can be used to simulate equipment failure in pyroprocessing.
# There is not any real life data for failures with pyroprocessing equipment. 
# The Weibull distribution is a typical go-to for these kinds of conditions. 
# 
########################################################################
#
# Current conditions
# Use the two-parameter Weibull distribution.
#
# probability density function
# f(t)=(beta/eta)*((time/eta)**(beta-1))*exp(-(time/eta)**(beta))
#
# cumulative density function
# F(t)=1-exp(-(time/eta)**(beta))
#
# F(T) gives the probability of a failure occuring within time <= T. 
# This is also called the unreliability function, Q(t).
#
# Typically, failure data is fit to the distribution to determine beta and eta.
#
########################################################################
#
# Assumption
# beta = 1 for random failures.
# Then, MTTF = eta for this case and the failure rate = 1/eta.
# With increasing time, failure is more likely due to wearing out of the equipment.
#
########################################################################
#
#
#
####### imports
import numpy
import matplotlib
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
########################################################################
#
#
#
####### set plot font
matplotlib.rcParams.update({'font.size': 14})
#######
#
#
#
####### initialize and set variables
operation_time=0
facility_operation=250
failure_event=False
failure_rate=float(1)/float(30)
delta_time=numpy.random.random_sample() # the time interval is set randomly
maintenance_time=2*delta_time
failure_counter=0
probability_density_function=0
unreliability_function=0
weibull_beta=1
weibull_eta=(1)/(failure_rate)
failure_testing=0
#######
#
#
#
####### controls
pdf_output=open('pdf.out','w+')
unreliability_function_output=open('unreliability_function.out','w+')
#######
#
#
#
########################################################################
#
#
#
#######
probability_density_function=(weibull_beta/weibull_eta)*((operation_time/weibull_eta)**(weibull_beta-1))*numpy.exp(-(operation_time/weibull_eta)**(weibull_beta)) # pdf at operation_time = 0
unreliability_function=1-numpy.exp(-(operation_time/weibull_eta)**(weibull_beta)) # unreliability function at operation_time = 0 
###
pdf_output.write(str.format('%.4f'%operation_time)+'\t'+str.format('%.4f'%probability_density_function)+'\n')
unreliability_function_output.write(str.format('%.4f'%operation_time)+'\t'+str.format('%.4f'%unreliability_function)+'\n')
#######
#
#
#
####### operation time loop
while(operation_time<=facility_operation):
    operation_time=operation_time+delta_time
###
    probability_density_function=(weibull_beta/weibull_eta)*((operation_time/weibull_eta)**(weibull_beta-1))*numpy.exp(-(operation_time/weibull_eta)**(weibull_beta)) 
    unreliability_function=1-numpy.exp(-(operation_time/weibull_eta)**(weibull_beta))
###
    pdf_output.write(str.format('%.4f'%operation_time)+'\t'+str.format('%.4f'%probability_density_function)+'\n')
    unreliability_function_output.write(str.format('%.4f'%operation_time)+'\t'+str.format('%.4f'%unreliability_function)+'\n')
###
#
### set random number for failure testing
# the random number is sampled from the uniform distribution (0,1)
# this is compared to the unreliability function to determine if a failure occurs
    failure_testing=numpy.random.rand()
###
    print '%.4f'%operation_time,'%.4f'%unreliability_function,'%.4f'%failure_testing
####### end operation loop
#
#
#
#######
pdf_output.close()
unreliability_function_output.close()
#######
#
#
#
########################################################################
#
#
#
####### pdf plot
fig,left_axis=plot.subplots()
title='Weibull pdf'
xtitle='Operation time'
ytitle='f(t)'
###
plot.title(title)
left_axis.set_xlabel(xtitle)
left_axis.set_ylabel(ytitle)
###
xmin=0
xmax=operation_time
ymin=-0.001 
ymax=failure_rate
###
xmajortick=0.1*facility_operation
ymajortick=0.01
###
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
###
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
###
left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
left_axis.grid(which='major',axis='both',linewidth='1.1')
###
pdf_graph=numpy.loadtxt('pdf.out',dtype=float,delimiter='\t')
###
left_axis.plot(pdf_graph[:,0],pdf_graph[:,1])
###
plot.get_current_fig_manager().resize(1600,900)
plot.savefig(title)
plot.show()
#######
#
#
######## unreliability function plot
fig,left_axis=plot.subplots()
title='Weibull unreliability function'
xtitle='Operation time'
ytitle='Q(t)'
###
plot.title(title)
left_axis.set_xlabel(xtitle)
left_axis.set_ylabel(ytitle)
###
xmin=0
xmax=operation_time
ymin=-0.01
ymax=1.01
###
xmajortick=0.1*facility_operation
ymajortick=0.05
###
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
###
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
###
left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
left_axis.grid(which='major',axis='both',linewidth='1.1')
###
unreliability_function_graph=numpy.loadtxt('unreliability_function.out',dtype=float,delimiter='\t')
###
left_axis.plot(unreliability_function_graph[:,0],unreliability_function_graph[:,1])
###
plot.get_current_fig_manager().resize(1600,900)
plot.savefig(title)
plot.show()
#######
#
#
########################################################################
#
# EOF
#
########################################################################
