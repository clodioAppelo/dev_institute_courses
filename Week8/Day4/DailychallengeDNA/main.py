# Instructions :
# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.
#
# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.
#
# Implement these classes as you see fit.
#
# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the
# probability for its DNA to mutate.
#
# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s.
# Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).
import random

class Gene:
    def __init__(self, geneValue):
        self.geneValue = geneValue

    def can_mutate(self, flip):
        self.geneValue = random.choice([random.randrange(0.2)], flip)


class Chromosome:
    def __init__(self, genes):
        if len(genes) != 10:
            raise Exception("The Chromosome must have ten genes")
        else:
            self.genes = genes

    def can_mutate(self, flip):
        for i in range(len(self.genes)):
            self.genes[i] = self.genes[i].can_mutate(flip)

    def is_ones(self):
        for gene in self.genes:
            if gene.gene == 0:
                return False

        return True


class DNA:
        def __init__(self, chromosomes):
            if not len(chromosomes) == 10:
                raise Exception("The DNA must contain 10 chromosomes")

            self.chromosomes = chromosomes

        def mutate(self, probability: 0.5):
            for i in range(len(self.chromosomes)):
                self.chromosomes[i] = self.chromosomes[i].mutate(probability)

        def is_ones(self):
            for chromosome in self.chromosomes:
                if not chromosome.chromos():
                    return False

            return True


class Organism:
    def __init__(self, dna: DNA, probability):
        self.dna = dna
        self.probability = probability
        self.generations_count = 0

    def mutate(self):
        self.dna.mutate(self.probability)
        if self.dna.is_all_ones():
            print(f'the generations count is {self.generations_count}')
            return

        self.mutate()



