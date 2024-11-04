from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
	try:
		data = load("../life_expectancy_years.csv")
		data.set_index('country', inplace=True)
		data.loc['France'].plot()
		plt.title("France Life expectancy Projections")
		plt.xlabel("Year")
		plt.ylabel("Life expectancy")
		plt.show()
	except KeyboardInterrupt as error_msg:
		return


if __name__ == "__main__":
	main()