#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        """Test product stealability"""
        prod = Product('Test Product', price=10, weight=10)
        self.assertEqual(prod.stealability(), "Very stealable!")

    def test_explode(self):
        """Test product explosivity"""
        prod = Product('Test Product', flammability=1.0, weight=100)
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num_products(self):
        """Test the number of default products in inventory."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test names of products are valid"""
        products = generate_products()
        res = True
        for p in products:
            adj, noun = p.name.split()
            if (adj not in ADJECTIVES) or (noun not in NOUNS):
                res = False
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
