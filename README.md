 #  AUTOmated QUBO Generator using the Dynex Platform

 AUTOmated QUBO Generator is an automatic tool for converting a high-level description
of an optimization problem, written in Python, into an equivalent QUBO representation.
It is doing this by using a novel **data driven** translation method that
can completely decouple the input and output representation.

<p align="center">
<img src="./doc/auto_qubo.png" alt= "overview of AutoQUBO" width="500" >
</p>


This repository acts as a companion to our publications:

1. Alberto Moraglio, Serban Georgescu, and Przemysław Sadowski. 2022. AutoQubo: Data-driven automatic QUBO generation. In Genetic and Evolutionary Computation Conference Companion (GECCO ’22 Companion), July 9–13, 2022, Boston, MA, USA. ACM, New York, NY, USA, 8 pages. https://doi.org/10.1145/3520304.3533965

2. Justin Pauckert, Mayowa Ayodele, Marcos Diez García, Serban Georgescu, and Matthieu Parizy. 2023. AutoQUBO v2: Towards Efficient and Effective QUBO Formulations for Ising Machines. In Genetic and Evolutionary Computation Conference Companion (GECCO ’23 Companion), July 15–19, 2023, Lisbon, Portugal. ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3583133.3590662

Installation
------------

install autoqubo as package:
```
pip install autoqubo
```

Example
-------
The maximum satisfiability problem (MAX-SAT) is the problem of determining the maximum number of clauses, of a given Boolean formula in conjunctive normal form, that can be made true by an assignment of truth values to the variables of the formula. One can define a weighted version of MAX-SAT as follows: given a conjunctive normal form formula with weights assigned to each clause, find truth values for its variables that maximize the combined weight of the satisfied clauses. The MAX-SAT problem is an instance of weighted MAX-SAT where all weights are 1. 

This example defines an objective function f(x), which is automatically converted and sampled on the Dynex Neuromorphic Computing Platform:
```
from autoqubo import Binarization, SamplingCompiler, SearchSpace, Utils
import dynex

def f(x):
    x1, x2, x3 = x
    val = 0

    # clause 1
    if x1 or not x2:
        val += 3
    # clause 2
    if x3:
        val += 1
    # clause 3
    if not x3 or x2:
        val += 4

    return val

# Automatically create the Qubo formulation based on function f()
# The solution is represetned by 3 bits
qubo, offset = SamplingCompiler.generate_qubo_matrix(fitness_function=f, use_multiprocessing=False, input_size=3)
print(qubo)

# Sample on the Dynex platform
sampleset = dynex.sample_qubo(qubo, offset, mainnet=False, num_reads=1024, annealing_time=200);

# Output result
print(sampleset)
```

Output:
```
[[ 0.  3.  0.]
 [ 0. -3.  4.]
 [ 0.  0. -3.]]

[DYNEX] PRECISION SET TO 0.0001
[DYNEX] SAMPLER INITIALISED
[DYNEX|TESTNET] *** WAITING FOR READS ***
╭────────────┬─────────────┬───────────┬───────────────────────────┬─────────┬─────────┬────────────────╮
│   DYNEXJOB │   BLOCK FEE │ ELAPSED   │ WORKERS READ              │ CHIPS   │ STEPS   │ GROUND STATE   │
├────────────┼─────────────┼───────────┼───────────────────────────┼─────────┼─────────┼────────────────┤
│         -1 │           0 │           │ *** WAITING FOR READS *** │         │         │                │
╰────────────┴─────────────┴───────────┴───────────────────────────┴─────────┴─────────┴────────────────╯

[DYNEX] FINISHED READ AFTER 0.00 SECONDS
[DYNEX] SAMPLESET READY

   0  1  2 energy num_oc.
0  0  0  1    4.0       1
['BINARY', 1 rows, 1 samples, 3 variables]
```

How to cite
-----------
If you find our work useful, please cite the paper below:

```
@inproceedings{10.1145/3520304.3533965,
    author = {Moraglio, Alberto and Georgescu, Serban and Sadowski, Przemys{\l}aw},
    title = {AutoQubo: Data-driven Automatic QUBO Generation},
    year = {2022},
    isbn = {978-1-4503-9268-6/22/07},
    publisher = {Association for Computing Machinery},
    doi = {10.1145/3520304.3533965},
    booktitle = {Proceedings of the Genetic and Evolutionary Computation Conference Companion},
    series = {GECCO '22} 
}
```




