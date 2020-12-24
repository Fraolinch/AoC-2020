with open("input7", 'r') as file:
    bags = file.read().splitlines()

class Bag:
    def __init__(self, color, bags_inside):
        self.color = color
        self.bags_inside = bags_inside

#bag1 = Bag("vibrant salmon", None)    
#bag2 = Bag("dotted plum", {bag1.color: 3})

bags_classed = []

for bag in bags:
    bag = bag.split(' ')
    bags_inside = {}
    word = 4
    while word < len(bag):
        if bag[word] == "no":
            bags_inside = None
        else:
            bags_inside.update({"" + bag[word + 1] + " " + bag[word + 2]: bag[word]})
            word = word + 4
    bags_classed.append(Bag("" + bag[0] + " " + bag[1], bags_inside))
    print(bags_classed[0].color)
    print(bags_classed[0].bags_inside)
    quit()