class Axiom:

    def __init__(self, name, axiom):
        self.name = name
        self.axiom = axiom
    
    def check_axiom(self, generator, scf):
        print("Checking if rule {} adheres to axiom {} using generator mode {}.".format(scf.name, self.name, generator.mode))
        while not generator.is_done():
            P = generator.next()
            f = scf.apply_rule(P)
            if not self.axiom(P, f):
                print("Axiom {} not valid.\nCounter example:\nP: {}\nscf(P): {}".format(self.name, P, f))
                return False
        print("Axiom {} valid, no counter examples found for generator settings.".format(self.name))
        return True