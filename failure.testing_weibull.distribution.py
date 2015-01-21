########################################################################
# R.A.Borrelli
# @TheDoctorRAB 
# rev.21.January.2015
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
from win32api import GetSystemMetrics
from matplotlib.ticker import MultipleLocator
########################################################################
#
#
#
####### controls
matplotlib.rcParams.update({'font.size': 14}) # set plot font
width=GetSystemMetrics (0) # get screen resolution
height=GetSystemMetrics (1) # get screen resolution
#######
#
#
#
####### initialize and set variables
operation_time=0
facility_operation=10
failure_event=False
failure_rate=float(1)/float(3)
delta_time=numpy.random.random_sample() # the time interval is set randomly
maintenance_time=2*delta_time
failure_counter=0
probability_density_function=0
unreliability_function=0
weibull_beta=1
weibull_eta=(1)/(failure_rate)
failure_testing=0
maintenance_time=delta_time+numpy.random.random_sample()
failure_time=0
campaign=1
probability_density_function_evaluate=0
unreliability_function_evaluate=0
probability_density_function_failure_evaluate=0
unreliability_function_failure_evaluate=0
#######
#
#
#
####### write files
def write_files(time_domain,campaign,pdf_evaluate,cdf_evaluate,failure_counter,failure_testing,time_domain_output,campaign_output,pdf_output,cdf_output,failure_record_output):
###
    time_domain_output.write(str.format('%.4f'%time_domain)+'\n')
    campaign_output.write(str.format('%.4f'%time_domain)+'\t'+str.format('%i'%campaign)+'\n')
    pdf_output.write(str.format('%.4f'%time_domain)+'\t'+str.format('%.4f'%pdf_evaluate)+'\n')
    unreliability_function_output.write(str.format('%.4f'%time_domain)+'\t'+str.format('%.4f'%cdf_evaluate)+'\n')
    failure_record_output.write(str.format('%.4f'%time_domain)+'\t'+str.format('%.4f'%failure_testing)+'\t'+str.format('%.4f'%cdf_evaluate)+'\t'+str.format('%i'%failure_counter)+'\n')
###
    return(time_domain_output,campaign_output,pdf_output,cdf_output,failure_record_output)
#######
#
#
#
####### probability density function
def probability_density_function(time_domain,weibull_beta,weibull_eta):
###
    function_evaluate=(weibull_beta/weibull_eta)*((time_domain/weibull_eta)**(weibull_beta-1))*numpy.exp(-(time_domain/weibull_eta)**(weibull_beta))
###
    return(function_evaluate)
#######
#
#
#
####### unreliability function
def unreliability_function(time_domain,weibull_beta,weibull_eta):
###
    function_evaluate=1-numpy.exp(-(time_domain/weibull_eta)**(weibull_beta)) 
###
    return(function_evaluate)
#######
#
#
#
#######
####### pdf plot
#def plot_pdf(operation_time,failure_rate,plotdata):
###
#fig,left_axis=plot.subplots()
#title='Weibull pdf'
#xtitle='Operation time'
#ytitle='f(t)'
###
#plot.title(title)
#left_axis.set_xlabel(xtitle)
#left_axis.set_ylabel(ytitle)
###
#xmin=0
#xmax=operation_time
#ymin=-0.001 
#ymax=failure_rate
###
#xmajortick=0.1*facility_operation
#ymajortick=0.01
#xminortick=0.25*xmajortick
#yminortick=0.25*ymajortick
###
#plot.xlim(xmin,xmax)
#left_axis.axis(ymin=ymin,ymax=ymax)
###
#left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
#left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
#left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
#left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
###
#left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
#left_axis.grid(which='major',axis='both',linewidth='1.1')
###
#pdf_graph=numpy.loadtxt('pdf.out',dtype=float,delimiter='\t')
###
#left_axis.plot(pdf_graph[:,0],pdf_graph[:,1])
###
#plot.get_current_fig_manager().resize(width,height)
#plot.gcf().set_size_inches((0.01*width),(0.01*height))
#plot.savefig(title)
#plot.show()
#######
#
#
#
#
#
#
####### open files 
operation_time_output=open('operation.time.out','w+')
failure_time_output=open('failure.time.out','w+')
campaign_output=open('campaign.out','w+')
probability_density_function_output=open('pdf.out','w+')
unreliability_function_output=open('unreliability.function.out','w+')
failure_record_output=open('failure.record.out','w+')
probability_density_function_failure_output=open('pdf.failure.out','w+')
unreliability_function_failure_output=open('unreliability.failure.function.out','w+')
#######
#
#
#
########################################################################
#
#
#
####### time = 0
probability_density_function_evaluate=probability_density_function(operation_time,weibull_beta,weibull_eta)
unreliability_function_evaluate=unreliability_function(operation_time,weibull_beta,weibull_eta)
probability_density_function_failure_evaluate=probability_density_function(failure_time,weibull_beta,weibull_eta)
unreliability_function_failure_evaluate=unreliability_function(failure_time,weibull_beta,weibull_eta)
###
operation_time_output,campaign_output,probability_density_function_output,unreliability_function_output,failure_record_output=write_files(operation_time,campaign,probability_density_function_evaluate,unreliability_function_evaluate,failure_counter,failure_testing,operation_time_output,campaign_output,probability_density_function_output,unreliability_function_output,failure_record_output)
#######
#
#
#
####### operation time loop
#
#
#
while(operation_time<=facility_operation):
    print 'Campaign:',campaign
