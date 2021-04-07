
class SCF:

    def __init__(self, name, rule):
        self.name = name
        self.rule = rule
    
    def apply_rule(self, P):
        #print("{} rule:".format(self.name))
        return self.rule(P)

    def apply_rule_arg(self, arg, P):
        print("{} rule with arg {}:".format(self.name, arg))
        return self.rule(arg, P)
                                              
                                              
class Condorcet(SCF):
    def __init__():
        super.__init__("Condorcet")

    def apply_rule():
        pass