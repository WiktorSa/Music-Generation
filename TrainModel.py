import argparse
import numpy as np
import torch
import torch.nn as nn
from os.path import join


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dt', default='data', help='Directory with data', type=str, required=False)
    parser.add_argument('-sr', default=16000, help='Sample rate of all songs (in Hz)', type=int, required=False)
    parser.add_argument('-lp', default=0.25, help='Length of sample (in seconds)', type=float, required=False)
    parser.add_argument('-nb', default=40, help='Batch size', type=int, required=False)
    parser.add_argument('-hs', default=2048, help='Hidden size', type=int, required=False)
    parser.add_argument('-dp', default=0.2, help='Value of dropout in linear layer', type=float, required=False)
    parser.add_argument('-lr', default=1e-4, help='Learning rate', type=float, required=False)
    parser.add_argument('-wd', default=1e-4, help='Value of weight decay in optimizer', type=float, required=False)
    parser.add_argument('-ep', default=2000, help='Number of epochs', type=int, required=False)
    parser.add_argument('-md', default='model', help='Directory where model should be saved', type=int, required=False)
    parser.add_argument('-sd', default=1001, help='Seed', type=int, required=False)
    return parser


if __name__ == '__main__':
    data_parser = create_parser()
    args = data_parser.parse_args()

    data = np.load(join(args.dt, 'data.npz'))
