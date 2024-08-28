# iDAS
# By: Ashton Visuvasam

## Background

My father takes part in races in an online racing simulator known as iRacing. In each of his races, he receives a large telemetry file in the form of an IBT file that contains the variables listed in the Vars file in the repository. He asked me to analyze the file in order to draw insights on how to improve his time.

## Current Progress

So far in this project, I converted the IBT file to a CSV file using a library created by a GitHub user named kutu. I have queried the data to see how it is organized and how exactly to graph and visualize it, checking whether it needs to be cleaned. I have also graphed the change in tire temperature and tread throughout the race to visualize what is happening. After discussing with my father, we decided that the next course of action will be to analyze the steering and see how it performs throughout the race. I will post updates as the project continues and more insights are discovered.

## End Goal

While the end goal of the project is not totally known, one of the possibilities is to compare these files to those of the top racers and see the differences, finding ways to make up the differences.

## Sources Used

- [pyirsdk GitHub Repository](https://github.com/kutu/pyirsdk)
