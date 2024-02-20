from autoqubo import Binarization, SamplingCompiler, SearchSpace, Utils
import dynex
import dimod


s = SearchSpace()
s.add('a', Binarization.uint, 3)
s.add('b', Binarization.uint, 3)


def ff(a, b):
    return 2 * a + 3 * b


q, offset = SamplingCompiler.generate_qubo_matrix(fitness_function=ff, input_size=s.size, searchspace=s)

print(q)

x = s.encode({'a': 3, 'b': 6})

print(s.decode(x))
print(s.decode_dict(x))

print(Utils.energy(q, x, offset=offset))
print(ff(3, 6))
