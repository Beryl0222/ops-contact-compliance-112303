"""检查交换数据中用于回查的事实。"""
import unittest

import numpy as np

from contact_compliance_input import load_record


class ExchangeRecordTests(unittest.TestCase):
    def test_exchange_contract(self):
        record = load_record()
        self.assertTrue(record["cases"][0]["contact_ids"] == record["cases"][1]["contact_ids"][::-1])
        self.assertTrue(record["cases"][1]["basis_quarters"] != record["cases"][0]["basis_quarters"] and 0 in record["cases"][2]["mu"])
        self.assertTrue(all(np.max(np.abs(c["coupling"])) < np.min(c["diagonal"]) for c in record["cases"]))
        self.assertTrue(record["cases"][0]["force_limit"] != record["cases"][1]["force_limit"])
