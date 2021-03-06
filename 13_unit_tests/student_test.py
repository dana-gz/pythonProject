import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.jon = Student('Jon', 'Snow', 4.5, None)
        self.anna = Student('Anna', 'Smith', 4.6, None)

    def tearDown(self):
        del self.jon
        del self.anna


    def test_email_when_name_changed(self):
        self.assertEqual(self.jon.email, 'jon.snow@university.com')
        self.assertEqual(self.anna.email, 'anna.smith@university.com')

        self.jon.name = 'John'
        self.assertEqual(self.jon.email, 'john.snow@university.com')

        self.anna.name = 'Anne'
        self.assertEqual(self.anna.email, 'anne.smith@university.com')

    def test_fullname_value(self):
        self.assertEqual(self.jon.fullname, 'Jon Snow')

    def test_full_when_lastname_changed(self):
        self.assertEqual(self.anna.fullname, 'Anna Smith')

        self.anna.last = 'Kowalska'
        self.assertEqual(self.anna.fullname, 'Anna Kowalska')


    def test_grant_scholarschip(self):
        self.assertEqual(self.anna.scholarship, None)
        self.anna.grant_scholarship()
        self.assertEqual(self.anna.scholarship, True)

    def test_not_grant_scholarship(self):
        self.assertEqual(self.jon.scholarship, None)
        self.jon.grant_scholarship()
        self.assertEqual(self.jon.scholarship, False)


    def test_grand_scholarship_on_avg_change(self):
        self.assertEqual(self.jon.scholarship, None)
        self.jon.grant_scholarship()
        self.assertEqual(self.jon.scholarship, False)

        self.jon.student_avg = 5.0
        self.jon.grant_scholarship()
        self.assertEqual(self.jon.scholarship, True)



if __name__ == '__main__':
    unittest.main()