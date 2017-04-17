import random
from time import time
from numpy import exp
import matplotlib.pyplot as plt
import statistics
import json


def ham(x):  # hamiltonian of X'th particle
    return - J * (state[x]*(state[x-1] + state[(x+1) % N])) - state[x] * h


def hamm(x):  # hamiltonian of X'th particle if it had an opposite state
    return - J * (-state[x]*(state[x-1] + state[(x+1) % N])) + state[x] * h


def success(x):
    return x == 1 or random.random() <= x


experiments = {}

#  should be ONE EVER!
J = 1


# for N in [10, 40, 160, 640]:
# for N in [10, 40, 160, 320, 1000]:
for N in [200, 400]:

    experiments[N] = {}

    # h = 0
    # for h in [-10, 0, 0.1, 1, 10, 100]:
    for h in [0, 1, 2, 4, 8]:
        experiments[N][h] = {}

        print()
        # beta = 1/10
        for beta in [100, 30, 10, 3, 1, 0.3, 0.1, 0.03, 0.01, 0.001]:
            # for beta in [10**(i/2-2.5) for i in range(11)]:
            print()
            # meanE = 0
            # meanM = 0
            # experiments[N][h][beta] = {}
            steps = 100*N**2

            experiments[N][h][beta] = {'J': J, "h": h, "beta": beta, 'steps': steps}

            # H(i) = -J * sum(i*j) - h * i
            state = [random.choice([1, -1]) for i in range(N)]
            # state = [1 for i in range(N)]
            # print('state=', state)

            # weird way to store startstate but it works
            # startstate = [x for x in state]
            # experiments[N][h][beta]['startstate'] = startstate
            # current energy value
            energy = sum([ham(i) for i in range(N)])
            # print('E=', energy)

            # list of energy values in order of appearance after thermalization
            evolution = []
            evomag = []
            # for measuring time
            start = time()

            for k in range(steps):
                j = random.randint(0, N-1)
                # print(j)

                if hamm(j) < ham(j):
                    A = 1
                else:
                    A = min(1, exp(-beta*(hamm(j) - ham(j))))

                # print(hamm(j), ham(j), A)
                if success(A):
                    # print('Success')

                    # removing energy that gonna change
                    deltaE = ham(j) + ham(j-1) + ham((j+1) % N)
                    energy -= deltaE
                    # print(deltaE)
                    state[j] *= -1

                    # putting back the new energy
                    deltaE = ham(j) + ham(j-1) + ham((j+1) % N)
                    energy += deltaE
                    # print(deltaE)

                # print('E`=', energy)
                # print(state)
                # print()

                if k > 200*N and k % N == 0:
                    evolution.append(energy)
                    magnetisation = sum(state) / N
                    evomag.append(magnetisation)

                if k == steps-1:
                    print('M=', sum(state))
                # if k > steps - 101:
                #     meanE += energy/100
                #
                #     magnetisation = sum(state) / N
                #
                #     meanM += magnetisation/100

            # final state
            # experiments[N][h][beta]['endstate'] = state
            # print('final state =', state)
            # print()
            # remembering the time for the run
            delta = time() - start

            # writing magnetisation in the end
            # magnetisation = sum(state) / N

            # evolution
            # evomag

            avE = statistics.mean(evolution)
            sigmaE = statistics.stdev(evolution, avE)
            avM = statistics.mean(evomag)
            sigmaM = statistics.stdev(evomag, avM)

            print('N=', N, 'beta=', "%.2f" % beta, 'h=', "%.3f" % h, sep='   ')
            print('mag=', "%.3f" % avM, 'sigmaM=', "%.2f" % sigmaM, '<E>/N=', "%.2f" % (avE/N), 'sigmaE/N=', "%.2f" % (sigmaE/N), sep='   ')
            #  writing evolution in the Dict
            # experiments[N][h][beta]['evolution'] = evolution
            # # writing magnetisation evolution
            # experiments[N][h][beta]['evomag'] = evomag

            # writing time for the run
            experiments[N][h][beta]['time'] = delta


            experiments[N][h][beta]['mag'] = avM
            experiments[N][h][beta]['sigmaM'] = sigmaM
            experiments[N][h][beta]['avE/N'] = avE/N
            experiments[N][h][beta]['sigmaE/N'] = sigmaE/N


    # print()
    # print(delta)

with open('result1D_3.json', 'w') as fp:
    json.dump(experiments, fp)

#
#
# plot = plt.plot(evolution[0:5*N])
# plt.show()
