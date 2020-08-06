# Clustering and prediction of trajectories of air objects

## Problem Statement
>The position of an object in the air can be indicated by latitude, longitude and altitude for a given time. A trajectory is a stream of such quadruples (time, latitude, longitude and altitude). Given a large set of such trajectories, without any other information, problem is to cluster them into meaningful objects such as Helicopter, Fighter/civilian Aircraft, UAV, Cruise Missile, dropped bomb, etc. An optimal scalable solution is desired using open source tools. Design a system to estimate location of flying object based on its trajectory, provide guidance to missile to shoot them depending on their location when missile will meet the object on its trajectory.

## Clustering Air Objects
    Clustering of air trajectories by k-Means algorithm using feature extraction.

![Alt text](./Results/cluster.jpeg?raw=true "Title")

## Prediction of Trajectories
    Prediction of missing parts of trajectories, predicting future course of an air object through LSTM models
![Alt text](./Results/3d_prediction.jpeg?raw=true "Title")

## Missile Guidance
    Integrated system where continous prediction of trajectory of foreign object and setting the course for the counter missile based on that.

## Technology stack
1. ### Python Packages for data processing and cleaning
    * Pandas
    * Numpy
2. ### Python Packages for deep learning.
    * PyTorch
3. ### User Interface
    * HTML, CSS, JS
    * Node.js, Express.js
    * Folium (Python Package)


## Possible future improvements
    Layered LSTM's, bi-directional LSTM's to improve prediction performance.
    Dynamic Training of LSTM

## Team

| [Sriram](https://github.com/sri1299) | [Karthik Udupa](https://github.com/k-udupa2000) | [Vikram C.P](www.github.com/sri1299) |
| :---: | :---: | :---: |




| [ParithiMalan](https://www.github.com/superhakar) | [Nachiappan S K](https://www.github.com/nachiappan14) | [Manasa Kashyap](https://github.com/manasa28) |
| :---: | :---: | :---: |
