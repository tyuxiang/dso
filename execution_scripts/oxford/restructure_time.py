import numpy as np
import argparse

def main(args):
    ts = np.loadtxt(args.ts_path)
    ts = ts[:,0]/1e6
    print(ts)
    np.savetxt(args.out_path, ts, fmt='%10.10f')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ts_path", help="path to ts")
    parser.add_argument("--out_path", help="path to save modified ts")

    args = parser.parse_args()

    # images_list = sorted(glob.glob(os.path.join(args.data_path, 'stereo/left_undistort/*.png')))
    # tstamps = [float(x.split('/')[-1][:-4])/1e6 for x in images_list][args.t0:args.t1]

    # Set it back to GT coordinate frame
    # Estimated Trajectory should be in the format of a 2D numpy array of: [[x1,y1,z1,qx1,qy1,qz1,qw1], [x2,y2,z2,qx2,qy2,qz2,qw2], ...]
    # traj_est = traj_est[:,[2,0,1,5,3,4,6]] # Use this line of code if the format of the data is in [[y1,z1,x1,qy1,qz1,qx1,qw1],...]


    main(args)