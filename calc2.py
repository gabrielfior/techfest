# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:05:51 2016

@author: gabrielfior
"""

Matrix3x3 MakeMatrix( Vector3 X, Vector3 Y )  
{  
    // make sure that we actually have two unique vectors.
    assert( X != Y );

    Matrix3x3 M;  
    M.X = normalise( X );  
    M.Z = normalise( cross_product(X,Y) );
    M.Y = normalise( cross_product(M.Z,X) );  
    return M;
}