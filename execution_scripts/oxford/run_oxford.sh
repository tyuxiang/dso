python3 restructure_time.py \
--ts_path /mnt/drive1/marvl/data/robotcar/2015-10-29-12-18-17/stereo.timestamps \
--out_path /home/marvl/Implementation/testing-suite/Methods/dso/execution_scripts/oxford/times.txt

cd /home/marvl/Implementation/testing-suite/Methods/dso/build

bin/dso_dataset \
files=/mnt/drive1/marvl/data/robotcar/2015-10-29-12-18-17/stereo/left_undistort/ \
calib=/home/marvl/Implementation/testing-suite/Methods/dso/execution_scripts/oxford/camera.txt \
preset=0 \
mode=1 \
start=1080 \
quiet=1 \
nogui=1 \
nolog=1 \
experiment=original.txt \
ts_path=/home/marvl/Implementation/testing-suite/Methods/dso/execution_scripts/oxford/times.txt
