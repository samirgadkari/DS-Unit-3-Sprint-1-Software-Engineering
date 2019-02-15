from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive',
              'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num: int = 30):
    """ Generate a list of products"""

    adjs = ADJECTIVES
    nouns = NOUNS
    products = []
    for i in range(num):
        adj = adjs[random.randint(0, len(adjs) - 1)]
        noun = nouns[random.randint(0, len(nouns) - 1)]
        name = adj + ' ' + noun

        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products.append(Product(name, price=price,
                                weight=weight,
                                flammability=flammability))
    return products


def inventory_report(products):
    """Print summary of product inventory"""

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: ", len(products))
    sum_price, sum_weight, sum_flammability = 0, 0, 0
    for p in products:
        sum_price += p.price
        sum_weight += p.weight
        sum_flammability += p.flammability

    print("Average price: ", sum_price/len(products))
    print("Average weight:", sum_weight/len(products))
    print("Average flammability:", sum_flammability/len(products))


if __name__ == '__main__':
    inventory_report(generate_products())
