import unittest

import sys
sys.path.append('..')
import xml_parser as app
import tulkotajs

class TestSum(unittest.TestCase):
    def test_replace_tex_by_id(self):
        id_dict = dict()
        result = tulkotajs.replace_tex_by_id('<source>aaa $a=1$ bbb $b=1$.</source>',id_dict)
        self.assertEqual(result,'<source>aaa §id1§ bbb §id2§.</source>')
        a = list(id_dict.keys())
        self.assertEqual(a, ['§id1§', '§id2§'])

    def test_xliff_translate(self):
        translated = tulkotajs.xliff_translate('Programming task Hairdressers', dict())
        self.assertEqual(translated, 'Programmēšanas uzdevumu frizieri')

if __name__ == '__main__':
    unittest.main()
