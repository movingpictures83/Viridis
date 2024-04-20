import matplotlib.pyplot as plt
import seaborn as sns
import pandas

class ViridisPlugin:
 def input(self, inputfile):
  self.df = pandas.read_csv(inputfile)
 def run(self):
  plt.figure(figsize=(8,8))
  sns.heatmap(self.df.corr(), cmap="viridis")
 def output(self, outputfile):
  plt.savefig(outputfile)
