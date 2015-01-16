########################################################################
# R.A.Borrelli
# @TheDoctorRAB 
# rev.12.January.2015
# v1.1
########################################################################
#
# Routines to simulate failure in general equipment. 
# To be applied to the main code.
# Small-scale testing here, to avoide full operation time, processing, etc.
# This code is not made to have complicated file input, writing, etc.
# Just set whatever variables and go.
#
########################################################################
#
# Objective
# Simulate one random failure within the 'failure period' for each period.
# If the failure rate is 0.1 day^-1; failure 1 occurs at random within 10 days.
# Failure 2 occurs at random from 11 to 20 days; failure 3 from 21 to 30 days, etc.
#
# While this does not simulate 'real' failure, it is needed to compare different facility designs.
#
# So, the Type I error is a design metric for the design because it is quantified over common events.
#
########################################################################
#
# Current conditions
# A single, generalized failure occurs halfway in to the equipment operation time. 
#
########################################################################
#
#
#
####### imports
import numpy
########################################################################
#
#
#
####### initialize and set variables
operation_time=0
facility_operation=15
failure_event=False
failure_probability=0.2
delta_time=numpy.random.random_sample() # the time interval is set randomly
maintenance_time=2*delta_time
failure_counter=0 
#######
#
#
#
########################################################################
#
#
#
####### operation time loop
while(operation_time<=facility_operation):
    operation_time=operation_time+delta_time
    print 'Operation time:','%.4f'%operation_time
    print failure_counter/failure_probability,operation_time,(failure_counter+1)/failure_probability,'\n'
#
    if(failure_counter/failure_probability<operation_time<(failure_counter+1)/failure_probability):
	failure_event=True
	failure_counter+=1
	print 'Failure occurred','#',failure_counter,'\n'
### end if
#
### resolve failure
    if(failure_event==True):
	print 'Peforming maintenance'
	operation_time=operation_time+maintenance_time
	failure_event=False
	print 'Failure resolved'
### end if
#
    print 'End of campaign','Total failure events',failure_counter,'\n'
####### end operation loop
#
#
#
########################################################################
#
# EOF
#
########################################################################
