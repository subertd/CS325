from runner.runner import Runner
from algorithm.collective_algorithm import RealTSPAlgorithm


runner = Runner(RealTSPAlgorithm())
runner.load()
runner.run()
