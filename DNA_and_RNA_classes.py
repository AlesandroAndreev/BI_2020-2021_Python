class DNA:

    def __init__(self, seq):

        if all(nuc in 'AaTtGgCc' for nuc in seq):
            self.seq = seq
        else:
            raise TypeError('This is not DNA!')

        self.nucleotide_index = 0

        self.dna_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',
                               'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
        self.dna_to_rna_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A',
                                      'a': 'u', 'c': 'g', 'g': 'c', 't': 'a'}

    def __eq__(self, other):
        if isinstance(other, DNA) or isinstance(other, RNA):
            if other.seq == self.seq:
                return True
        return False

    def __key(self):
        return self.seq

    def __hash__(self):
        return hash(self.__key())

    def __next__(self):
        if self.nucleotide_index < len(self.seq):
            nucleotide = self.seq[self.nucleotide_index]
            self.nucleotide_index += 1
            return nucleotide

    def reverse_complement(self):
        revers_seq = self.seq[::-1]
        complement = [self.dna_complement[base] for base in revers_seq]
        return DNA(''.join(complement))

    def transcribe(self):
        dna_to_rna_seq = \
            [self.dna_to_rna_complement[base] for base in self.seq[::-1]]
        return RNA(''.join(dna_to_rna_seq))

    def gc_content(self):
        count = 0
        if len(self.seq) != 0:
            for i in self.seq:
                if i in ["G", "C", "g", "c"]:
                    count += 1
            return round((count/len(self.seq))*100, 2)
        else:
            return 0


class RNA:

    def __init__(self, seq):

        if all(nuc in 'AaUuGgCc' for nuc in seq):
            self.seq = seq
        else:
            raise TypeError('This is not RNA!')

        self.nucleotide_index = 0

        self.rna_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A',
                               'a': 'u', 'c': 'g', 'g': 'c', 'u': 'a'}

    def __eq__(self, other):
        if isinstance(other, DNA) or isinstance(other, RNA):
            if other.seq == self.seq:
                return True
        return False

    def __key(self):
        return self.seq

    def __hash__(self):
        return hash(self.__key())

    def __next__(self):
        if self.nucleotide_index < len(self.seq):
            nucleotide = self.seq[self.nucleotide_index]
            self.nucleotide_index += 1
            return nucleotide

    def reverse_complement(self):
        revers_seq = self.seq[::-1]
        complement = [self.rna_complement[base] for base in revers_seq]
        return RNA(''.join(complement))

    def gc_content(self):
        count = 0
        if len(self.seq) != 0:
            for i in self.seq:
                if i in ["G", "C", "g", "c"]:
                    count += 1
            return round((count/len(self.seq))*100, 2)
        else:
            return 0
