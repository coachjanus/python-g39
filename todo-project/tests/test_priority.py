import unittest
from todo_project.priority import Priority

class TestPriority(unittest.TestCase):
    def test_priority_values(self):
        self.assertEqual(Priority.NORMAL, 0)
        self.assertEqual(Priority.IMPORTANT, 1)
        self.assertEqual(Priority.CRITICAL, 2)
        
    def test_priority_names(self):
        self.assertEqual(Priority.NORMAL.name, "NORMAL")
        self.assertEqual(Priority.IMPORTANT.name, "IMPORTANT")
        self.assertEqual(Priority.CRITICAL.name, "CRITICAL")
        
    def test_priority_from_name(self):
        self.assertEqual(Priority.from_name("NORMAL"), Priority.NORMAL)
        self.assertEqual(Priority.from_name("IMPORTANT"), Priority.IMPORTANT)
        self.assertEqual(Priority.from_name("CRITICAL"), Priority.CRITICAL)
        
    def test_priority_from_name_invalid(self):
        with self.assertRaises(ValueError):
            Priority.from_name("INVALID")

if __name__ == "__main__":
    unittest.main()