def create_vector(way):
    from Bio import SeqIO
    data_vector = []
    records = SeqIO.parse(way, "fasta")

    for i, seq_record in enumerate(records):
        length_value = seq_record.seq.count("A") + \
                       seq_record.seq.count("C") + \
                       seq_record.seq.count("G") + \
                       seq_record.seq.count("T")
        data_vector.append(length_value)

    return data_vector


def paint(vector):
    import matplotlib.pyplot as plt

    plt.hist(vector, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')
    plt.title('Distribution of sequences by length', fontsize=14)
    plt.xlabel('Length', fontsize=14)
    plt.ylabel('Numbers of length variant', fontsize=14)
    plt.grid(True)
    plt.show()


file_way = input("Write way to fasta: ")

try:
    data_to_paint_graph = create_vector(file_way)
except FileNotFoundError:
    print("Wrong way to file!")

paint(data_to_paint_graph)
