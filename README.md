# Image Classifier k-Nearest Neighbor (k-NN)
Chapter 7 of the Deep Learning for Computer Vision book. Exercise making an initial image classifier on animals data set.

Implementation of a simple k-Nearest Neighbor (k-NN) classifier.

>"Tell me who your neighbors are, and I'll tell you who you are"

## Running the

```$oython knn.py --dataset "../datasets/animals"```

results from first run:

```
[INFO] loading images...
[INFO] processed 500/3000
[INFO] processed 1000/3000
[INFO] processed 1500/3000
[INFO] processed 2000/3000
[INFO] processed 2500/3000
[INFO] processed 3000/3000
[INFO] features matrix; 8.8MB
[INFO] evaluating k-NN classifier...
              precision    recall  f1-score   support

        cats       0.40      0.56      0.46       249
        dogs       0.41      0.47      0.43       262
       panda       0.80      0.32      0.46       239

    accuracy                           0.45       750
   macro avg       0.53      0.45      0.45       750
weighted avg       0.53      0.45      0.45       750
```
## Environment for MacOS

create conda environment using;

```$conda env create -f dl4cv_environment.yml```
