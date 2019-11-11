class Pozdrav:
    """
    KLasa ktera zdravi
    """
    text="nevim co mam rict"
    def pozdrav(self,jmeno):
        """
        KLasa zdravi uzviatele
        :param jmeno:
        :return:

        """
        return "{0} {1}!".format(self.text, jmeno)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
