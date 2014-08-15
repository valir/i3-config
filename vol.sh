#!/bin/bash
vol=`amixer get Master | grep "Front Left:" | awk '{print $5}'`
echo $vol
