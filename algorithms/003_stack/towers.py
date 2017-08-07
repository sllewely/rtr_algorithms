import sys

def towers():
    # set up pegs and rings
    for ring in reversed(xrange(1, num_rings + 1)):
        p1.append(ring)
    print_status()

    # start by trying to move the bottom ring
    move_ring(p1[0], p1, p3, p2)
    print_move_count()

def move_ring(ring, source, dest, other):
    # base case: if ring is at top of stack, move it
    if ring == source[-1]:
        dest.append(source.pop()) # actually move the ring

        # keep track of number of moves and print what happened
        count_move(ring)
        print_status()
    else:
        next_ring = next_ring_above(ring, source)
        # try to move the next ring up in the stack to the "other" peg
        move_ring(next_ring, source, other, dest)
        # then move the current ring to the destination
        move_ring(ring, source, dest, other)
        # then move the next ring up on top of the current ring
        move_ring(next_ring, other, dest, source)

def next_ring_above(ring, source):
    next_index = source.index(ring) + 1
    return source[next_index]

def count_move(ring):
    key = str(ring)
    if key in move_log:
        move_log[key] += 1
    else:
        move_log[key] = 1

def print_move_count():
    for ring, num_moves in sorted(move_log.iteritems()):
        print("Ring {} was moved {} times".format(ring, num_moves))
    print("Total number of moves: {}".format(sum(move_log.values())))

def print_status():
    for i in reversed(xrange(num_rings)):
        ring1 = ring_to_s(p1, i)
        ring2 = ring_to_s(p2, i)
        ring3 = ring_to_s(p3, i)
        print("{}\t{}\t{}".format(ring1, ring2, ring3))
    print("")

def ring_to_s(peg, index):
    try:
        return peg[index]
    except IndexError:
        return "|"

if __name__ == "__main__":
    move_log = {}
    p1 = []
    p2 = []
    p3 = []
    if len(sys.argv) > 1:
        # if we run this script with an argument, e.g.
        # python towers.py 4, use that for the number of rings...
        num_rings = int(sys.argv[1])
    else:
        # or else use the default number 3
        num_rings = 3
    towers()
