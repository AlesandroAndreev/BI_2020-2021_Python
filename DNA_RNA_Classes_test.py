import unittest

import DNA_and_RNA_classes
from DNA_and_RNA_classes import DNA
from DNA_and_RNA_classes import RNA


class NucleicTest(unittest.TestCase):

    def setUp(self):

        self.dna_zero = DNA("")
        self.dna_g = DNA('GGGGGGGGGGGGGGG')
        self.dna_different_registr = DNA('AtGcAAATTGCc')
        self.dna_normal = DNA('ATGCCAAATTGCCA')

        try:
            self.other_DNA = DNA("ATGCCAAAIQTTGCCA")
        except TypeError:
            self.other_DNA = "This is not DNA!"

        self.rna_zero = RNA("")
        self.rna_g = RNA('GGGGGGGGGGGGGGG')
        self.rna_different_registr = RNA('AuGcAAAuuGCc')
        self.rna_normal = RNA('AUGCCAAAUUGCCA')

        try:
            self.other_RNA = RNA("AUGCCAAAIQTTGCCU")
        except TypeError:
            self.other_RNA = "This is not RNA!"

    def test_init(self):

        self.assertEqual(self.dna_zero.seq, '',
                         'Нарушенна последовательность ДНК!')
        self.assertEqual(self.dna_g.seq,
                         'GGGGGGGGGGGGGGG',
                         'Нарушенна последовательность ДНК!')
        self.assertEqual(self.dna_different_registr.seq,
                         'AtGcAAATTGCc',
                         'Нарушенна последовательность ДНК!')
        self.assertEqual(self.dna_normal.seq,
                         'ATGCCAAATTGCCA',
                         'Нарушенна последовательность ДНК!')

        self.assertEqual(self.rna_zero.seq, '',
                         'Нарушенна последовательность РНК!')
        self.assertEqual(self.rna_g.seq,
                         'GGGGGGGGGGGGGGG',
                         'Нарушенна последовательность РНК!')
        self.assertEqual(self.rna_different_registr.seq,
                         'AuGcAAAuuGCc',
                         'Нарушенна последовательность РНК!')
        self.assertEqual(self.rna_normal.seq,
                         'AUGCCAAAUUGCCA',
                         'Нарушенна последовательность РНК!')

    def test_eq(self):

        self.assertTrue(self.dna_zero == self.dna_zero,
                        "Неравенство не соблюдено!")
        self.assertTrue(self.dna_g == self.dna_g,
                        "Неравенство не соблюдено!")
        self.assertTrue(
            self.dna_different_registr == self.dna_different_registr,
            "Неравенство не соблюдено!")
        self.assertTrue(self.dna_normal == self.dna_normal,
                        "Неравенство не соблюдено!")

        self.assertTrue(self.rna_zero == self.rna_zero,
                        "Неравенство не соблюдено!")
        self.assertTrue(self.rna_g == self.rna_g,
                        "Неравенство не соблюдено!")
        self.assertTrue(
            self.rna_different_registr == self.rna_different_registr,
            "Неравенство не соблюдено!")
        self.assertTrue(self.rna_normal == self.rna_normal,
                        "Неравенство не соблюдено!")

        self.assertEqual(
            self.dna_normal.reverse_complement().seq,
            'TGGCAATTTGGCAT',
            'Не правильный Revers-compliment!')

    def test_self_type(self):

        self.assertIsInstance(self.dna_zero, DNA_and_RNA_classes.DNA,
                              'Не верный формат! Ожидалась ДНК!')
        self.assertIsInstance(self.dna_g, DNA_and_RNA_classes.DNA,
                              'Не верный формат! Ожидалась ДНК!')
        self.assertIsInstance(self.dna_different_registr,
                              DNA_and_RNA_classes.DNA,
                              'Не верный формат! Ожидалась ДНК!')
        self.assertIsInstance(self.dna_normal, DNA_and_RNA_classes.DNA,
                              'Не верный формат! Ожидалась ДНК!')

        self.assertIsInstance(self.rna_zero, DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')
        self.assertIsInstance(self.rna_g, DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')
        self.assertIsInstance(self.rna_different_registr,
                              DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')
        self.assertIsInstance(self.rna_normal, DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')

    def test_other_nc(self):

        self.assertEqual(self.other_DNA, "This is not DNA!",
                         "Код пропустил неожиданные символы!")
        self.assertEqual(self.other_RNA, "This is not RNA!",
                         "Код пропустил неожиданные символы!")

    def test_revers_compliment(self):

        self.assertEqual(self.dna_zero.reverse_complement().seq, '',
                         'Не правильный Revers-compliment!')
        self.assertEqual(self.dna_g.reverse_complement().seq,
                         'CCCCCCCCCCCCCCC',
                         'Не правильный Revers-compliment!')
        self.assertEqual(self.dna_different_registr.reverse_complement().seq,
                         'gGCAATTTgCaT',
                         'Не правильный Revers-compliment!')
        self.assertEqual(self.dna_normal.reverse_complement().seq,
                         'TGGCAATTTGGCAT',
                         'Не правильный Revers-compliment!')

        self.assertEqual(self.rna_zero.reverse_complement().seq, '',
                         'Не правильный Revers-compliment!')
        self.assertEqual(self.rna_g.reverse_complement().seq,
                         'CCCCCCCCCCCCCCC',
                         'Не правильный Revers-compliment!')
        self.assertEqual(self.rna_different_registr.reverse_complement().seq,
                         'gGCaaUUUgCaU',
                         'Не правильный Revers-compliment!')
        self.assertEqual(self.rna_normal.reverse_complement().seq,
                         'UGGCAAUUUGGCAU',
                         'Не правильный Revers-compliment!')

    def test_transcription(self):

        self.assertIsInstance(self.dna_zero.transcribe(),
                              DNA_and_RNA_classes.RNA,
                              'Неправильная Транскрипция! Ожидалась РНК!')
        self.assertIsInstance(self.dna_g.transcribe(),
                              DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')
        self.assertIsInstance(self.dna_different_registr.transcribe(),
                              DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')
        self.assertIsInstance(self.dna_normal.transcribe(),
                              DNA_and_RNA_classes.RNA,
                              'Не верный формат! Ожидалась РНК!')

        self.assertEqual(self.dna_zero.transcribe().seq, '',
                         'Транскрипция не верная!')
        self.assertEqual(self.dna_g.transcribe().seq,
                         'CCCCCCCCCCCCCCC',
                         'Транскрипция не верная!')
        self.assertEqual(self.dna_different_registr.transcribe().seq,
                         'gGCAAUUUgCaU',
                         'Транскрипция не верная!')
        self.assertEqual(self.dna_normal.transcribe().seq,
                         'UGGCAAUUUGGCAU',
                         'Транскрипция не верная!')

    def test_gc(self):

        self.assertEqual(self.dna_zero.gc_content(), 0,
                         'Нарушенна последовательность ДНК!')
        self.assertEqual(self.dna_g.gc_content(), 100,
                         'Нарушенна последовательность ДНК!')
        self.assertEqual(self.dna_different_registr.gc_content(),
                         round((5/12)*100, 2),
                         'Нарушенна последовательность ДНК!')
        self.assertEqual(self.dna_normal.gc_content(),
                         round((6/14)*100, 2),
                         'Нарушенна последовательность ДНК!')

        self.assertEqual(self.rna_zero.gc_content(), 0,
                         'Нарушенна последовательность РНК!')
        self.assertEqual(self.rna_g.gc_content(), 100,
                         'Нарушенна последовательность РНК!')
        self.assertEqual(self.rna_different_registr.gc_content(),
                         round((5/12)*100, 2),
                         'Нарушенна последовательность РНК!')
        self.assertEqual(self.rna_normal.gc_content(),
                         round((6/14)*100, 2),
                         'Нарушенна последовательность РНК!')

    def test_iter(self):
        self.assertListEqual([x for x in self.dna_zero.seq], [],
                             "Нарушенна последовательность итерации!!!")
        self.assertListEqual([x for x in self.dna_g .seq],
                             ['G', 'G', 'G', 'G', 'G', 'G',
                              'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                             "Нарушенна последовательность итерации!!!")
        self.assertListEqual([x for x in self.dna_different_registr.seq],
                             ['A', 't', 'G', 'c', 'A',
                              'A', 'A', 'T', 'T', 'G', 'C', 'c'],
                             "Нарушенна последовательность итерации!!!")
        self.assertListEqual([x for x in self.dna_normal.seq],
                             ['A', 'T', 'G', 'C', 'C', 'A',
                              'A', 'A', 'T', 'T', 'G', 'C', 'C', 'A'],
                             "Нарушенна последовательность итерации!!!")

        self.assertListEqual([x for x in self.rna_zero.seq], [],
                             "Нарушенна последовательность итерации!!!")
        self.assertListEqual([x for x in self.rna_g .seq],
                             ['G', 'G', 'G', 'G', 'G', 'G', 'G',
                              'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                             "Нарушенна последовательность итерации!!!")
        self.assertListEqual([x for x in self.rna_different_registr.seq],
                             ['A', 'u', 'G', 'c', 'A', 'A',
                              'A', 'u', 'u', 'G', 'C', 'c'],
                             "Нарушенна последовательность итерации!!!")
        self.assertListEqual([x for x in self.rna_normal.seq],
                             ['A', 'U', 'G', 'C', 'C', 'A',
                              'A', 'A', 'U', 'U', 'G', 'C', 'C', 'A'],
                             "Нарушенна последовательность итерации!!!")


if __name__ == '__main__':
    unittest.main()
