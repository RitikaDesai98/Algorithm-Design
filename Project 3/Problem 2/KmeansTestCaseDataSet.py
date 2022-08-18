import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('ggplot')


class K_Means:
    def __init__(self, k=2, tolerance=0.0001, max_iterations=100):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def fit(self, data):
        self.centroids = {}

        # initialize the centroids, the first 'k' elements in the dataset will be our initial centroids
        for i in range(self.k):
            self.centroids[i] = data[i]

        # begin iterations
        for j in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

            # find the distance between the point and cluster; choose the nearest centroid
            loss_sum = 0
            for features in data:
                distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids]
                #print(distances)
                classification = distances.index(min(distances))
                loss_sum += (min(distances) ** 2)
                self.classes[classification].append(features)
            final_loss = loss_sum/len(data)
            print("Loss in iteration " +str(j) +": "+ str(final_loss))

            previous = dict(self.centroids)

            # average the cluster datapoints to re-calculate the centroids
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)

            isOptimal = True

            for centroid in self.centroids:

                original_centroid = previous[centroid]
                curr = self.centroids[centroid]

                if np.sum((curr - original_centroid) / original_centroid * 100.0) > self.tolerance:
                    isOptimal = False

            # break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
            if isOptimal:
                break

    def pred(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        #print(classification)
        return classification


def main():
    df = pd.read_csv("./Project3_Test_Case.csv")
    df = df[['X1', 'X2']]
    dataset = df.astype(float).values.tolist()

    X = df.values  # returns a numpy array
    #print(X)

    km = K_Means(2)
    km.fit(X)

    # Plotting starts here
    colors = 10 * ["r", "g", "c", "b", "k"]

    print("Coordinates of centroids are: ")
    for centroid in km.centroids:
        print(km.centroids[centroid][0], km.centroids[centroid][1])
        plt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], s=130, marker="x")

    for classification in km.classes:
        color = colors[classification]
        print("Number of points in cluster "+str(classification) + " = " + str(len(km.classes[classification])))
        for features in km.classes[classification]:
            plt.scatter(features[0], features[1], color=color, s=30)


    #plt.show()


if __name__ == "__main__":
    main()