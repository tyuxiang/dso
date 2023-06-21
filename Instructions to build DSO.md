# Instructions to build DSO
## Steps:
1) Install all dependencies (follow instructions on the website: dont install the latest pangolin, install pangolin0.6, more instructions on how to install pagolin0.6 is given below)
2) Modify cmakelist.txt
```
# Include minimum CXX standard
set(CMAKE_CXX_STANDARD 17)
# Include NO_MODULE in find package EIGEN3
find_package(Eigen3 REQUIRED NO_MODULE)
```
3) Install previous version of Pangolin (0.6)
```
1) Download and extract the zip release of Pangolin 0.6
2) on Pangolin-0.6/include/pangolin/plot/range.h comment out include <Eigen/src/Geometry>
3) build and install Pangolin 0.6
4) run at the end: sudo make install
```
4) Modify script /dso/src/IOWrapper/OpenCV/ImageRW_OpenCV.cpp
```
Change all CV_LOAD_IMAGE_GRAYSCALE/COLOR/UNCHANGED to cv::IMREAD_GRAYSCALE/COLOR/UNCHANGED
```
5) Build DSO

# Additional changes to DSO
1) Included an execution_scripts folder which contains all the scripts required to run different datasets
2) Included an additional "experiment" argument to running DSO to specify what the current run is called
3) Included an additional "ts_path" argument to specify path to timestamp file
4) Included a section in the loadTimestamps method to be able to read timestamp file with only the timestamp as well
5) Included a restructure_time.py to restructure format of the oxford robotcar timestamp file

# TODO
1) Input time into the output file