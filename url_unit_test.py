import unittest
import url_status
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        urls = []
        url_file = open("urls.txt", "r")
        for i in url_file.readlines():
            urls.append(i.strip())
        url_file.close()
        #urls = ['https://httpstat.us/200','https://httpsttat.us/200']
        for i in urls:
            print(i)
            respone_of_test = url_status.get_url_status(i)
            self.assertEqual(200,200)

if __name__ == '__main__':
    unittest.main()
