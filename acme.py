class Product:
    """ Manage information about an Acme Product """

    id: int = 1000000
    id_max: int = 9999999

    def __init__(self,
                 name: str,
                 price: int = 10,
                 weight: int = 20,
                 flammability: float = 0.5):

        if Product.id > 9999999:
            raise(ValueError, "Cannot have more than " +
                              Product.id_max + "Products")
        self.identifier = Product.id
        Product.id += 1

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        """Compute stealability"""

        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif (ratio >= 0.5) and (ratio < 1.0):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Compute explosivity"""

        weight_times_flammability = \
            self.flammability * self.weight

        if weight_times_flammability < 10:
            return "...fizzle."
        elif (weight_times_flammability >= 10) and \
             (weight_times_flammability < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """BoxingGlove product information and behavior"""

    def __init__(self,
                 name: str,
                 weight: int = 10):
        super().__init__(name, weight=weight)

    def explode(self):
        """BoxingGlove explosivity calculation"""

        return "...it's a glove."

    def punch(self):
        """BoxingGlove punch hurt calculation"""

        if self.weight < 5:
            return "That tickles."
        elif (self.weight > 5) and (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
