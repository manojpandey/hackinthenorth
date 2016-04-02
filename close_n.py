import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


def compare_im(im1, im2):
    return np.sqrt(0.5*np.sum(np.power(np.sqrt(im1)-np.sqrt(im2), 2)))


def comp_im_01(im1, im2):
    return np.sqrt(np.sum(np.power(im1-im2, 2)))


def imload_reshape(im_name, w=100, h=100):
    im = cv2.imread(im_name)
    # height, width = im.shape[:2]
    im = cv2.resize(im, (w, h))
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return im


def best_match(imc):
    f = os.listdir('data')
    d = []
    for ix in f[:]:
        im = imload_reshape('data/'+ix)
        d.append(compare_im(imc, im))
        # d.append(comp_im_01(imc, im))
    return f[np.argmin(d)], np.min(d)


if __name__ == "__main__":
    f = os.listdir('data')
    k = 1
    name = f[k]
    imc = imload_reshape('data/'+f[k])
    # cv2.imshow('c', imc)
    print imc.shape
    d = []
    f.pop(k)
    for ix in f[:]:
        im = imload_reshape('data/'+ix)
        d.append(compare_im(imc, im))
        # d.append(comp_im_01(imc, im))
    # print d
    # print np.min(d), d.index(np.min(d)), np.argmin(d)
    print f[np.argmin(d)], name, f[np.argmax(d)]
    # ima = imload_reshape('data/'+f[np.argmin(d)])
    # cv2.imshow('a', ima)
    # cv2.waitKey(0)
