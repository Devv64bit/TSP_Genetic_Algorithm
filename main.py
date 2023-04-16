import numpy as np
import matplotlib.pyplot as plt


# read target sequence from file
with open('dataset\sequences.txt', 'r') as f:
    target_seq = f.read().strip()


# generate random DNA sequences
np.random.seed(0)
num_sequences = 50
sequence_length = len(target_seq)
sequences = []
for i in range(num_sequences):
    sequence = ""
    for j in range(sequence_length):
        sequence += np.random.choice(['A', 'C', 'G', 'T'])
    sequences.append(sequence)

# genetic algorithm parameters
num_generations = 200
population_size = 130
mutation_rate = 0.02

# fitness function


def fitness(sequence):
    similarity = 0
    for i in range(sequence_length):
        if sequence[i] == target_seq[i]:
            similarity += 1
    return similarity / sequence_length

# crossover function


def crossover(parent1, parent2):
    # select a random crossover point
    crossover_point = np.random.randint(sequence_length)
    # combine the two parents' sequences
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# mutation function


def mutation(sequence):
    if np.random.rand() < mutation_rate:
        i = np.random.randint(sequence_length)
        nucleotides = ['A', 'C', 'G', 'T']
        nucleotides.remove(sequence[i])
        sequence = sequence[:i] + \
            np.random.choice(nucleotides) + sequence[i+1:]
    return sequence


# initialize population
population = []
for i in range(population_size):
    sequence = ""
    for j in range(sequence_length):
        sequence += np.random.choice(['A', 'C', 'G', 'T'])
    population.append(sequence)

# evolve population
fitness_values = np.zeros((num_generations, population_size))
for generation in range(num_generations):
    # evaluate fitness of population
    for i in range(population_size):
        fitness_values[generation, i] = fitness(population[i])
    # select parents
    parent1 = population[np.argmax(fitness_values[generation])]
    fitness_values[generation, np.argmax(fitness_values[generation])] = -1
    parent2 = population[np.argmax(fitness_values[generation])]
    # create new population
    new_population = []
    for i in range(population_size):
        child = crossover(parent1, parent2)
        child = mutation(child)
        new_population.append(child)
    population = new_population
    # plot best sequence
    best_sequence = population[np.argmax(fitness_values[generation])]
    best_similarity = fitness_values[generation,
                                     np.argmax(fitness_values[generation])]
    print("Generation {}: Best Sequence = {}, Similarity = {:.4f}".format(
        generation+1, best_sequence, best_similarity))

# display the final best sequence
best_sequence = population[np.argmax(fitness_values[-1])]
best_similarity = fitness_values[-1, np.argmax(fitness_values[-1])]
print("Final Best Sequence = {}, Similarity = {:.4f}".format(
    best_sequence, best_similarity))

# plot heat map
plt.imshow(fitness_values, cmap='inferno', interpolation='nearest')
plt.xlabel('Sequence')
plt.ylabel('Generation')
plt.title('Fitness Heat Map')
plt.colorbar()
plt.show()
