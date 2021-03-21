class NucleicAcids:

    def __init__ (self, seq):
        self.seq = seq
        self.dna_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        self.rna_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        self.dna_to_rna_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

    def __eq__(self, other):
         if isinstance(other, DNA) or isinstance(other, RNA):
            if other.seq == self.seq:
                return True
         return False

    def __key(self):
        return self.seq

    def __hash__(self):
        return hash(self.__key())

    def gc_content(self):

        count = 0

        for i in self.seq:
            if i in ["G", "C"]:
                count += 1

        return round((count/len(self.seq))*100, 2)

class RNA(NucleicAcids):

   def __init__(self, seq):
       super().__init__(seq)

   def reverse_complement(self):
       revers_seq = self.seq[::-1]
       complement =  [self.rna_complement[base] for base in revers_seq]
       return RNA(''.join(complement))

class DNA(NucleicAcids):

    def __init__(self, seq):
        super().__init__(seq)

    def reverse_complement(self):
        revers_seq = self.seq[::-1]
        complement =  [self.dna_complement[base] for base in revers_seq]
        return RNA(''.join(complement))

    def transcribe(self):
        dna_to_rna_seq = [self.dna_to_rna_complement[base] for base in self.seq[::-1]]
        return RNA(''.join(dna_to_rna_seq))

print("Cod for test")

print("write your DNA set: ")
dna_set = [DNA(seq) for seq in input().split()]

print("write your RNA set: ")
rna_set = [RNA(seq) for seq in input().split()]

print("Lets start test!")

if len(dna_set) != 0:

    for number, dna in enumerate(dna_set):

        print("\nInfo about your DNA number {0}\n".format(number + 1))

        print("Your sequence {0}".format(dna.seq))
        print("Your sequence type is {0}".format(type(dna)))
        print("Hash your DNA will {0}\n".format(dna.__hash__()))

        print("Is it true that different objects created from the same "
              "sequence are equal? It is {0}".format(dna == DNA(dna.seq)))
        print("And if we compare it with a reverse compliment, "
              "then there will already be {0}\n".format(dna == dna.reverse_complement()))

        print("By the way! And if we write the reverse compliment,"
              " it will look like {0}".format(dna.reverse_complement().seq))
        print("And its type is {0}".format(type(dna.reverse_complement())))
        print("Hash your revers compliment will {0}\n".format(dna.reverse_complement().__hash__()))

        print("If we use transcribe sequence looks like {0}".format(dna.transcribe().seq))
        print("Type of your transcribe sequence is {0}".format(type(dna.transcribe())))
        print("Hash of your transcribe sequence will {0}\n".format(dna.transcribe().__hash__()))
else:
    print("You haven't entered DNA sequences!:(")

if len(rna_set) != 0:

    for number, rna in enumerate(rna_set):

        print("\nInfo about your RNA number {0}\n".format(number + 1))

        print("Your sequence {0}".format(rna.seq))
        print("Your sequence type is {0}".format(type(rna)))
        print("Hash your RNA will {0}\n".format(DNA(rna).__hash__()))

        print("Is it true that different objects created from the same "
              "sequence are equal? It is {0}".format(rna == RNA(rna.seq)))
        print("And if we compare it with a reverse compliment, "
              "then there will already be {0}\n".format(rna == rna.reverse_complement()))

        print("By the way! And if we write the reverse compliment,"
              " it will look like {0}".format(rna.reverse_complement().seq))
        print("And its type is {0}".format(type(rna.reverse_complement())))
        print("Hash your revers compliment will {0}\n".format(rna.reverse_complement().__hash__()))
else:
    print("You haven't entered RNA sequences!:(")
