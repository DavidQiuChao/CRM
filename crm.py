#!/usr/bin/env python
#coding=utf-8


import cv2
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve



def normValue(im):
    maxV = np.max(im)
    minV = np.min(im)
    im = (im-minV)/(maxV-minV+1e-6)
    return im


def diff(x,n,ax):
    '''
    # use forward difference
    # to approximate gradient
    '''
    return np.diff(x,n,ax)


def diffH(im):
    res = np.zeros(im.shape)
    res[:-1,:] = diff(im,1,0)
    res[-1,:] = im[0,:]-im[-1,:]
    return res


def diffW(im):
    res = np.zeros(im.shape)
    res[:,:-1] = diff(im,1,1)
    res[:,-1] = im[:,0]-im[:,-1]
    return res


def Exp(x,a,b):
    return np.exp((1-np.sign(x)*np.power(abs(x),a))*b)

def cameraModel(im,k):
    a = -0.3293
    b = 1.12458
    f = Exp(k,a,b)
    g = np.power(im,np.sign(k)*np.power(abs(k),a))*f
    return g


def exposureMap(im,win,alpha,rMax,eps):
    # init exposure map
    t0 = np.max(im,axis=2)
    H,W = t0.shape
    # exposure map refinement
    t0 = cv2.resize(t0,(int(W/2),int(H/2)))
    dt0h = diffH(t0)
    dt0w = diffW(t0)
    kh = np.zeros((win,win))
    kw = np.zeros((win,win))
    kh[:,2] = 1
    kw[2,:] = 1
    gsh = cv2.filter2D(dt0h,-1,kh)
    gsw = cv2.filter2D(dt0w,-1,kw)
    Wh = 1./(abs(gsh)*abs(dt0h)+eps)
    Ww = 1./(abs(gsw)*abs(dt0w)+eps)
    T = solveLinearEquation(t0,Wh,Ww,alpha/2.)
    T = cv2.resize(T,(W,H))
    T = np.expand_dims(T,2).repeat(3,2)
    kR = np.minimum(1./T,rMax)
    return kR


def solveLinearEquation(t0,Wh,Ww,alpha):
    H,W = t0.shape
    k = H*W
    # the main diagonals of symmetrix
    # positive definite laplacian matrix(SPDLM)
    dh = -alpha*Wh.flatten()
    dw = -alpha*Ww.flatten()
    temph = np.zeros(Wh.shape)
    temph[0,:] = Wh[-1,:]
    temph[1:,:] = Wh[:-1,:]
    tempw = np.zeros(Ww.shape)
    tempw[:,0] = Ww[:,-1]
    tempw[:,1:] = Ww[:,:-1]
    dha = -alpha*temph.flatten()
    dwa = -alpha*tempw.flatten()
    # the 4 sub-diagonals of SPDLM
    temph = np.zeros(Wh.shape)
    temph[-1,:] = Wh[-1,:]
    tempw = np.zeros(Ww.shape)
    tempw[:,-1] = Ww[:,-1]
    dhd1 = -alpha*temph.flatten()
    dwd1 = -alpha*tempw.flatten()
    Wh[-1,:] = 0
    Ww[:,-1] = 0
    dhd2 = -alpha*Wh.flatten()
    dwd2 = -alpha*Ww.flatten()
    dhd1 = np.expand_dims(dhd1,1)
    dhd2 = np.expand_dims(dhd2,1)
    dwd1 = np.expand_dims(dwd1,1)
    dwd2 = np.expand_dims(dwd2,1)
    ah = np.concatenate((dhd1,dhd2),axis=1)
    aw = np.concatenate((dwd1,dwd2),axis=1)
    Ah = sp.spdiags(ah.T,[-k+W,-W],k,k)
    Aw = sp.spdiags(aw.T,[-W+1,-1],k,k)
    # main diagonal
    D = 1-(dh+dw+dha+dwa)
    A = (Ah+Aw)+(Ah+Aw).T+sp.spdiags(D,[0],k,k)
    t0 = np.expand_dims(t0.flatten(),1).astype(np.float32)
    tout = spsolve(A,t0)
    out = np.reshape(tout,(H,W))
    out = normValue(out)
    return out


def CRM(src):
    alpha = 1
    eps = 0.001
    win = 5
    rMax = 7

    im = np.array(src.copy())
    im = im/255.
    kR = exposureMap(im,win,alpha,rMax,eps)
    J = cameraModel(im,kR)
    J = np.maximum(0,np.minimum(1,J))
    J = J*255.
    return J
