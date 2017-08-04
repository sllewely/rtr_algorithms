peg_1 = [5, 4, 3, 2, 1]
peg_2 = []
peg_3 = []

def move(source, destination):
    # print("moving top of {} to {}".format(source, destination))
    ring = source.pop()
    destination.append(ring)
    print_status()

def print_status():
    print("peg_1: {}, peg_2: {}, peg_3: {}".format(peg_1, peg_2, peg_3))

def move_two(source, destination, other):
    move(source, other)
    move(source, destination)
    move(other, destination)

def move_stack(source, destination, other):
    # print("moving {} to {}".format(source, destination))
    # base case
    if len(source) == 2:
        move_two(source, destination, other)
    else:
        # move all but the bottom to the other peg
        # move the bottom to the destination
        # move the rest from other to destination
        bottom = source[0] # assign bottom ring to a temporary variable
        print("bottom is {}".format(bottom))
        source.remove(bottom) # remove the bottom ring from the source temporarily p1 [2, 1] p2 [] p3 [] set aside = 3
        move_stack(source, other, destination) # move the rest of the source to the middle ring p1 [], p2 [2, 1] p3 [] set aside = 3
        source.append(bottom) # put the bottom ring back on the source p1 [3], p2 [2, 1] p3 [0]
        print_status()
        move(source, destination) # move the bottom ring to the destination p1 [], p2 [2, 1], p3 [3]
        move_stack(other, destination, source) # move the rest of the stack onto the bottom ring p1 [], p2 [] p3 [3, 2, 1]

def main():
    print_status()
    move_stack(peg_1, peg_3, peg_2)

if __name__ == "__main__":
    main()
