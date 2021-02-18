def generate(n):

    def list_to_string(list_to_convert):
        return ''.join([str(elem) for elem in list_to_convert])

    from itertools import product


    for i in range(1, n + 1):
        for j in product("ATGC", repeat = i):
            yield list_to_string(j)


def translate_convertor(way, gen_code_table = "Standard"):

    from Bio import SeqIO

    with open(way, "r") as fasta_file:

        for record in SeqIO.parse(fasta_file,'fasta'):

            dna = record.seq

            yield record.id, dna.translate( table = gen_code_table )


print("This task contains 2 functions.\n "
      "1 is a generator of combinations of 4 basic nucleotides (A, T, G, C).\n "
      "2 is a generator of translated sequences obtained from the specified fasta file.\n"
      "To call the first function, press 1, the second - 2.)")

answer = input("Enter function number: ")

if answer == "1":

    try:
        number_of_combinations = int(input("Enter function number: "))
    except ValueError:
        print("Wrong value! Try again!")

    print(list(generate(number_of_combinations)))

elif answer == "2":

    try:
        input_way_to_file = input("Enter way to your file: ")
        gen_code_table = input("Type of gen code table. 'Standard' by default. "
                               "If you don't want to change anything, just press Enter. ")
    except FileNotFoundError:
        print("File not found! Try again!")

    if gen_code_table == '':
        for amino_acid in translate_convertor(input_way_to_file):
            print(amino_acid[0])
            print(amino_acid[1])
    else:
        try:
            for amino_acid in translate_convertor(input_way_to_file,gen_code_table):
                print(amino_acid[0])
                print(amino_acid[1])
        except (ValueError, KeyError) :
            print("Wrong gen code table! Try again!")
