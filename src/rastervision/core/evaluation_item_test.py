import unittest

from rastervision.core.evaluation_item import EvaluationItem


class TestEvaluationItem(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge_both_empty(self):
        a = EvaluationItem()
        b = EvaluationItem()
        a.merge(b)
        self.assertEqual(a.precision, None)
        self.assertEqual(a.recall, None)
        self.assertEqual(a.f1, None)
        self.assertEqual(a.count_error, None)
        self.assertEqual(a.gt_count, 0)

    def test_merge_first_empty(self):
        a = EvaluationItem()
        b = EvaluationItem(
            precision=1, recall=1, f1=1, count_error=0, gt_count=1)
        a.merge(b)
        self.assertEqual(a.precision, 1)
        self.assertEqual(a.recall, 1)
        self.assertEqual(a.f1, 1)
        self.assertEqual(a.count_error, 0)
        self.assertEqual(a.gt_count, 1)

    def test_merge_second_empty(self):
        a = EvaluationItem(
            precision=1, recall=1, f1=1, count_error=0, gt_count=1)
        b = EvaluationItem()
        a.merge(b)
        self.assertEqual(a.precision, 1)
        self.assertEqual(a.recall, 1)
        self.assertEqual(a.f1, 1)
        self.assertEqual(a.count_error, 0)
        self.assertEqual(a.gt_count, 1)

    def test_merge(self):
        a = EvaluationItem(
            precision=1, recall=1, f1=1, count_error=0, gt_count=1)
        b = EvaluationItem(
            precision=0, recall=0, f1=0, count_error=1, gt_count=2)
        a.merge(b)
        self.assertEqual(a.precision, 1 / 3)
        self.assertEqual(a.recall, 1 / 3)
        self.assertEqual(a.f1, 1 / 3)
        self.assertEqual(a.count_error, 2 / 3)
        self.assertEqual(a.gt_count, 3)


if __name__ == "__main__":
    unittest.main()
