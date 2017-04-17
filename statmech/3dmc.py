import random
from time import time
from numpy import exp
import matplotlib.pyplot as plt
import statistics
import json
from d3state015 import st015_50


def mag():
    mm = 0
    for x1 in range(L):
        for y1 in range(L):
            for z1 in range(L):
                mm += state[x1][y1][z1]
    return mm


def Estate():
    return [[[ham(x1, y1, z1) for x1 in range(L)] for y1 in range(L)] for z1 in range(L)]


def ham(x1, y1, z1):
    su = state[x1-1][y1][z1] + \
         state[(x1 + 1) % L][y1][z1] + \
         state[x1][y1-1][z1] + \
         state[x1][(y1 + 1) % L][z1] + \
         state[x1][y1][z1-1] + \
         state[x1][y1][(z1 + 1) % L]

    return - J * state[x1][y1][z1] * su - state[x1][y1][z1] * h


def hamm(x1, y1, z1):
    return -ham(x1, y1, z1)


def success(x1):
    return x1 == 1 or random.random() <= x1


def writing_json():

    energy_evolution = {'E': energy_state, 'beta': beta_state}
    with open('MC_3D_Estates_L50_b015_025_2L.json', 'w') as fp:
        json.dump(energy_evolution, fp)

    print('done dumping', time() - start)
    return True


experiments = {}

#  J should be ONE EVER!
J = 1
h0 = 0
beta0 = 0.15

energy_state = []
beta_state = []

# for N in [10, 40, 160, 640]:
# for N in [10, 40, 160, 320, 1000]:

for L in [50]:
    N = L ** 3

    experiments[N] = {}

    for h2 in [h0]:
        experiments[N][h2] = {}
        h = h2
        evolution = []
        evomag = []

        # print()
        for beta2 in [beta0]:
            steps = 800 * L ** 3
            # steps = 1
            beta = beta2
            experiments[N][h2][beta] = {'J': J, "h": h, "beta": beta, 'steps': steps}

            # state = [[[random.choice([-1, 1]) for i in range(L)] for j in range(L)] for k in range(L)]
            state = st015_50

            # Calculating the sum of the energies
            energy = 0
            for y in range(L):
                for x in range(L):
                    for z in range(L):
                        energy += ham(x, y, z)

            mmag = mag()
            print('<m0>=', mmag / N, '   beta=', beta, '   <E0>=', energy/N)

            # list of energy values in order of appearance after thermalization

            # for measuring time
            start = time()

            # dbeta = 0.3
            dbeta = 0.15
            ldbeta = 0.6

            dh = 0
            ldh = 0.5
            for k in range(steps):
                if k % (steps//20) == 0:
                    print("%.0f" % (k / steps*100), "%.2f" % (time() - start))

                if steps / 20 < k <= (steps * (1 - ldbeta)) // 1:
                    beta += dbeta / (1 - ldbeta - 0.05) / steps
                    h += dh / steps / (1 - ldh - 0.05)

                i2 = random.randint(0, L - 1)
                j2 = random.randint(0, L - 1)
                k2 = random.randint(0, L - 1)

                # print(i2, j2, k2)

                if ham(i2, j2, k2) > 0:
                    A = 1
                else:
                    A = min(1, exp(beta * 2*ham(i2, j2, k2)))

                # print(A)
                if success(A):
                    # print('Success')

                    # removing energy that is gonna change
                    deltaE = ham(i2, j2, k2) + ham(i2-1, j2, k2) + ham(i2, j2-1, k2) + ham(i2, j2, k2-1) + \
                             ham((i2 + 1) % L, j2, k2) + ham(i2, (j2 + 1) % L, k2) + ham(i2, j2, (k2 + 1) % L)
                    energy -= deltaE
                    # print('dE-=', deltaE)
                    mmag -= 2*state[i2][j2][k2]

                    state[i2][j2][k2] *= -1


                    # putting back the new energy
                    deltaE = ham(i2, j2, k2) + ham(i2 - 1, j2, k2) + ham(i2, j2 - 1, k2) + ham(i2, j2, k2 - 1) + \
                             ham((i2 + 1) % L, j2, k2) + ham(i2, (j2 + 1) % L, k2) + ham(i2, j2, (k2 + 1) % L)
                    energy += deltaE
                    # print('dE+=', deltaE)

                # print('E`=', energy)
                # print(state)
                # print()

                # if k > 0 and k % ((L ** 3 / 128) // 1) == 0:
                if k > 0 and k % (steps//400) == 0:
                    evolution.append(energy/N)
                    energy_state.append(Estate())
                    beta_state.append(beta)
                    evomag.append(mmag/N)

            # print('M=', mag()/L**3)
            print('<m>=', mag() / L ** 3, '   beta=', beta, '   <E>=', energy/L**3)


            # final state
            # experiments[N][h2][beta]['endstate'] = state
            # print('final state =', state)
            # print()
            # remembering the time for the run
            delta = time() - start
            # print('Time', delta)
            # writing magnetisation in the end
            # magnetisation = sum(state) / N

            # evolution
            # evomag

            # avE = statistics.mean(evolution)
            # sigmaE = statistics.stdev(evolution, avE)
            # avM = statistics.mean(evomag)
            # sigmaM = statistics.stdev(evomag, avM)

            # print('N=', N, 'beta=', "%.2f" % beta, 'h=', "%.3f" % h, sep='   ')
            # print('mag=', "%.3f" % avM, 'sigmaM=', "%.2f" % sigmaM, '<E>/N=', "%.2f" % (avE/N), 'sigmaE/N=', "%.2f" % (sigmaE/N), sep='   ')
            #  writing evolution in the Dict
            # experiments[N][h2][beta]['evolution'] = evolution
            # # writing magnetisation evolution
            # experiments[N][h2][beta]['evomag'] = evomag



    # print()
    # print(delta)
    print('DONE CALCULATING', time() - start)
    # print(state[0])

# with open('result2D_4.json', 'w') as fp:
#     json.dump(experiments, fp)


# WRITING A JSON FILE!!!!!!!!!!!!
writing_json()

print(state)
#
#
plot = plt.plot(evolution)
plot2 = plt.plot(evomag)
plot3 = plt.plot(beta_state)
plt.show()


# for i in range(L):
#     for j in range(L):
#         print(state[i][j], '   ', Estate()[i][j])
#     print()
