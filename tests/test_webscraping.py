import unittest

from webscraping import Scp
# from scraping import set_url_and_tag
# import scraping

class ScpTest(unittest.TestCase):

    # -----上級編----------

    @classmethod
    def setUpClass(cls):
        cls.scp = Scp()
        print('初期化')

    @classmethod
    def tearDownClass(cls):
        del cls.scp
        print('削除')

    def setUp(self):
        print('テストケースのsetup')

    def tearDown(self):
        print('テストケースのteardown')

    def test_set_url_and_tag(self):
        url = 'https://zerofromlight.com/blogs/'
        tag = 'h5'
        datas = self.scp.set_url_and_tag(url, tag)
        # データ型の判定
        self.assertIsInstance(datas, list,
                '戻り値はリスト型である')

    # @unittest.skipIf(Scp.__version__ > '3.0.0',
    #         "依存関係のライブラリが更新されたのでスキップ")
    # @unittest.skip('スキップします。')
    def test_set_url_and_tag_raise(self):
        no_https_url = 'zerofromlight.com/blogs'
        tag = 'h5'
        with self.assertRaisesRegex(ValueError,
                'Invalid URL:Example is https://example.com/.'):
            self.scp.set_url_and_tag(no_https_url, tag)
    
    # def test_set_url_and_tag_raise(self):
    #     if Scp.__version__ > '3.0.0':
    #         self.skipTest(
    #                 '依存関係のライブラリが更新されたのでスキップ')
    #     no_https_url = 'zerofromlight.com/blogs'
    #     tag = 'h5'
    #     with self.assertRaisesRegex(ValueError,
    #             'Invalid URL:Example is https://example.com/.'):
    #         self.scp.set_url_and_tag(no_https_url, tag)

    # ----中級編----------
    # def test_set_url_and_tag(self):
    #     url = 'https://zerofromlight.com/blogs/'
    #     tag ='h5'
    #     datas = set_url_and_tag(url, tag)
    #     # データ型の判定
    #     self.assertIsInstance(datas, list,
    #             '戻り値はリスト型である')
    # 
    # 
    # def test_set_url_and_tag_raise(self):
    #     no_https_url = 'zerofromlight.com/blogs'
    #     tag = 'h5'
    #     with self.assertRaisesRegex(ValueError,
    #             'Invalid URL:Example is https://example.com/.'):
    #         set_url_and_tag(no_https_url, tag)

        # with self.assertRaises(ValueError) as cm:
        #     self.scp.set_url_and_tag(no_https_url, tag)
        # the_exc = cm.exception
        # self.assertEqual(the_exc.args[0],
        #         'Invalid URL:Example is https://example.com/.')
    
    
    # ----初級編２----------
    # def test_set_url_and_tag_result(self):
    #     url = 'https://zerofromlight.com/blogs/'
    #     tag = 'h5'
    #     datas = set_url_and_tag(url, tag)
    #     # データ型の判定
    #     self.assertIsInstance(datas, list,
    #             '戻り値はリスト型である')

    # ----初級編１----------
    # def test_scp(self):
    #     pass


if __name__ == '__main__':
    unittest.main()

