#!/usr/bin/env python

import unicornhat as unicorn
import time
import argparse

unicorn.brightness(0.1)

HEIGHT=8
WIDTH=8

parser = argparse.ArgumentParser(
    description="A small implementation of conways game of life")

parser.add_argument("-o", "--object", 
                    dest="conway_object", 
                    default="glider", 
                    help="Define object to print, e.g. glider, tripole, pentimo")
args = parser.parse_args()

def get_object(a):
    if args.conway_object == "glider":
        a[0,2] = "x"
        a[1,0] = "x"
        a[1,2] = "x"
        a[2,1] = "x"
        a[2,2] = "x"
        return a
    elif args.conway_object == "tripole":
        a[1,1] = "x"
        a[1,2] = "x"
        a[2,1] = "x"
        a[2,3] = "x"
        a[4,3] = "x"
        a[4,5] = "x"
        a[5,4] = "x"
        a[5,5] = "x"
        return a
    elif args.conway_object == "pentimo":
        a[3,4] = "x"
        a[4,3] = "x"
        a[4,4] = "x"
        a[4,5] = "x"
        a[5,3] = "x"
        return a

def main():
    a = {} #alivelist
    b = {} #birthlist
    d = {} #deathlist

    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            a[i,j] = None
            b[i,j] = None
            d[i,j] = None

    
    a = get_object(a)
    for i in range(0, HEIGHT, 1):
        for j in range(0, WIDTH, 1):
            if a[i,j] == "x":
                unicorn.set_pixel(i, j, 0, 255, 0)
            if a[i,j] == None:
                unicorn.set_pixel(i, j, 0, 0, 0)
    if b[i,j] == "x":
        print "b[%s,%s]" % (i,j)
    unicorn.show()
    time.sleep(1)
    
    while True:
        for i in range(0, HEIGHT):
            for j in range(0, WIDTH):
                b[i,j] = None
                d[i,j] = None
        try:
            for i in range(0, HEIGHT):
                for j in range(0, WIDTH):
                    n=0
                    if i > 0 and j > 0 and a[i-1,j-1] == "x":
                        n += 1
                    if j > 0 and a[i,j-1] == "x":
                        n += 1
                    if j > 0 and i < HEIGHT-1 and a[i+1,j-1] == "x":
                        n += 1
                    if i > 0 and a[i-1,j] == "x":
                        n += 1
                    if i < HEIGHT-1 and a[i+1,j] == "x":
                        n += 1
                    if j < WIDTH-1 and i > 0 and a[i-1,j+1] == "x":
                        n += 1
                    if j < WIDTH-1 and a[i,j+1] == "x":
                        n += 1
                    if i < HEIGHT-1 and j < WIDTH-1 and a[i+1,j+1] == "x":
                        n += 1


                    if n == 3 and a[i,j] == None:
                        b[i,j] = "x"
                    elif n == 2 and a[i,j] == "x" or n == 3 and a[i,j] == "x":
                        b[i,j] = "x"
                    elif n != 3:
                        d[i,j] = "x"
                    
                    #if b[i,j] == "x":
                    #    print "b[%s,%s]" % (i,j)
        except KeyError:
            print "KeyError"
            pass

        for i in range(0, HEIGHT, 1):
            for j in range(0, WIDTH, 1):
                if d[i,j] == "x":
                    a[i,j] = None
                if b[i,j] == "x":
                    a[i,j] = "x"

        #drawing
        for i in range(0, HEIGHT, 1):
            for j in range(0, WIDTH, 1):
                if a[i,j] == "x":
                    unicorn.set_pixel(i, j, 0, 255, 0)
                if a[i,j] == None:
                    unicorn.set_pixel(i, j, 0, 0, 0)
        unicorn.show()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