###
    operation_time=operation_time+delta_time
    failure_time=failure_time+delta_time
###
    probability_density_function_evaluate=probability_density_function(operation_time,weibull_beta,weibull_eta)
    unreliability_function_evaluate=unreliability_function(operation_time,weibull_beta,weibull_eta)
#    probability_density_function_failure_evaluate=probability_density_function(failure_time,weibull_beta,weibull_eta)
#    unreliability_function_failure_evaluate=unreliability_function(failure_time,weibull_beta,weibull_eta)
###
    operation_time_output,campaign_output,probability_density_function_output,unreliability_function_output,failure_record_output=write_files(operation_time,campaign,probability_density_function_evaluate,unreliability_function_evaluate,failure_counter,failure_testing,operation_time_output,campaign_output,probability_density_function_output,unreliability_function_output,failure_record_output)
###
#
### set random number for failure testing
# the random number is sampled from the uniform distribution (0,1)
# this is compared to the unreliability function to determine if a failure occurs
    failure_testing=numpy.random.rand()
###
    if(failure_testing<=unreliability_function_evaluate):
	failure_event=True
	failure_counter+=1
    else: 
	failure_event=False
### end if
#
###
    print 'Operation time','%.4f'%operation_time,'\t','Failure time','%.4f'%failure_time
    print 'Failure test generator','%.4f'%failure_testing,'\t','Failure probability','%.4f'%unreliability_function_evaluate,'\t','Failure?',failure_event,'\t','Total failures',failure_counter
###
#
### resolve failure
# if there is a failure, the equipment is repaired so the existing distribution does not apply anymore
# the failure distribution is then 'reset'
###
    while(failure_event==True):
	print 'Performing maintenance'
	failure_time=0
	operation_time=operation_time+maintenance_time
	failure_time=failure_time+maintenance_time
	failure_event=False
	probability_density_function_evaluate=probability_density_function(operation_time,weibull_beta,weibull_eta)
	unreliability_function_evaluate=unreliability_function(operation_time,weibull_beta,weibull_eta)
### end failure loop
#
###
    print 'End campaign:',campaign,'\n'
    campaign+=1
###
#
#
#
####### end operation loop
#
#
#
####### close files
operation_time_output.close()
campaign_output.close()
probability_density_function_output.close()
unreliability_function_output.close()
failure_record_output.close()
failure_time_output.close()
probability_density_function_failure_output.close()
unreliability_function_failure_output.close()
#######
#
#
#
# make a multi failure pdf, unreliability plot and a single pdf, unreliability plot
#
########################################################################
#
#
#
#
#
#
#
#
#
#######

#
#
######## unreliability function plot
#fig,left_axis=plot.subplots()
#title='Weibull unreliability function'
#xtitle='Operation time'
#ytitle='Q(t)'
###
#plot.title(title)
#left_axis.set_xlabel(xtitle)
#left_axis.set_ylabel(ytitle)
###
#xmin=0
#xmax=operation_time
#ymin=-0.01
#ymax=1.01
###
#xmajortick=0.1*facility_operation
#ymajortick=0.05
#xminortick=0.25*xmajortick
#yminortick=0.25*ymajortick
###
#plot.xlim(xmin,xmax)
#left_axis.axis(ymin=ymin,ymax=ymax)
###
#left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
#left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
#left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
#left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
###
#left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
#left_axis.grid(which='major',axis='both',linewidth='1.1')
###
#unreliability_function_graph=numpy.loadtxt('unreliability.function.out',dtype=float,delimiter='\t')
###
#left_axis.plot(unreliability_function_graph[:,0],unreliability_function_graph[:,1])
###
#plot.get_current_fig_manager().resize(width,height)
#plot.gcf().set_size_inches((0.01*width),(0.01*height))
#plot.savefig(title)
#plot.show()
#######
#
#
#
####### failure record plot
#fig,left_axis=plot.subplots()
#title='Failure record'
#xtitle='Operation time'
#ytitle='Failures'
###
#plot.title(title)
#left_axis.set_xlabel(xtitle)
#left_axis.set_ylabel(ytitle)
###
#xmin=0
#xmax=operation_time
#ymin=-0.03
#ymax=failure_counter+0.03
###
#xmajortick=0.1*facility_operation
#ymajortick=1
#xminortick=0.25*xmajortick
###
#plot.xlim(xmin,xmax)
#left_axis.axis(ymin=ymin,ymax=ymax)
###
#left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
#left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
#left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
###
#left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
#left_axis.grid(which='major',axis='both',linewidth='1.1')
###
#failure_record_graph=numpy.loadtxt('failure.record.out',dtype=float,delimiter='\t')
###
#left_axis.plot(failure_record_graph[:,0],failure_record_graph[:,3])
###
#plot.get_current_fig_manager().resize(width,height)
#plot.gcf().set_size_inches((0.01*width),(0.01*height))
#plot.savefig(title)
#plot.show()
#######
#
#
#
########################################################################
#
# EOF
#
########################################################################
