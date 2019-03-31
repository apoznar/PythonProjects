from itertools import product

k = 23  # AA  homozygous dominant
m = 17  # Aa  heterozygous
n = 27  # aa  homozygous recessive

population = (['AA'] * k) + (['Aa'] * m) + (['aa'] * n)

all_children = []
for parent1 in population:
    # remove selected parent from population.
    chosen = population[:]
    chosen.remove(parent1)
    for parent2 in chosen:
        # get all possible children from 2 parents. Punnet square
        children = product(parent1, parent2)
        all_children.extend([''.join(c) for c in children])

dominants = filter(lambda c: 'A' in c, all_children)
# float for python2
print(float(len(list(dominants))) / len(all_children))
# 0.7833333
