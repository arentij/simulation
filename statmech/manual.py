# 1D problem J=1
#
# During simulations with h=0 was found:
# for L = 50 - 1000 amount of steps for thermalization grows linearly:
# -if we start from random states (hot start) and assume large beta (low temperature) then it takes 10*L steps to reach and stay at -2*L energy
# -if we start from uniform state (cold start) and set low beta (high T) then it takes about 2*L steps to get to <E> ~ 0 (reasonable, because we have a high chance to switch every particle state no matter of hamiltonian, because either way beta is small and A~1)
#
# So we will expect the worse and wait at least 10*L before starting recording every L steps  energies of the system and magnetisation and so on.
#
#
# Observations: high beta > 10 and h=0 with 50% chance give magnetization ~1 and 50% for ~-1
# For high beta and h > 0 magnetization ~1
# As might be expected
#
#
# For L = 100 - 400:
# For h = 0, magnetization stays at +-1 for beta > 1
# For h = 1, magnetization stays at 1 for beta > 0.1
#
#
# For L = 200 - 400
# for high beta magnetization stays at 1
# transition to <sigma> ~ 0 happends when:
# beta < 1 for h=0
# beta < 0.1 for h=1
# beta < 0.03 for h=2
# beta < 0.01 for h=4
# beta ~0.003 for h=8
#
# So we need a higher temperature to make a mess with magnetisation with increasion of magnetic field.
#
#
# 2D model
# with L=100 and matrix 100*100 it takes 50*100*100 steps for termalization
# for L=50 50*50*50 steps
# so thermalization will take 50*L^2 steps, we would double it to 100*L^2
#
# The same parameters appear for transition as in 1D.
#
# For beta less (-0.1) than critical (0.5log2+1)/2  could be observed thermalization <sigma>~0, for beta a bigger (+0.1) than critical, average magnetization trend to go to 1.
#
#
